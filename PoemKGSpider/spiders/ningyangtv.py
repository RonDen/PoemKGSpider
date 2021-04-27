import scrapy
from scrapy import Request, Selector
import requests
from urllib import parse
from PoemKGSpider.util import reg_int, get_years
from PoemKGSpider.service.mysql import Poem
from PoemKGSpider.items import TopicItem, DynastyItem, BookItem, MingjvItem, IdiomItem


class NYBookSpider(scrapy.Spider):
    name = 'nybook'
    allowed_domains = ['www.ningyangtv.cn/']
    start_urls = ['http://www.ningyangtv.cn/book/']
    _base_url = 'http://www.ningyangtv.cn/'
    _origin = 'ningyangtv'

    def parse(self, response, **kwargs):
        lis = response.xpath('/html/body/div[2]/div[1]/ul/li')
        for li in lis:
            title = li.css('strong a::text').get()
            link = li.css('strong a::attr(href)').get()
            book_id = reg_int(link)
            url = parse.urljoin(self._base_url, link)
            img_link = li.css('a img::attr(src)').get()
            img_url = parse.urljoin(self._base_url, img_link)
            author_name = li.css('span a::text').get("")
            author_link = li.css('span a::attr(href)').get()
            if not author_name:
                author_link = ""
            author_id = reg_int(author_link)
            _meta = {
                "book_title": title,
                "book_id": book_id,
                "book_url": url,
                "book_img": img_url,
                "book_author": author_name,
                "book_author_id": author_id
            }
            yield Request(url, callback=self._parse_one_book, dont_filter=True, meta=_meta)
        # parse next page
        if response.css('.page a::text')[-2].get() == '下一页':
            link = response.css('.page a::attr(href)')[-2].get()
            url = parse.urljoin(self._base_url, link)
            yield Request(url, callback=self.parse, dont_filter=True)

    def _parse_one_book(self, response):
        info = response.meta
        detail = '\n'.join([d.strip() for d in response.css('#cc ::text').getall()])
        chapter = ' '.join(response.css('dl ul li a::text').getall())
        book = {
            'origin': 'ningyangtv',
            'origin_id': info.get('book_id'),
            'url': info.get('book_url'),
            'title': info.get('book_title'),
            'author': info.get('book_author'),
            'author_id': info.get('book_author_id'),
            'detail': detail,
            'chapter': chapter,
            'img_url': info.get('book_img')
        }
        yield BookItem(book)


class NYDynastySpider(scrapy.Spider):
    name = 'nydynasty'
    allowed_domains = ['www.ningyangtv.cn/']
    start_urls = ['http://www.ningyangtv.cn/shiren/']
    _base_url = 'http://www.ningyangtv.cn/'
    _origin = 'ningyangtv'

    def start_requests(self):
        for i in range(15, 16):
            url = "http://www.ningyangtv.cn/chaodai/{}.html".format(i)
            _meta = {
                'url': url,
                'id': i,
            }
            yield Request(url, callback=self._parse_one_dynasty, dont_filter=True, meta=_meta)

    def _parse_one_dynasty(self, response):
        if response.css('center'):
            return
        info = response.meta
        name = response.xpath('/html/body/div[2]/div[1]/div[5]/h2/text()').get()
        detail = '\n'.join([d.strip() for d in response.css('dd ::text').getall()])
        start, end = get_years(detail)

        dynasty = {
            'origin': 'ningyangtv',
            'origin_id': info.get('id'),
            'url': info.get('url'),
            'name': name,
            'detail': detail,
            'start': start,
            'end': end
        }
        yield DynastyItem(dynasty)

    def _parse(self, response, **kwargs):
        pass


class NYIdiomSpider(scrapy.Spider):
    name = 'nyidiom'
    allowed_domains = ['www.ningyangtv.cn/']
    start_urls = ['http://www.ningyangtv.cn/shiren/']
    _base_url = 'http://www.ningyangtv.cn/'
    _origin = 'ningyangtv'

    def start_requests(self):
        for i in range(5, 13035):
            url = "http://www.ningyangtv.cn/chengyu/{}.html".format(i)
            _meta = {
                'url': url,
                'id': i,
            }
            yield Request(url, callback=self._parse_one_idiom, dont_filter=True, meta=_meta)

    def _parse_one_idiom(self, response):
        if response.css('center'):
            return
        info = response.meta
        content = response.xpath('/html/body/div[2]/div[1]/div[5]/h2/text()').get("")
        pingyin = response.xpath('/html/body/div[2]/div[1]/div[5]/dl/dd[1]/text()').get("").strip()
        explain = response.xpath('/html/body/div[2]/div[1]/div[5]/dl/dd[2]/text()').get("").strip()
        come_from = "".join([d.strip() for d in response.css('.article dd')[2].css('::text').getall()])
        example = response.xpath('/html/body/div[2]/div[1]/div[5]/dl/dd[4]/text()').get('').strip()
        idiom = {
            'origin': 'ningyangtv',
            'origin_id': info.get('id'),
            'url': info.get('url'),
            'content': content,
            'pingyin': pingyin,
            'explain': explain,
            'come_from': come_from,
            'example': example
        }
        yield IdiomItem(idiom)

    def _parse(self, response, **kwargs):
        pass


class NYMingjvSpider(scrapy.Spider):
    name = 'nymingjv'
    allowed_domains = ['www.ningyangtv.cn/']
    start_urls = ['http://www.ningyangtv.cn/shiren/']
    _base_url = 'http://www.ningyangtv.cn/'
    _origin = 'ningyangtv'

    def start_requests(self):
        inf = 5870
        for i in range(5, inf):
            url = "http://www.ningyangtv.cn/juzi/{}.html".format(i)
            _meta = {
                'url': url,
                'id': i,
            }
            yield Request(url, callback=self._parse_one_mingjv, dont_filter=True, meta=_meta)

    def _parse_one_mingjv(self, response):
        if response.css('center'):
            return
        info = response.meta
        content = response.xpath('/html/body/div[2]/div[1]/div[5]/h2/text()').get('').strip()
        author, come_from = response.css('.article em a::text').getall()
        author_link, come_from_link = response.css('.article em a::attr(href)').getall()
        author_id, come_from_id = reg_int(author_link), reg_int(come_from_link)
        mingjv = {
            'origin': 'ningyangtv',
            'origin_id': info.get('id', 0),
            'url': info.get('url', 0),
            'content': content,
            'come_from': come_from,
            'come_from_id': come_from_id,
            'author': author,
            'author_id': author_id
        }
        yield MingjvItem(mingjv)

    def _parse(self, response, **kwargs):
        pass


class NYTopicSpider(scrapy.Spider):
    name = 'nytopic'
    allowed_domains = ['www.ningyangtv.cn/']
    start_urls = ['http://www.ningyangtv.cn/']
    _base_url = 'http://www.ningyangtv.cn/'
    _origin = 'ningyangtv'
    _template = "http://www.ningyangtv.cn/gushi/0/0/0/{}/0/0/"
    """
    1 - 写景
    2 - 咏物
    3 - 描写春天
    4 - 描写夏天 ...
    """

    def parse(self, response, **kwargs):
        pass

    def start_requests(self):
        html_text = requests.get('http://www.ningyangtv.cn/gushi/0/0/0/400/0/1/').text
        response = Selector(text=html_text)
        topic_names = response.xpath('//*[@id="type"]/a/text()').getall()
        topic_links = response.xpath('//*[@id="type"]/a/@href').getall()
        for name, link in zip(topic_names, topic_links):
            url = parse.urljoin(self._base_url, link)
            topic_id = int(link.split('/')[5])
            topic = {
                'origin': 'ningyangtv',
                'origin_id': topic_id,
                'url': url,
                'name': name
            }
            yield Request(self._base_url, callback=self._return_item, dont_filter=True, meta={'topic': topic})
            # yield Request(url, callback=self._parse_one_topic, meta={'topic_name': name, 'topic_id': topic_id},
            #               dont_filter=False)

    def _return_item(self, response):
        yield TopicItem(response.meta.get('topic', {}))

    def _parse_one_topic(self, response):
        topic_name = response.meta.get('topic_name', '')
        poem_hrefs = response.xpath('/html/body/div[2]/div[1]/ul/li/strong/a/@href').getall()
        poem_ids = list(map(reg_int, poem_hrefs))
        topic_id = response.meta.get('topic_id', 0)

        for poem_id in poem_ids:
            poem_select = Poem.select().where(Poem.origin_id==poem_id)
            for poem in poem_select:
                if poem.topic:
                    topics = set(poem.topic.split(' '))
                    topics.add(topic_name)
                    poem.topic = " ".join(list(topics))
                else:
                    poem.topic = topic_name
                poem.save()
        # parse one page finished
        # go to next page
        if response.css('.page a::text')[-2].get() == '下一页':
            link = response.css('.page a::attr(href)')[-2].get()
            url = parse.urljoin(self._base_url, link)
            yield Request(url, callback=self._parse_one_topic, meta={'topic_name': topic_name, 'topic_id': topic_id}, dont_filter=False)


