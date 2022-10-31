from collections import defaultdict
from datetime import date
from math import dist
from multiprocessing import dummy
from sqlite3 import Date
from time import time
from types import new_class
from urllib import response
from xxlimited import new
import boto3
from cv2 import sort


def query():
     client=boto3.client('dynamodb',region_name="ap-south-1")
     db=boto3.resource('dynamodb', region_name="ap-south-1")
     table=db.Table('iot_table_3').scan()
     table=table['Items']
     
     ans=table[0]['payload']
     
     for i in table:
          if i['payload']['timestamp']>ans['timestamp']:
               ans=i['payload']
     return ans

def fetch_data():
     client=boto3.client('dynamodb',region_name="ap-south-1")
     db=boto3.resource('dynamodb', region_name="ap-south-1")
     table=db.Table('iot_table_3').scan()
     table=table['Items']
     dummyData=[]
     for item in table:
          if 'temperature'in item['payload'] and 'SMOKE' in item['payload']:
               dictSampath={
                    'temp':item['payload']['temperature'],
                    'smoke':item['payload']['SMOKE'],
                    'timestamp':item['payload']['timestamp']
               }
               dummyData.append(dictSampath)
     return dummyData

def TempVsTime():
     # #Duumy data code
     #dynamoDBData = fetch_data()
     dynamoDBData = [{'temp': '25', 'timestamp': '2022-10-16 16:15:22.744720'}, 
          {'temp': '24', 'timestamp': '2022-10-16 16:15:30.282364'},
          {'temp': '32', 'timestamp': '2022-10-15 16:14:08.760409'},
          {'temp': '27', 'timestamp': '2022-10-15 16:15:50.463591'},
          {'temp': '25', 'timestamp': '2022-10-15 16:14:01.225144'},
          {'temp': '22', 'timestamp': '2022-10-15 16:16:15.598491'}, 
          {'temp': '24', 'timestamp': '2022-10-14 16:12:17.716659'}, 
          {'temp': '25', 'timestamp': '2022-10-14 16:15:05.082236'}, 
          {'temp': '38', 'timestamp': '2022-10-13 16:12:52.971539'}, 
          {'temp': '12', 'timestamp': '2022-10-13 16:15:57.999128'}, 
          {'temp': '34', 'timestamp': '2022-10-13 16:14:16.296072'}, 
          {'temp': '43', 'timestamp': '2022-10-12 16:13:43.570479'}, 
          {'temp': '21', 'timestamp': '2022-10-12 16:13:10.571249'}, 
          {'temp': '32', 'timestamp': '2022-10-12 16:12:42.907813'}, 
          {'temp': '29', 'timestamp': '2022-10-12 16:12:35.370878'}, 
          {'temp': '21', 'timestamp': '2022-10-11 16:13:03.039860'}, 
          {'temp': '26', 'timestamp': '2022-10-11 16:13:36.038626'}, 
          {'temp': '22', 'timestamp': '2022-10-11 16:13:18.107354'},
          {'temp': '25', 'timestamp': '2022-10-10 16:16:35.726886'}, 
          {'temp': '26', 'timestamp': '2022-10-10 16:14:55.019459'}, 
          {'temp': '28', 'timestamp': '2022-10-10 16:16:28.191047'},
          {'temp': '27', 'timestamp': '2022-10-9 16:16:05.534794'}, 
          {'temp': '26', 'timestamp': '2022-10-9 16:14:42.425235'},
          {'temp': '25', 'timestamp': '2022-10-9 16:14:34.890473'}]

     distinctDates=set()

     for i in dynamoDBData:
          if len(distinctDates) >= 10: break
          else:
               distinctDates.add(i['timestamp'].split(' ')[0])
               
     newData=[]
     for uniqueDate in distinctDates:
          customDict={'date':uniqueDate, 'readings':{'temp':[]}}
          for data in dynamoDBData:
               date2 = data['timestamp'].split(' ')[0]
               if date2 == uniqueDate:
                    customDict['readings']['temp'].append(data['temp'])
          newData.append(customDict)

     temp = []

     for data in newData:
          temp.append( 
               max(data['readings']['temp']) 
          )
     
     newList = []
     distinctDates = list(distinctDates)
     for i in range(0,len(temp)):
          t=[]
          t.append(distinctDates[i])
          t.append(temp[i])
          newList.append(t)
     newList.sort(key=lambda x: x[1])
     return newList

def SmokeVsTime():
     # #Duumy data code
     #dynamoDBData = fetch_data()
     dynamoDBData = [{'smoke': '0.00543', 'timestamp': '2022-10-16 16:15:22.744720'}, 
          {'smoke': '0.00533', 'timestamp': '2022-10-16 16:15:30.282364'},
          {'smoke': '0.00447', 'timestamp': '2022-10-15 16:14:08.760409'},
          {'smoke': '0.00523', 'timestamp': '2022-10-15 16:15:50.463591'},
          {'smoke': '0.00245', 'timestamp': '2022-10-15 16:14:01.225144'},
          {'smoke': '0.00649', 'timestamp': '2022-10-15 16:16:15.598491'}, 
          {'smoke': '0.00948', 'timestamp': '2022-10-14 16:12:17.716659'}, 
          {'smoke': '0.00146', 'timestamp': '2022-10-14 16:15:05.082236'}, 
          {'smoke': '0.00473', 'timestamp': '2022-10-13 16:12:52.971539'}, 
          {'smoke': '0.00442', 'timestamp': '2022-10-13 16:15:57.999128'}, 
          {'smoke': '0.00543', 'timestamp': '2022-10-13 16:14:16.296072'}, 
          {'smoke': '0.00533', 'timestamp': '2022-10-12 16:13:43.570479'}, 
          {'smoke': '0.00243', 'timestamp': '2022-10-12 16:13:10.571249'}, 
          {'smoke': '0.00643', 'timestamp': '2022-10-12 16:12:42.907813'}, 
          {'smoke': '0.00443', 'timestamp': '2022-10-12 16:12:35.370878'}, 
          {'smoke': '0.00443', 'timestamp': '2022-10-11 16:13:03.039860'}, 
          {'smoke': '0.00833', 'timestamp': '2022-10-11 16:13:36.038626'}, 
          {'smoke': '0.00423', 'timestamp': '2022-10-11 16:13:18.107354'},
          {'smoke': '0.00523', 'timestamp': '2022-10-10 16:16:35.726886'}, 
          {'smoke': '0.00513', 'timestamp': '2022-10-10 16:14:55.019459'}, 
          {'smoke': '0.00943', 'timestamp': '2022-10-10 16:16:28.191047'},
          {'smoke': '0.00744', 'timestamp': '2022-10-9 16:16:05.534794'}, 
          {'smoke': '0.00741', 'timestamp': '2022-10-9 16:14:42.425235'},
          {'smoke': '0.00399', 'timestamp': '2022-10-9 16:14:34.890473'}]

     distinctDates=set()
     for i in dynamoDBData:
          if len(distinctDates) >= 10: break
          else:
               distinctDates.add(i['timestamp'].split(' ')[0])
               
     newData=[]
     for uniqueDate in distinctDates:
          customDict={'date':uniqueDate, 'readings':{'smoke':[]}}
          for data in dynamoDBData:
               date2 = data['timestamp'].split(' ')[0]
               if date2 == uniqueDate:
                    customDict['readings']['smoke'].append(data['smoke'])
          newData.append(customDict)
     smoke = []

     for data in newData:
          smoke.append( 
               max(data['readings']['smoke']) 
          )
     newList = []
     distinctDates = list(distinctDates)
     for i in range(1,len(smoke)):
          t=[]
          t.append(distinctDates[i])
          t.append(smoke[i])
          newList.append(t)
     newList.sort(key=lambda x: x[1])
     print(newList)
     return newList




     



     