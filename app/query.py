from datetime import date
from math import dist
from sqlite3 import Date
from urllib import response
from xxlimited import new
import boto3


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

def TempVsTime():
     # #Duumy data code
     dummyData=(
          {'temperature': '25', 'timestamp': '2022-10-16 16:15:22.744720'}, 
          {'temperature': '24', 'timestamp': '2022-10-16 16:15:30.282364'},
          {'temperature': '32', 'timestamp': '2022-10-15 16:14:08.760409'},
          {'temperature': '27', 'timestamp': '2022-10-15 16:15:50.463591'},
          {'temperature': '25', 'timestamp': '2022-10-15 16:14:01.225144'},
          {'temperature': '22', 'timestamp': '2022-10-15 16:16:15.598491'}, 
          {'temperature': '24', 'timestamp': '2022-10-14 16:12:17.716659'}, 
          {'temperature': '25', 'timestamp': '2022-10-14 16:15:05.082236'}, 
          {'temperature': '38', 'timestamp': '2022-10-13 16:12:52.971539'}, 
          {'temperature': '12', 'timestamp': '2022-10-13 16:15:57.999128'}, 
          {'temperature': '34', 'timestamp': '2022-10-13 16:14:16.296072'}, 
          {'temperature': '43', 'timestamp': '2022-10-12 16:13:43.570479'}, 
          {'temperature': '21', 'timestamp': '2022-10-12 16:13:10.571249'}, 
          {'temperature': '32', 'timestamp': '2022-10-12 16:12:42.907813'}, 
          {'temperature': '29', 'timestamp': '2022-10-12 16:12:35.370878'}, 
          {'temperature': '21', 'timestamp': '2022-10-11 16:13:03.039860'}, 
          {'temperature': '26', 'timestamp': '2022-10-11 16:13:36.038626'}, 
          {'temperature': '22', 'timestamp': '2022-10-11 16:13:18.107354'},
          {'temperature': '25', 'timestamp': '2022-10-10 16:16:35.726886'}, 
          {'temperature': '26', 'timestamp': '2022-10-10 16:14:55.019459'}, 
          {'temperature': '28', 'timestamp': '2022-10-10 16:16:28.191047'},
          {'temperature': '27', 'timestamp': '2022-10-9 16:16:05.534794'}, 
          {'temperature': '26', 'timestamp': '2022-10-9 16:14:42.425235'},
          {'temperature': '25', 'timestamp': '2022-10-9 16:14:34.890473'}
     )


     distinctDates=set()
     for i in dummyData:
          if len(distinctDates) >= 10: break
          else:
               distinctDates.add(i['timestamp'].split(' ')[0])
               
     newData=[]
     for date in distinctDates:
          dict={'date':date, 'readings':{'temp':[]}}
          for data in dummyData:
               date2 = data['timestamp'].split(' ')[0]
               if date2 == date:
                    dict['readings']['temp'].append(data['temperature'])
          newData.append(dict)

     temp = []

     for data in newData:
          temp.append( 
               max(data['readings']['temp']) 
          )
     
     TempVsTime=dict()
     