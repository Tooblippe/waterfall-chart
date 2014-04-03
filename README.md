# waterfall.py

Simple function that implements a waterfall chart in python. I have not  been able to find any decent implementation of a waterfall chart online and implementing it in Excel is neither trivial nor pretty. 

#usage

This implementation is still very basic as I needed it fairly quickly

It reads an Excel file into a pandas dataframe. YOu can obviously hard code your data.The file format currently is very simple. Some of the axis names and chart heading is still hard coded.

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
df = pandas.ExcelFile('test.xls').parse("Sheet1")
Waterfall( df )
```

![waterfall](https://raw.github.com/Tooblippe/waterfall/master/temp.png)

# custom matplotlib
The function makes small modifications to the Matplotlib config file and also sets the default size to someting that should be easy to copy and paste to powerpoint.



```
