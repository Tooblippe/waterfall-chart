# -*- coding: utf-8 -*-
"""

    Matplotlib waterfall chart proof of concept

"""
import numpy as np

from pylab import *
from pandas import *


def autolabel(rects):
    # attach some text labels
    #http://matplotlib.org/examples/api/barchart_demo.html
    for rect in rects:
        height = rect.get_height()
        text(rect.get_x() + rect.get_width() / 2., 1.05 * height, '%d' % int(height),
             ha='right', va='bottom')

#we need to turn this into an object still!
def Waterfall(values, # values to plot
              xtick_names, # x axis names
              plot_title="Waterfall", # set plot title
              plot_X="xname", # labels x axis
              plot_Y="yname", # labels y axis
              plot_line=True, # add a 'trend' line
              bar_color='#082583', # set the bar color
              neg_color='red', # color of a negative bar
              plc="g--", # plot line style and color
              plwidth=2, # plot width
              fig_size=(15.5, 9), # figure size
              tfont_size=25, # font size
              axfont_size=20, # axis font size
              bar_width=0.5, # width of the bar
              xticks_fontsize=15, # fontsize of axis names
              grid_val=True, # use grid
              xkcd=False, # use xkcd type plot
              toplabel=True, # add top label
              outfile='temp.png'):          # filename to write the plot to
    if xkcd:
        plt.xkcd()


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
    rcParams['figure.figsize'] = fig_size

    sumvalues = np.cumsum(values)
    blanks = [0 for i in range(len(sumvalues))]

    neg_h = [0 for i in range(len(sumvalues))]
    negblanks = [0 for i in range(len(sumvalues))]
    for i in range(len(sumvalues)):
        if values[i] > 0:
            blanks[i] = sumvalues[i] - values[i]
        if values[i] < 0:
            sumvalues[i] = sumvalues[i - 1]
            blanks[i] = sumvalues[i] + values[i]
            neg_h[i] = sumvalues[i]
            negblanks[i] = blanks[i]

    xpos = [bar_width * x for x in range(len(values))]

    title(plot_title, fontsize=tfont_size)
    xlabel(plot_X, fontsize=axfont_size)
    ylabel(plot_Y, fontsize=axfont_size)

    rects1 = bar(xpos, sumvalues, align='center', width=bar_width, color=bar_color)

    bar(xpos, blanks, color='#eeeeee', edgecolor='#eeeeee', align='center', width=bar_width)
    bar(xpos, neg_h, align='center', width=bar_width, color=neg_color)
    bar(xpos, negblanks, color='#eeeeee', edgecolor='#eeeeee', align='center', width=bar_width)

    xticks(xpos, xtick_names, fontsize=xticks_fontsize)

    if plot_line:
        plot(xpos, sumvalues, plc, linewidth=plwidth)

    grid(grid_val)

    if toplabel:
        autolabel(rects1)

    if outfile:
        savefig(outfile, dpi=200, bbox_inces="Tight")

    show()
    return "OK"


def demo(exampleFile=''):
    if not exampleFile:
        exampleFile = 'test.xls'

    try:
        df = pandas.ExcelFile(exampleFile).parse("Sheet1")
        values = df['Rbn']
        xtick_names = df['Values']
        Waterfall(values, xtick_names, fig_size=(11, 6), xticks_fontsize=9, outfile="temp.png")
    except:
        print "Error, please check if the example file is in the path"


if __name__ == "__main__":
    demo('test.xls')