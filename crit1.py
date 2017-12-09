# -*- coding: utf-8 -*-

import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

# read in file
p = "/Users/Bobby/anaconda/ANLY503ClassActivity/Final"
file_path = p+"/TerrorismDATA_Real_1970_2016.csv"
df = pd.read_csv(file_path, encoding = "ISO-8859-1")

crit1 = df.groupby('iyear', as_index=False)['crit1'].sum()
#count = df.groupby('iyear', as_index=False).sum()
#norm = crit1/count

data = go.Scatter(x=crit1.iyear, y=crit1.crit1,
                  mode='lines+markers',
                  name='Political/Economic/Religious/Social Goal', 
                  line=dict(color='pu', width = 2),
                  hoverinfo = 'x+y+name')
                  
layout = go.Layout(title = 'Political/Economic/Religious/Social Goal by Year')

fig = go.Figure(data=[data], layout=layout)
py.iplot(fig, filename='crit1')



