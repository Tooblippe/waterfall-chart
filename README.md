# waterfall.py

[![Build Status](https://travis-ci.org/Tooblippe/waterfall.svg?branch=master)](https://travis-ci.org/Tooblippe/waterfall)

--------------

Simple function that implements a waterfall chart in python.
I have not  been able to find any decent implementation of a waterfall chart online and implementing it in Excel is neither trivial nor pretty.

#usage

This implementation is still very basic as I needed it fairly quickly

An exmaple Excel file is provided here (test.xls) and the demo reads an Excel file into a pandas DataFrame and passes the values and xtick names to the drawing function.

Item  | Value
-----  |  ------
Tomatos  | 50
Potatos | 30
Gas | 90
Correction | -10
Unplanned | 9
Stuff | 20
Other Stuff | 20
Foo | 10

Edit the following lines to point to an Excel file with the data. The waterfall() function is called with the parsed Excel file pandas dataframe.

```
    import pandas
    import waterfall

    df = pandas.ExcelFile('test.xls').parse("Sheet1")
    values = df['Rbn']
    xtick_names = df['Values']
    Waterfall( values, xtick_names, fig_size = ( 11, 6 ), xticks_fontsize = 9, outfile = "temp.png")
```
or just run demo.py

```
    import waterfall
    waterfall.demo('test.xls')
```


![waterfall](https://raw.github.com/Tooblippe/waterfall/master/temp.png)

# custom matplotlib
The function makes small modifications to the Matplotlib config file and also sets the default size to someting that should be easy to copy and paste to powerpoint.

