from elasticsearch import Elasticsearch
from mysql import Poem, Author


es_client = Elasticsearch()


def poem_to_es():
    for poem in Poem.select():
        try:
            doc = {
                'id': poem.id,
                'title': poem.title,
                'origin': poem.origin,
                'origin_id': poem.origin_id,
                'content': poem.content,
                'author': poem.author,
                'dynasty': poem.dynasty,
                'translate': poem.translate,
                'url': poem.url
            }
            es_client.create(id=poem.id, index='poem',body=doc)
        except Exception as ex:
            print(poem.id)
            print(ex)


def author_to_es():
    for author in Author.select():
        try:
            doc = {
                'id': author.id,
                'name': author.name,
                'origin': author.origin,
                'origin_id': author.origin_id,
                'detail': author.detail,
                'dynasty': author.dynasty,
                'img_url': author.img_url,
                'url': author.url
            }
            es_client.create(id=author.id, index='poem',body=doc)
        except Exception as ex:
            print(author.id)
            print(ex)


if __name__ == '__main__':
    poem_to_es()
