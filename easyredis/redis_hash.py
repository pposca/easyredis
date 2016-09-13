from easyredis import RedisModel


class RedisHash(RedisModel):
    # TODO Add documentation to RedisHash
    # TODO Add tests to RedisHash
    def __init__(self, key, redis=False):
        # TODO Add documentation to RedisHash.__init__
        # TODO Add tests to RedisHash.__init__
        super().__init__(key, redis)

    def get(self, fields=None, redis=False, decode=True):
        # TODO Add documentation to RedisHash.get
        # TODO Add tests to RedisHash.get
        redis = redis or self.redis

        result = None
        if not fields:
            result = redis.hgetall(self.key)
        elif isinstance(fields, list):
            result = redis.hmget(self.key, fields)
        elif isinstance(fields, str):
            result = redis.hget(self.key, fields)

        if decode:
            result = self.decode_value(result)

        return result

    def set(self, fields, value=None, redis=False):
        # TODO Add documentation to RedisHash.set
        # TODO Add tests to RedisHash.set
        redis = redis or self.redis

        result = None
        if isinstance(fields, dict):
            result = redis.hmset(self.key, fields)
        elif isinstance(fields, str):
            result = redis.hset(self.key, fields, value)

        return result

    def has_field(self, field, redis=False):
        # TODO Add documentation to RedisHash.has_field
        # TODO Add tests to RedisHash.has_field
        redis = redis or self.redis

        return redis.hexists(field)

    def incr(self, field, value, redis=False):
        # TODO Add documentation to RedisHash.incr
        # TODO Add tests to RedisHash.incr
        redis = redis or self.redis

        return self.hincrby(self.key, field, value, redis)
