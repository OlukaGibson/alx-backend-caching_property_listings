# ALX Django Caching Project

This project demonstrates caching in Django using Redis and PostgreSQL, with Docker for environment setup.

## 🚀 Features
- PostgreSQL + Redis setup via Docker Compose
- Redis-backed cache for property list views
- Low-level cache for queryset with invalidation
- Cache hit/miss tracking with Redis INFO

## 📦 Stack
- Django
- Redis
- PostgreSQL
- docker-compose
- django-redis

## ⚙️ Run the Project

### 1. Start Services
```bash
docker-compose up -d
```

###  2. Run Migrations
```bash
docker-compose exec web python manage.py migrate
```

docker-compose exec web python manage.py shell
>>> from properties.utils import get_redis_cache_metrics
>>> get_redis_cache_metrics()
