class Config:
    SQLALCHEMY_DATABASE_URI = "mysql://root:password@db/travel_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "supersecret"
    JWT_SECRET_KEY = "jwtsecret"

    # Redis cache
    CACHE_TYPE = "RedisCache"
    CACHE_REDIS_URL = "redis://redis:6379/0"
