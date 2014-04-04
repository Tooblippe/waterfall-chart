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
def Waterfall(values,
              xtick_names,
              plot_title="Waterfall",
              plot_X="xname",
              plot_Y="yname",
              plot_line=True,
              bar_color='#082583',
              neg_color='red',
              plc="g--",
              plwidth=2,
              fig_size=(15.5, 9),
              tfont_size=25,
              axfont_size=20,
              bar_width=0.5,
              xticks_fontsize=15,
              grid_val=True,
              xkcd=False,
              toplabel=True,
              outfile='temp.png'):
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


if __name__ == "__main__":
    df = pandas.ExcelFile('test.xls').parse("Sheet1")
    values = df['Rbn']
    xtick_names = df['Values']
    Waterfall(values, xtick_names, fig_size=(11, 6), xticks_fontsize=9, outfile="temp.png")