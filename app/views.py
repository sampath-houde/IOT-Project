import imp
import re
from django.shortcuts import render
from .query import *
import pandas as pd
import plotly.express as px



def home(request):
    data=query()
    t1=data['Gas LPG']
    t2=data['Humidity']
    t3=data['CO VAL']
    t4=data['SMOKE']
    t5=data['temperature']
    t6=data['timestamp']

    graph = Plotgraph()

    context={
        't1':t1,
        't2':t2,
        't3':t3,
        't4':t4,
        't5':t5,
        't6':t6
        # 'graph':graph
    }
    return render(request,'home.html',context)


def Plotgraph():
    data = TempVsTime()
#     data=TempVsTime()
#     data=  pd.DataFrame(data.items(), columns=['Date', 'Temp'])
#     fig = px.bar(data,x='Date', y='Temp')
#     return fig.to_html()