from datetime import date
from math import dist
from sqlite3 import Date
from urllib import response
import boto3

client=boto3.client('dynamodb',region_name="eu-central-1")
db=boto3.resource('dynamodb', region_name="eu-central-1")
table=db.Table('LightTable').scan()


def Details():
     return table['Items'][0]

def CountPersons():
     '''Real dataset code
dates=set()
for i in table['Items']:
     dates.add(i['TimeStamp'].split(' ')[0])
     print(f"{i},")
'''
     # #Duumy data code
     dummyData=({'payload': {'Temperature': '25', 'Person count': '0', 'TimeStamp': '2022-10-11 16:15:22.744720'}, 'TimeStamp': '2022-10-11 16:15:22.744720'},
     {'payload': {'Temperature': '24', 'Person count': '1', 'TimeStamp': '2022-10-11 16:15:30.282364'}, 'TimeStamp': '2022-10-11 16:15:30.282364'},
     {'payload': {'Temperature': '24', 'Person count': '2', 'TimeStamp': '2022-10-11 16:14:08.760409'}, 'TimeStamp': '2022-10-11 16:14:08.760409'},
     {'payload': {'Temperature': '25', 'Person count': '3', 'TimeStamp': '2022-10-11 16:15:50.463591'}, 'TimeStamp': '2022-10-11 16:15:50.463591'},
     {'payload': {'Temperature': '25', 'Person count': '0', 'TimeStamp': '2022-10-10 16:14:01.225144'}, 'TimeStamp': '2022-10-10 16:14:01.225144'},
     {'payload': {'Temperature': '25', 'Person count': '1', 'TimeStamp': '2022-10-10 16:16:15.598491'}, 'TimeStamp': '2022-10-10 16:16:15.598491'},
     {'payload': {'Temperature': '24', 'Person count': '2', 'TimeStamp': '2022-10-10 16:12:17.716659'}, 'TimeStamp': '2022-10-10 16:12:17.716659'},
     {'payload': {'Temperature': '25', 'Person count': '3', 'TimeStamp': '2022-10-10 16:15:05.082236'}, 'TimeStamp': '2022-10-10 16:15:05.082236'},
     {'payload': {'Temperature': '25', 'Person count': '4', 'TimeStamp': '2022-10-10 16:12:52.971539'}, 'TimeStamp': '2022-10-10 16:12:52.971539'},
     {'payload': {'Temperature': '25', 'Person count': '3', 'TimeStamp': '2022-10-10 16:15:57.999128'}, 'TimeStamp': '2022-10-10 16:15:57.999128'},
     {'payload': {'Temperature': '24', 'Person count': '2', 'TimeStamp': '2022-10-10 16:14:16.296072'}, 'TimeStamp': '2022-10-10 16:14:16.296072'},
     {'payload': {'Temperature': '25', 'Person count': '1', 'TimeStamp': '2022-10-10 16:13:43.570479'}, 'TimeStamp': '2022-10-10 16:13:43.570479'},
     {'payload': {'Temperature': '25', 'Person count': '0', 'TimeStamp': '2022-10-10 16:13:10.571249'}, 'TimeStamp': '2022-10-10 16:13:10.571249'},
     {'payload': {'Temperature': '25', 'Person count': '1', 'TimeStamp': '2022-10-10 16:12:42.907813'}, 'TimeStamp': '2022-10-10 16:12:42.907813'},
     {'payload': {'Temperature': '25', 'Person count': '2', 'TimeStamp': '2022-10-10 16:12:35.370878'}, 'TimeStamp': '2022-10-10 16:12:35.370878'},
     {'payload': {'Temperature': '24', 'Person count': '3', 'TimeStamp': '2022-10-10 16:13:03.039860'}, 'TimeStamp': '2022-10-10 16:13:03.039860'},
     {'payload': {'Temperature': '25', 'Person count': '2', 'TimeStamp': '2022-10-10 16:13:36.038626'}, 'TimeStamp': '2022-10-10 16:13:36.038626'},
     {'payload': {'Temperature': '25', 'Person count': '1', 'TimeStamp': '2022-10-10 16:13:18.107354'}, 'TimeStamp': '2022-10-10 16:13:18.107354'},
     {'payload': {'Temperature': '25', 'Person count': '2', 'TimeStamp': '2022-10-10 16:16:35.726886'}, 'TimeStamp': '2022-10-10 16:16:35.726886'},
     {'payload': {'Temperature': '25', 'Person count': '3', 'TimeStamp': '2022-10-10 16:14:55.019459'}, 'TimeStamp': '2022-10-10 16:14:55.019459'},
     {'payload': {'Temperature': '25', 'Person count': '4', 'TimeStamp': '2022-10-10 16:16:28.191047'}, 'TimeStamp': '2022-10-10 16:16:28.191047'},
     {'payload': {'Temperature': '25', 'Person count': '5', 'TimeStamp': '2022-10-10 16:16:05.534794'}, 'TimeStamp': '2022-10-10 16:16:05.534794'},
     {'payload': {'Temperature': '25', 'Person count': '4', 'TimeStamp': '2022-10-10 16:14:42.425235'}, 'TimeStamp': '2022-10-10 16:14:42.425235'},
     {'payload': {'Temperature': '25', 'Person count': '5', 'TimeStamp': '2022-10-10 16:14:34.890473'}, 'TimeStamp': '2022-10-10 16:14:34.890473'})


     distinctDates=set()
     for i in dummyData:
          distinctDates.add(i['TimeStamp'].split(' ')[0])

     DateData=dict()
     
     for i in distinctDates:
          DateData[i]=[]

     for i in dummyData:
          tmp=[]
          tmp.append(i['TimeStamp'].split(' ')[1])
          tmp.append(i['payload']['Person count'])
          lst=DateData.get(i['TimeStamp'].split(' ')[0])
          lst.append(tmp)
          DateData[i['TimeStamp'].split(' ')[0]]=lst

     for i in DateData:
          lst=DateData[i]
          lst=sorted(lst,key=lambda x: x[0])
          DateData[i]=lst

     PersonCount=dict()
     for i in DateData:
          prev=DateData[i][0]
          cnt=0
          if prev!=0:
               cnt=1
          for idx in range(1,len(DateData[i])):
               if DateData[i][idx][1]>DateData[i][idx-1][1]:
                    cnt=cnt+1     
          PersonCount[i]=cnt           
     return PersonCount     
