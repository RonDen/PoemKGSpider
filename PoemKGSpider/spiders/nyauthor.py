import scrapy
import math
from scrapy import Request
from PoemKGSpider.util import reg_int
from PoemKGSpider.items import NYAuthorItem
from urllib import parse


class NYAuthorSpider(scrapy.Spider):
    name = 'nyauthor'
    allowed_domains = ['www.ningyangtv.cn/']
    start_urls = ['http://www.ningyangtv.cn/shiren/']
    _base_url = 'http://www.ningyangtv.cn/'
    _origin = 'ningyangtv'

    def start_requests(self):
        for i in range(1, 3000):
            url = 'http://www.ningyangtv.cn/shiren/{}.html'.format(i)
            yield Request(url=url, meta={"author_id": i}, callback=self._parse_one_author)

    def _parse_one_author(self, response):
        if response.css('center'):
            return
        dds = response.css('dd')
        ems = response.css('em')
        _details = dds[0].css('p::text').extract()
        details = '\n'.join([d.strip() for d in _details])
        dynasty = ems[0].css('a::text').extract_first()
        name = response.css('div .article h2::text').extract_first().split(' ')[0]
        img_url = self._base_url
        if dds.css('img'):
            _img_url = dds.css('img::attr(src)').extract_first()
            img_url = parse.urljoin(self._base_url, _img_url)
        author = {
            'origin': self._origin,
            'origin_id': response.meta['author_id'],
            'url': response.url,
            'dynasty': dynasty,
            'name': name,
            'detail': details,
            'img_url': img_url
        }
        yield NYAuthorItem(author)
