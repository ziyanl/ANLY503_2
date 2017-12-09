# -*- coding: utf-8 -*-

import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

# read in file
p = "/Users/Bobby/anaconda/ANLY503ClassActivity/Final"
file_path = p+"/TerrorismDATA_Real_1970_2016.csv"
df = pd.read_csv(file_path, encoding = "ISO-8859-1")

pivot = pd.crosstab(df.iyear, df.weaptype1_txt)

colorscale = [[0,'#deebf7'],[1, '#084594']]

score = []
for x in pivot.apply(tuple):
  score.extend(x)

data = [
    go.Heatmap(
        z=score,
        x=list(pivot.index) * len(pivot.columns),
        y=[item for item in list(pivot.columns) for i in range(len(pivot.index))],
        colorscale=colorscale,
    )
]

layout = go.Layout(
    title='Number of Terrorist Attacks by Weapon Type',
    xaxis = dict(ticks='', nticks=36),
    yaxis = dict(ticks='')
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='attacks_by_weapon')






