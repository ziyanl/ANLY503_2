# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from bokeh.palettes import Spectral11
from bokeh.plotting import figure, show, output_file

# read in file
p = "/Users/Bobby/anaconda/ANLY503ClassActivity/Final"
file_path = p+"/TerrorismDATA_Real_1970_2016.csv"
df = pd.read_csv(file_path, encoding = "ISO-8859-1")

numlines=len(df.attacktype1_txt)
mypalette=Spectral11[0:numlines]

output_file('attacktype.html')

p = figure(width=500, height=300, x_axis_type="iyear") 
p.multi_line(xs=[df.index.values]*numlines,
             ys=[df[name].values for name in df],
             line_color=mypalette,
             line_width=1)
show(p)




toy_df = pd.DataFrame(data=np.random.rand(5,3), columns = ('a', 'b' ,'c'), index = pd.DatetimeIndex(start='01-01-2015',periods=5, freq='d'))   

numlines=len(toy_df.columns)
mypalette=Spectral11[0:numlines]

p = figure(width=500, height=300, x_axis_type="datetime") 
p.multi_line(xs=[toy_df.index.values]*numlines,
                ys=[toy_df[name].values for name in toy_df],
                line_color=mypalette,
                line_width=5)
show(p)





