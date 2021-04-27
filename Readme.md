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
（注，该爬虫项目经过一次重构，原版本未使用scrapy这种体量较大的框架，而是基于requests和BeautifulSoup4来抓取和提取数据，并集成了fake-useragent、ip-proxy等技术，还自己实现了日志记录logger、常用正则表达式、日期处理等小模块，但是后来发现需要爬取的网站几乎没有反爬措施，并且希望提升代码的复用性，因此用Scrapy进行重构。得益于twisted非阻塞IO的特点，基于scrapy实现后，爬取速度得到了数倍的提升。）


