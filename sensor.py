#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
import datetime
import random
import testdata
import boto3

boto_session = boto3.Session(aws_access_key_id='AKIA5NKG5NAPJMAZFENN',aws_secret_access_key='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')

client = boto_session.client(service_name='firehose',region_name='us-west-2')

def getData(iotName, lowVal, highVal):
   data = {}
   data["iotName"] = iotName
   data["iotValue"] = random.randint(lowVal, highVal)
   return data

while 1:
   rnd = random.random()
   if (rnd < 0.01):
      response = client.put_record(
           DeliveryStreamName='sourcestream',
           Record={
                'Data': json.dumps(getData("SensorRecord", 100, 120))
            }
        )

   else:
      response = client.put_record(
           DeliveryStreamName='sourcestream',
           Record={
                'Data': json.dumps(getData("SensorRecord", 10, 20))
            }
        )

