# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 21:25:24 2013

@author: tobie
"""
import numpy as np
from pylab import *
from matplotlib import rc_params
from pandas import *



def Waterfall( df, xkcd=False, outfile = 'temp.png'):
    if xkcd: 
        plt.xkcd()
        
    values = df.Rbn
    xtick_names = df.Values
    
    plot_title = 'Divisional Stuff'
    plot_X = "DX Stuff"
    plot_Y = "Rands (Bn)"
    plot_line = True
    
    bar_color = '#082583'
    neg_color = '#705F49'
    
    
    plc = "g--"
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
    
    rcParams.update(s)
    rcParams['figure.figsize'] = 15.5, 9
    
    sumvalues = np.cumsum(values)
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
    
    bar(xpos,neg_h,align='center',width=bwidth,color=neg_color)
    bar(xpos,negblanks,color='#eeeeee',edgecolor='#eeeeee',align='center',width=bwidth)
    
    if plot_line : plot(xpos,sumvalues, plc, linewidth=plwidth)
    
    xticks(xpos,xtick_names,fontsize=15)
    savefig(outfile,dpi=200,bbox_inces="Tight")
    show()
    


df = pandas.ExcelFile('../Downloads/test.xls').parse("Sheet1")
Waterfall( df )