"""
   Just starting out with tests for now. !
"""

import pandas

from waterfall import Waterfall

def testWaterfall():
    df = pandas.ExcelFile('test.xls').parse("Sheet1")
    values = df['Rbn']
    xtick_names = df['Values']
    assert Waterfall(values, xtick_names, fig_size=(11, 6), xticks_fontsize=9, outfile="temp.png") == 'OK'






