import redis
from redis_lru import RedisLRU
from models import Author, Quote

client = redis.StrictRedis(host='localhost', port=6379, password=None)
cache = RedisLRU(client)

@cache
def find_by_tag(tag: str) -> list[str | None]:
    quotes = Quote.objects(tags__iregex=tag)
    return [x.quote for x in quotes]

@cache
def find_by_author(fullname: str) -> dict[str, list[str]]:
    authors = Author.objects(fullname__iregex=fullname)
    result = {}
    for a in authors:
        quotes = Quote.objects(author=a)
        result[a.fullname] = [x.quote for x in quotes]
    return result

@cache
def find_by_tags(tags: list[str]) -> list[str]:
    quotes = Quote.objects(tags__in=tags)
    return [x.quote for x in quotes]
