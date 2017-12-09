# -*- coding: utf-8 -*-

import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

# read in file
p = "/Users/Bobby/anaconda/ANLY503ClassActivity/Final"
file_path = p+"/TerrorismDATA_Real_1970_2016.csv"
df = pd.read_csv(file_path, encoding = "ISO-8859-1")

success = df.groupby('iyear', as_index=False)['success'].sum()

data = go.Scatter(x=success.iyear, y=success.success,
                  mode='lines+markers', name='Success', 
                  line=dict(color='red', width=2),
                  hoverinfo='x+y+name')

layout = go.Layout(title = 'Number of Successful Terrorist Attacks by Year')

fig = go.Figure(data=[data], layout=layout)
py.iplot(fig, filename='success_by_year')



