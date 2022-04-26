import redis
import os
from api.utils.logging_handler import LoggingHandler
logger = LoggingHandler.getLogger()

class RedisService:
    def __init__(self):       
        #host hardcoded as such should be name of redis container
        self.client = redis.Redis(host=os.getenv('REDIS_URL', 'redis'), port=6379,decode_responses=True, username=os.getenv('REDIS_USERNAME'), password = os.getenv('REDIS_PASSWORD') )
    
    def set(self,key_name,key_value,set_expire=True,expire_time=500):
        self.client.set(key_name,key_value)
        logger.info(f"$$$$$$ set {key_name} : {key_value}")
        if set_expire:
            self.client.expire(key_name,expire_time) # set expire time to 100 seconds
    
    def get(self,key_name,default=""):
        value = self.client.get(key_name)
        # logger.info(f"$$$$$$ get {key_name} : {value}")
        if value is None:
            return default
        else:
            return value

    def delete(self, key_name):
        try:
            value = self.client.delete(key_name)
            if value:
                logger.info(f"Key {key_name} deleted from redis")
            else:
                logger.info(f'key {key_name} does not exist')
        except Exception as e:
            logger.info(e)

    def set_values_to_key(self, dict_key, key_name, key_value,set_expire=True, expire_time=10000):
        value = self.client.hset(dict_key, key_name, key_value)
        # logger.info(self.client.hget(dict_key, ))
        if set_expire:
            self.client.expire(key_name,expire_time)
        if value:
            logger.info(f"Key {dict_key} added to redis")
        else:
            logger.info(f'key {dict_key} is not added to redis')
    def hget(self, dict_key, key_name):
        value = self.client.hget(dict_key, key_name)
        if value:
            logger.info(f'retrived values for {dict_key} are {value}')
            return value
        else:
            logger.info(f'retriving failed')
            return None