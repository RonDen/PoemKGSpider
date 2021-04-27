from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from elasticsearch_dsl import Document, Integer, Keyword, Text


es_client = Elasticsearch()


class PoemIndex(Document):
    id = Integer()
    title = Text(analyzer='ik_max_word', search_analyzer='ik_smart')
    origin = Keyword()
    origin_id = Integer()
    url = Keyword()
    content = Text(analyzer='ik_max_word', search_analyzer='ik_smart')
    author = Keyword()
    dynasty = Text(analyzer='ik_max_word', search_analyzer='ik_smart')
    translate = Text(analyzer='ik_max_word', search_analyzer='ik_smart')

    class Meta:
        index = "poem"


class AuthorIndex(Document):
    id = Integer()
    name = Keyword()
    origin = Keyword()
    origin_id = Integer()
    detail = Text(analyzer='ik_max_word', search_analyzer='ik_smart')
    dynasty = Text(analyzer='ik_max_word', search_analyzer='ik_smart')
    img_url = Keyword()
    url = Keyword()

    class Meta:
        index = "author"


if __name__ == '__main__':
    PoemIndex.init(index="poem")
    AuthorIndex.index(index="author")
