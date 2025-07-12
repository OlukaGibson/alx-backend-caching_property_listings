from django.core.cache import cache
from .models import Property
from django_redis import get_redis_connection
import logging

def get_all_properties():
    properties = cache.get('all_properties')
    if properties is None:
        properties = Property.objects.all()
        cache.set('all_properties', properties, 3600)
    return properties

def get_redis_cache_metrics():
    r = get_redis_connection("default")
    info = r.info()
    hits = info.get('keyspace_hits', 0)
    misses = info.get('keyspace_misses', 0)
    total = hits + misses
    hit_ratio = hits / total if total > 0 else 0
    logging.info(f"Cache metrics — Hits: {hits}, Misses: {misses}, Hit Ratio: {hit_ratio:.2f}")
    return {"hits": hits, "misses": misses, "hit_ratio": round(hit_ratio, 2)}
