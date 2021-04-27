# 古诗文爬虫与知识图谱构建

本项目爬取了常见古诗词网站，并对数据进行分析和存储，以支持知识图谱的分析与构建。

## 爬取的网站

[http://www.ningyang.cn/](http://www.ningyang.cn/)

## 爬取的内容

- 古诗词、古文等：Poem
- 作者、诗人：Author
- 成语：Idiom
- 朝代历史信息：Dynasty
- 古籍信息：Book
- 分类信息：Topic
- 名句：Mingjv

## 存储数据库

- MySQL
- MongoDB
- neo4j
- ElasticSearch

## 爬虫实现技术

主要基于Scrapy框架进行数据爬取和采集。
（注，该爬虫项目经过一次重构，[原版本](https://github.com/RonDen/spider-snippet) 未使用scrapy这种体量较大的框架，而是基于requests和BeautifulSoup4来抓取和提取数据，并集成了fake-useragent、ip-proxy等技术，还自己实现了日志记录logger、常用正则表达式、日期处理等小模块，但是后来发现需要爬取的网站几乎没有反爬措施，并且希望提升代码的复用性，因此用Scrapy进行重构。得益于twisted非阻塞IO的特点，基于scrapy实现后，爬取速度得到了数倍的提升。）

## 项目细节与代码实例

### MySQL表结构定义

示例：古诗词的表结构定义

```mysql
CREATE TABLE `poemkg2`.`poem`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'mysql自增id',
  `origin` varchar(20) NOT NULL DEFAULT "" COMMENT '爬取来源',
  `origin_id` int NOT NULL DEFAULT -1 COMMENT '在爬取来源中的id',
  `url` varchar(200) NOT NULL DEFAULT "" COMMENT '诗词来源的url',
  `title` varchar(200) NOT NULL DEFAULT "" COMMENT '诗词标题',
  `content` longtext NOT NULL COMMENT '诗词内容',
  `pingyin` longtext NOT NULL COMMENT '诗词的拼音',
  `author_id` int NOT NULL DEFAULT -1 COMMENT '诗词作者，来源网站中的作者id，-1表示没有更多信息',
  `author` varchar(20) NOT NULL DEFAULT "" COMMENT '作者姓名',
  `author_url` varchar(200) NULL DEFAULT "" COMMENT 'url，如果author_id为-1，url无效',
  `dynasty` varchar(10) NOT NULL DEFAULT "" COMMENT '诗歌创作朝代',
  `translate` longtext NOT NULL COMMENT '诗歌的翻译信息',
  `shangxi` varchar(200) NOT NULL DEFAULT "" COMMENT '诗歌的赏析信息，使用逗号分隔赏析文章列表',
  `create_at` DATETIME NOT NULL DEFAULT NOW() COMMENT '该条记录创建时间，用于记录和更新',
  `update_at` DATETIME NOT NULL DEFAULT NOW() COMMENT '该条记录修改时间',
  `topic` varchar(100) NOT NULL DEFAULT "" COMMENT  '所在topic',
  `book` varchar(100) NOT NULL DEFAULT "" COMMENT  '来源书籍',
  PRIMARY KEY (`id`),
  INDEX `origin_id_idx`(`origin_id`) USING BTREE,
  INDEX `title_idx`(`title`) USING BTREE,
  INDEX `author_idx`(`author`) USING BTREE,
  INDEX `dynasty`(`dynasty`) USING BTREE,
  INDEX `book_idx`(`book`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=1;
```

更多示例内容见[ddl.sql](./PoemKGSpider/ddl.sql)文件。

### Pipeline设计示例

```python
# 通用的将内容存入Json文件的pipeline
class CommonJsonPipeline:
    def __init__(self, file_prefix):
        self.result_file = 'results/{}/{}-{}.json'.format(file_prefix, file_prefix, datetime.now().strftime("%Y-%m-%d-%H_%M_%S"))
        self.result_writer = open(self.result_file, 'w', encoding='utf8')

    def process_item(self, item, spider):
        self.result_writer.write(_encoder.encode(item))
        self.result_writer.write('\n')
        return item

    def __del__(self):
        self.result_writer.close()

# 只需要集成CommonJsonPipeline，并提供名称参数即可
class NYPoemJsonPipeline(CommonJsonPipeline):
    def __init__(self):
        super(NYPoemJsonPipeline, self).__init__('poem-dynasty')

# 处理Mysql数据库写入的管线，这里使用了peewee便捷的orm模型，Poem是一个peewee Model对象
# 由于item是一个DictItem的实例，因此可以使用`**item`来操作
class NYPoemMysqlPipeline:
    def __init__(self):
        super(NYPoemMysqlPipeline, self).__init__()

    def process_item(self, item, spider):
        poem = Poem(**item)
        poem.save()
        return item
```

更多内容见[pipeline.py](./PoemKGSpider/pipelines.py)文件。

