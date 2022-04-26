from flask_restful import Resource
from api.services import redisService
from datetime import datetime
import json
from api.utils.logging_handler import LoggingHandler
from api.services import RedisService

logger = LoggingHandler.getLogger()
class LastmessagetimeforHibernatRasa(Resource):
    def get(self):
        limt = redisService.get("last_incomingmessage_time")
        # logger.info(limt)
        # if limt:
        #     return {"limt":limt}, 200
        # else:
        #     logger.info("in else")
        #     RedisService().set("last_incomingmessage_time",float(datetime.now().timestamp()), False)
        #     return {"limt":float(datetime.now().timestamp())}, 200

