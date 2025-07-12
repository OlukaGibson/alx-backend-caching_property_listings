DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'property_db',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'db',  # service name in docker-compose
        'PORT': '5432',
    }
}

INSTALLED_APPS = [
    # ...
    'properties',
    'django_redis',
]

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
