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

unique_regions = set(df['region_txt'].unique())

numlines = len(unique_regions)
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

output_file("region.html")
p = figure()

i = 0
for region in unique_regions:
    # number of attacks by year for each region
    region_attacks = df[df['region_txt'] == region]['iyear'].value_counts()
    region_attacks = region_attacks.sort_index()
    color = mypalette[i]
    p.line(region_attacks.index, region_attacks, line_color=color, legend=region, line_width=2)
    i = i+1

#p.add_tools(HoverTool(tooltips=[("Attacks: ", "$mpg_mean")]))
p.title = "Number of Terrorist Attacks by Region"
p.xaxis.axis_label = 'year'
p.yaxis.axis_label = 'number of terrorist attacks'
p.legend.location ="top_left"
show(p)      

    
    
    
    
    