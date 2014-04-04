"""
   Just starting out with tests for now.
"""

import pandas

from waterfall import Waterfall


def testWaterfall():
    df = pandas.ExcelFile('test.xls').parse("Sheet1")
    assert Waterfall(df, fig_size=(11, 6), xticks_fontsize=9, outfile="temp.png") == 'OK'



