# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BaseItem(scrapy.Item):
    origin = scrapy.Field()
    origin_id = scrapy.Field()
    url = scrapy.Field()


class NYPoemItem(scrapy.Item):
    origin = scrapy.Field()
    origin_id = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    pingyin = scrapy.Field()
    author_id = scrapy.Field()
    author = scrapy.Field()
    author_url = scrapy.Field()
    dynasty = scrapy.Field()
    translate = scrapy.Field()
    shangxi = scrapy.Field()


class NYAuthorItem(scrapy.Item):
    origin = scrapy.Field()
    origin_id = scrapy.Field()
    url = scrapy.Field()
    dynasty = scrapy.Field()
    name = scrapy.Field()
    detail = scrapy.Field()
    img_url = scrapy.Field()


class TopicItem(scrapy.Item):
    origin = scrapy.Field()
    origin_id = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()


class BookItem(scrapy.Item):
    origin = scrapy.Field()
    origin_id = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    author_id = scrapy.Field()
    detail = scrapy.Field()
    img_url = scrapy.Field()
    chapter = scrapy.Field()


class DynastyItem(BaseItem):
    name = scrapy.Field()
    start = scrapy.Field()
    end = scrapy.Field()
    detail = scrapy.Field()


class IdiomItem(BaseItem):
    content = scrapy.Field()
    pingyin = scrapy.Field()
    explain = scrapy.Field()
    come_from = scrapy.Field()
    example = scrapy.Field()


class MingjvItem(BaseItem):
    content = scrapy.Field()
    come_from = scrapy.Field()
    come_from_id = scrapy.Field()
    author = scrapy.Field()
    author_id = scrapy.Field()


if __name__ == '__main__':
    def __test_topic_save():
        topic = {"origin": "ningyangtv", "origin_id": 29, "url": "http://www.ningyangtv.cn/gushi/0/0/0/29/0/0/", "name": "离别诗"}
        item = TopicItem(topic)
        from service.mysql import Topic
        from service.mongo import mongo_db

        t = Topic(**item)
        t.save()
        mongo_db.poemkg.topic.insert_one({**item})

    def __test_save():
        from service.mysql import Poem
        poem = {
            "origin": "ningyangtv",
            "origin_id": 3,
            "url": "http://www.ningyangtv.cn/shi/3.html", "title": "灞陵行送别", "content": "送君灞陵亭，灞水流浩浩。\r\n上有无花之古树，下有伤心之春草。\r\n我向秦人问路岐，云是王粲南登之古道。\r\n古道连绵走西京，紫阙落日浮云生。\r\n正当今夕断肠处，骊歌愁绝不忍听。", "pingyin": "sòng jun1 bà líng tíng ，bà shuǐ liú hào hào 。\r\nshàng yǒu wú huā zhī gǔ shù ，xià yǒu shāng xīn zhī chūn cǎo 。\r\nwǒ xiàng qín rén wèn lù qí ，yún shì wáng càn nán dēng zhī gǔ dào 。\r\ngǔ dào lián mián zǒu xī jīng ，zǐ què luò rì fú yún shēng 。\r\nzhèng dāng jīn xī duàn cháng chù ，lí gē chóu jué bú rěn tīng 。\n※提示：拼音为程序生成，因此多音字的拼音可能不准确。\n", "author_id": 242, "author": "李白", "author_url": "http://www.ningyangtv.cn/shiren/242.html", "dynasty": "唐朝", "translate": "", "shangxi": ""}
        item = NYPoemItem(poem)
        # poem = Poem(**item)
        # poem.save()
        from service.mongo import mongo_db
        mongo_db.poemkg.poem.insert_one({**poem})

    def __test():

        poem = {"origin": "ningyangtv", "origin_id": 3, "url": "http://www.ningyangtv.cn/shi/3.html", "title": "灞陵行送别", "content": "送君灞陵亭，灞水流浩浩。\r\n上有无花之古树，下有伤心之春草。\r\n我向秦人问路岐，云是王粲南登之古道。\r\n古道连绵走西京，紫阙落日浮云生。\r\n正当今夕断肠处，骊歌愁绝不忍听。", "pingyin": "sòng jun1 bà líng tíng ，bà shuǐ liú hào hào 。\r\nshàng yǒu wú huā zhī gǔ shù ，xià yǒu shāng xīn zhī chūn cǎo 。\r\nwǒ xiàng qín rén wèn lù qí ，yún shì wáng càn nán dēng zhī gǔ dào 。\r\ngǔ dào lián mián zǒu xī jīng ，zǐ què luò rì fú yún shēng 。\r\nzhèng dāng jīn xī duàn cháng chù ，lí gē chóu jué bú rěn tīng 。\n※提示：拼音为程序生成，因此多音字的拼音可能不准确。\n", "author_id": 242, "author": "李白", "author_url": "http://www.ningyangtv.cn/shiren/242.html", "dynasty": "唐朝", "translate": "", "shangxi": ""}

        item = NYPoemItem(poem)
        from scrapy.utils.serialize import ScrapyJSONEncoder
        encoder = ScrapyJSONEncoder(ensure_ascii=False)
        with open('debug.txt', 'w', encoding='utf8') as f:
            f.write(encoder.encode(item))
            f.write('\n')

    # __test_save()
    __test_topic_save()
