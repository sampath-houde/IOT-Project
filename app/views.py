import imp
from django.shortcuts import render
from .query import *
from chart_studio import plotly
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd



def Plotgraph():
    data=CountPersons()
    data=  pd.DataFrame(data.items(), columns=['Date', 'Count'])
    fig = px.bar(data,x='Date', y='Count')
    return fig.to_html()



def home(request):
    graph=Plotgraph()
    data=Details()
    tmp=data['payload']['Temperature']
    person=data['payload']['Person count']
    light="off"
    if person!=0:
        light="onn"

    context={
        'graph':graph,
        'tmp':tmp,
        'person':person,
        'light':light
    }
    return render(request,'home.html',context)