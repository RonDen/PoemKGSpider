# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from datetime import datetime
from scrapy.utils.serialize import ScrapyJSONEncoder
from PoemKGSpider.service.mysql import Poem, Author, Topic, Book, Idiom, Dynasty, Mingjv
from PoemKGSpider.service.mongo import mongo_db


_encoder = ScrapyJSONEncoder(ensure_ascii=False)


class PoemkgspiderPipeline:
    def process_item(self, item, spider):
        return item


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


class NYPoemJsonPipeline(CommonJsonPipeline):
    def __init__(self):
        super(NYPoemJsonPipeline, self).__init__('poem-dynasty')


class NYPoemMysqlPipeline:
    def __init__(self):
        super(NYPoemMysqlPipeline, self).__init__()

    def process_item(self, item, spider):
        poem = Poem(**item)
        poem.save()
        return item


class NYPoemMongoPipeline:
    def __init__(self):
        super(NYPoemMongoPipeline, self).__init__()

    def process_item(self, item, spider):
        mongo_db.poemkg.poem.insert_one({**item})
        return item


class NYAuthorJsonPipeline(CommonJsonPipeline):
    def __init__(self):
        super(NYAuthorJsonPipeline, self).__init__('author')


class NYAuthorMysqlPipeline:
    def __init__(self):
        super(NYAuthorMysqlPipeline, self).__init__()

    def process_item(self, item, spider):
        author = Author(**item)
        author.save()
        return item


class NYAuthorMongoPipeline:
    def __init__(self):
        super(NYAuthorMongoPipeline, self).__init__()

    def process_item(self, item, spider):
        mongo_db.poemkg.author.insert_one({**item})
        return item


class NYTopicJsonPipeline(CommonJsonPipeline):
    def __init__(self):
        super(NYTopicJsonPipeline, self).__init__('topic')


class NYTopicMysqlPipeline:
    def __init__(self):
        super(NYTopicMysqlPipeline, self).__init__()

    def process_item(self, item, spider):
        topic = Topic(**item)
        topic.save()
        return item


class NYTopicMongoPipeline:
    def __init__(self):
        super(NYTopicMongoPipeline, self).__init__()

    def process_item(self, item, spider):
        mongo_db.poemkg.topic.insert_one({**item})
        return item


class NYBookJsonPipeline(CommonJsonPipeline):
    def __init__(self):
        super(NYBookJsonPipeline, self).__init__('book')


class NYBookMysqlPipeline:
    def __init__(self):
        super(NYBookMysqlPipeline, self).__init__()

    def process_item(self, item, spider):
        # books = Book.select().where(Book.origin_id==item.origin_id)
        book = Book(**item)
        book.save()
        return item


class NYBookMongoPipeline:
    def __init__(self):
        super(NYBookMongoPipeline, self).__init__()

    def process_item(self, item, spider):
        mongo_db.poemkg.book.insert_one({**item})
        return item


class NYDynastyJsonPipeline(CommonJsonPipeline):
    def __init__(self):
        super(NYDynastyJsonPipeline, self).__init__('dynasty')


class NYDynastyMysqlPipeline:
    def __init__(self):
        super(NYDynastyMysqlPipeline, self).__init__()

    def process_item(self, item, spider):
        dynasty = Dynasty(**item)
        dynasty.save()
        return item


class NYDynastyMongoPipeline:
    def __init__(self):
        super(NYDynastyMongoPipeline, self).__init__()

    def process_item(self, item, spider):
        mongo_db.poemkg.dynasty.insert_one({**item})
        return item


class NYIdiomJsonPipeline(CommonJsonPipeline):
    def __init__(self):
        super(NYIdiomJsonPipeline, self).__init__('idiom')


class NYIdiomMysqlPipeline:
    def __init__(self):
        super(NYIdiomMysqlPipeline, self).__init__()

    def process_item(self, item, spider):
        idiom = Idiom(**item)
        idiom.save()
        return item


class NYIdiomMongoPipeline:
    def __init__(self):
        super(NYIdiomMongoPipeline, self).__init__()

    def process_item(self, item, spider):
        mongo_db.poemkg.idiom.insert_one({**item})
        return item


class NYMingjvJsonPipeline(CommonJsonPipeline):
    def __init__(self):
        super(NYMingjvJsonPipeline, self).__init__('mingjv')


class NYMingjvMysqlPipeline:
    def __init__(self):
        super(NYMingjvMysqlPipeline, self).__init__()

    def process_item(self, item, spider):
        mingjv = Mingjv(**item)
        mingjv.save()
        return item


class NYMingjvMongoPipeline:
    def __init__(self):
        super(NYMingjvMongoPipeline, self).__init__()

    def process_item(self, item, spider):
        mongo_db.poemkg.mingjv.insert_one({**item})
        return item