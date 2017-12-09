# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from bokeh.palettes import Spectral11
from bokeh.plotting import output_file, show, figure
from bokeh.models import ColumnDataSource, HoverTool

# read in file
p = "/Users/Bobby/anaconda/ANLY503ClassActivity/Final"
file_path = p+"/TerrorismDATA_Real_1970_2016.csv"
df = pd.read_csv(file_path, encoding = "ISO-8859-1")

unique_attacktypes = set(df['attacktype1_txt'].unique())

numlines = len(unique_attacktypes)
mypalette = [ "#99d594", 
              "#ffffbf", 
              '#5e4fa2', 
              '#3288bd', 
              '#66c2a5', 
              '#abdda4',
              '#e6f598',
              '#ffffbf',
              '#fee08b',
              '#fdae61',
              '#f46d43',
              '#d53e4f',
              '#9e0142']

output_file("attacktype1.html")
p = figure()

i = 0
for attacktype in unique_attacktypes:
    # number of attacks by year for each region
    n = df[df['attacktype1_txt'] == attacktype]['iyear'].value_counts()
    n = n.sort_index()
    color = mypalette[i]
    p.line(n.index, n, line_color=color, legend=attacktype, line_width=2)
    i = i+1

#p.add_tools(HoverTool(tooltips=[("Attacks: ", "$mpg_mean")]))
p.title = "Number of Terrorist Attacks by Primary Attack Type"
p.xaxis.axis_label = 'year'
p.yaxis.axis_label = 'number of terrorist attacks'
p.legend.location ="top_left"
show(p)      

    
    
    
    
    