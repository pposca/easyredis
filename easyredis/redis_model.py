class RedisModel:
    # TODO Add documentation to RedisModel
    # TODO Add tests to RedisModel
    def __init__(self, key, redis=False):
        # TODO Add documentation to RedisModel.__init__
        # TODO Add tests to RedisModel.__init__
        self.key = key
        self.redis = redis

    def exists(self, redis=False):
        # TODO Add documentation to RedisModel.exists
        # TODO Add tests to RedisModel.exists
        redis = redis or self.redis
        return redis.exists(self.key)

    @staticmethod
    def decode_value(value):
        # TODO Add documentation to RedisModel.decode_value
        # TODO Add tests to RedisModel.decode_value
        def dec(v):
            return v.decode() if isinstance(v, bytes) else v

        if isinstance(value, bytes):
            return dec(value)
        elif isinstance(value, dict):
            return {dec(k): dec(v) for k, v in value.items()}
        elif isinstance(value, list):
            return [dec(v) for v in value]
