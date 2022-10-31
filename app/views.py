import imp
import re
from django.shortcuts import render
from .query import *
import pandas as pd
import plotly.express as px



def home(request):
    #data=query()
    data={'Gas LPG': 34324,'Humidity': 32234, 'CO VAL':32,'SMOKE': 2334, 'temperature':43, 'timestamp':2022-10-20}
    t1=data['Gas LPG']
    t2=data['Humidity']
    t3=data['CO VAL']
    t4=data['SMOKE']
    t5=data['temperature']
    t6=data['timestamp']

    tempVsTime = tempVsTimeGraph()
    smokeVsTime = smokeVsTimeGraph()

    context={
        't1':t1,
        't2':t2,
        't3':t3,
        't4':t4,
        't5':t5,
        't6':t6,
        'tempVsTime':tempVsTime,
        'smokeVsTime':smokeVsTime
    }
    return render(request,'home.html',context)


def tempVsTimeGraph():
    data = TempVsTime()
    data=  pd.DataFrame(data, columns=['Date', 'Temp'])
    fig = px.bar(data,x='Date', y='Temp')
    fig.update_yaxes(rangemode="tozero")
    return fig.to_html()

def smokeVsTimeGraph():
    data = SmokeVsTime()
    data=  pd.DataFrame(data, columns=['Date', 'Smoke'])
    fig = px.bar(data,x='Date', y='Smoke')
    return fig.to_html()