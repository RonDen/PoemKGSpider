import requests
import scrapy
from scrapy import Request, Selector
from PoemKGSpider.util import reg_int
from urllib import parse
from PoemKGSpider.items import NYPoemItem




class NYPoemSpider(scrapy.Spider):
    name = 'nypoem'
    allowed_domains = ['www.ningyangtv.cn/']
    start_urls = ['http://www.ningyangtv.cn/gushi/']
    _page_size = 11
    _base_url = 'http://www.ningyangtv.cn/'
    _origin = 'ningyangtv'

    def start_requests(self):
        poem_num = 62500
        # poem_num = 10
        for i in range(1, poem_num):
            url = 'http://www.ningyangtv.cn/shi/{}.html'.format(i)
            yield Request(url=url, callback=self.parse_one_poem, meta={"poem_id": i})

    def parse_one_poem(self, response):
        if response.css('center'):
            return
        title = response.css('div .article h2::text').extract_first()
        if '貔貅' in title:
            return
        dds = response.css('dd')
        ems = response.css('em')
        dynasty = ems[1].css('a::text').extract_first()
        author = ems[0].css('a::text').extract_first()
        _author_url = ems[0].css('a::attr(href)').extract_first()
        author_id = -1
        if not author:
            author = ems[0].css('::text').extract()[0][3:]
            author_url = ''
            author_id = -1
        else:
            author_url = parse.urljoin(self._base_url, _author_url)
            author_id = reg_int(_author_url)
        _content = dds[0].css('::text').extract()
        _pingyin = dds[1].css('::text').extract()
        content = "\n".join([c.strip() for c in _content])
        pingyin = "\n".join([c.strip() for c in _pingyin])
        translate_detail = ""
        shangxi_detail = ""
        if dds[2].css('a::attr(href)'):
            _translate_url = dds[2].css('a::attr(href)').extract()[0]
            translate_url = parse.urljoin(self._base_url, _translate_url)
            translate_detail = self._get_translate(translate_url)
        if dds[3].css('a::attr(href)'):
            shangxi_detail = ",".join(list(map(str, set(map(reg_int, dds[3].css('a::attr(href)').getall())))))
        poem = {
            'origin': self._origin,
            'origin_id': response.meta['poem_id'],
            'url': response.url,
            'title': title,
            'content': content,
            'pingyin': pingyin,
            'author_id': author_id,  # -1 means no detail information
            'author': author,
            'author_url': author_url,
            'dynasty': dynasty,
            'translate': translate_detail,
            'shangxi': shangxi_detail
        }
        yield NYPoemItem(poem)

    def _get_translate(self, url: str):
        response = requests.get(url)
        selector = Selector(text=response.text)
        _details = selector.css('dd p::text').extract()
        res = '\n'.join([d.strip() for d in _details])
        return res
