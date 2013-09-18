# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 21:25:24 2013

@author: tobie
"""
import numpy as np
from pylab import *
from matplotlib import *

values = np.array([5, 50, 10, -3,30, 10, -21, 10,5, 50, 10, -3,30, 10, -21, 10])
xtick_names = ['Tobie','Sandra','Mike','Danie','Tobie','Sandra','Mike','Danie','Tobie','Sandra','Mike','Danie','Tobie','Sandra','Mike','Danie']
plot_title = 'Divisional Stuff'
plot_X = "DX Stuff"
plot_Y = "Rands (Bn)"
plot_line = True
#figsize(16/3.0,9/3.0)


bar_color = "green"
outfilename = "test11."
filetype = "png"
outfile = outfilename+filetype


plc = "b--"
plwidth = 3
#Some standard stuff. Also see last cell for custom css
import json
s = json.loads('''
{
  "lines.linewidth": 2.0,
  "examples.download": true,
  "axes.edgecolor": "#bcbcbc",
  "patch.linewidth": 0.5,
  "legend.fancybox": true,
  "axes.color_cycle": [
    "#348ABD",
    "#A60628",
    "#7A68A6",
    "#467821",
    "#CF4457",
    "#188487",
    "#E24A33"
  ],
  "axes.facecolor": "#eeeeee",
  "axes.labelsize": "large",
  "axes.grid": true,
  "patch.edgecolor": "#eeeeee",
  "axes.titlesize": "x-large",
  "svg.embed_char_paths": "path",
  "examples.directory": ""
}''')

matplotlib.rcParams.update(s)
rcParams['figure.figsize'] = 8, 4.5

sumvalues = cumsum(values)
blanks = [ 0 for i in range(len(sumvalues))]

neg_h = [ 0 for i in range(len(sumvalues)) ]
negblanks = [ 0 for i in range(len(sumvalues)) ]
for i in range(len(sumvalues)):
    if values[i]>0: 
        blanks[i] =sumvalues[i]-values[i] 
    if values[i]<0:
        sumvalues[i] = sumvalues[i-1]
        blanks[i]=sumvalues[i]+values[i]
        neg_h[i] = sumvalues[i]
        
        negblanks[i] = blanks[i]
#blanks =sumvalues -values
print "Total " , sum(values)
tfont_size = 25
axfont_size = 20
bwidth = 0.5
xpos = [bwidth*x for x in range(len(values))]
#figsize(sum(xpos), round(sum(xpos)/16.0*9.0)) 
#figsize(16,9)

title(plot_title,fontsize=tfont_size)
xlabel(plot_X,fontsize=axfont_size)
ylabel(plot_Y, fontsize=axfont_size)
bar(xpos,sumvalues,align='center',width=bwidth,color=bar_color)
bar(xpos,blanks,color='#eeeeee',edgecolor='#eeeeee',align='center',width=bwidth)

bar(xpos,neg_h,align='center',width=bwidth,color='red')
bar(xpos,negblanks,color='#eeeeee',edgecolor='#eeeeee',align='center',width=bwidth)

if plot_line : plot(xpos,sumvalues, plc, linewidth=plwidth)

xticks(xpos,xtick_names,fontsize=15)
savefig(outfile,dpi=200,bbox_inces="Tight")
show()