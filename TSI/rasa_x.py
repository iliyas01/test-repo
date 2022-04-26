import json
from flask import Flask, request
from flask.wrappers import Response
from flask_restful import Resource
import boto3
import time, os
from api.utils.logging_handler import LoggingHandler
logger = LoggingHandler.getLogger()

class Rasa_X(Resource):

    def get(self):
        # ec2 = EC2()
        # state = ec2.perform(action = 'STATUS')state,
        return  200
    
                                                            
    def post(self):

        request_data = request.get_json(force=True)            
        #logger.info("####### Request Data Found: {}".format(request_data))         
        action = request_data['action']
        logger.info(f'##### Action to perform on EC2 Instance : {action}')
        
        # ec2 = EC2()
        # response = ec2.perform(action)
        #logger.info(f'  ##### Response from EC2 : {response}')response,
        return  200



class EC2:

    def __init__(self):
        #TODO: should come form env
        self.rasa_x_instance_id =os.getenv('RASA_X_INSTANCE_ID')
        region = 'us-east-1'
        access_id = os.getenv('AWS_ACCESS_KEY_ID')
        secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
        self.ec2 = boto3.client('ec2',region_name = region,
                                aws_access_key_id = access_id,
                                aws_secret_access_key = secret_key
                                )


    def get_state(self):
        response = self.ec2.describe_instances(InstanceIds=[ self.rasa_x_instance_id ] ) 
        logger.info(response)
        state = response['Reservations'][0]['Instances'][0]['State']['Name']
        return state
    
    def perform(self, action):

        if action == 'START':

            state = self.get_state()
            if state == 'terminated' or state == 'stopped':
                res = self.ec2.start_instances(InstanceIds = [self.rasa_x_instance_id])
                state = "starting"  

        elif action == 'STOP':
            
            state = self.get_state()
            if state == 'running':
                res = self.ec2.stop_instances(InstanceIds = [self.rasa_x_instance_id], Hibernate=True)
                state = 'stopped'
        
        elif action == 'STATUS':
            state = self.get_state()
        
        else:
            state = 'invalid'

        data = {
            'state':state
        }

        return data
    