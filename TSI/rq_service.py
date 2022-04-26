from rq import Queue
from redis import Redis

from api.utils.logging_handler import LoggingHandler
import os
logger = LoggingHandler.getLogger()

from api.services.redis_service import RedisService


class RedisQue:
    def __init__(self):       
        self.redis_conn = RedisService().client
        self.rq = Queue(connection= self.redis_conn)
    
    def get_length(self):
        return len(self.rq)
    
    def create_job_broadcast(self, data):
        logger.info(f'##### background job request data : {data}')

        job = self.rq.enqueue(broadcast_job, kwargs=data)

        if job == None:
            logger.error("JOB could not be Created")
            # there should be some retry mechanism
        else:
            logger.info(f"##### Task {job.id} is added in queue at {job.enqueued_at}")
        return job
    def create_job_hibernate_rasa(self):
        # logger.info(f'creating job for hibernating rasa x')
        job = self.rq.enqueue(hibernate_rasa, (os.getenv("RASA_IDEAL_TIME")))
        # if job == None:
        #     logger.error("Job could not be created for hibernating rasa x")
        # else:
        #     logger.info(f'##### Task {job.id} is added in queue at {job.enqueued_at}')
        # return job

# job function need to give reference here, otherwise comm will generate error
# in actually RQ will use job function which is define in RQ container.
def broadcast_job():
    pass
def hibernate_rasa():
    pass