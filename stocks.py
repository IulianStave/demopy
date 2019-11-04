from pandas_datareader import data
from bokeh.plotting import figure, show, output_file
from bokeh.models.annotations import Title
from datetime import datetime as dt

def inc_dec(open, close):
    if open < close:
        return 'Increase'
    elif open > close:
        return 'Decrease'
    else:
        return 'Equal'
#start_date = dt(2019,10,1)
#end_date = dt(2019,10,10) 

start_date = dt(2016,3,1)
end_date = dt(2016,3,10) 

hours_12_in_ms = 12*60*60*1000

df = data.DataReader(name = "GOOG", data_source = "yahoo", start = start_date, end = end_date)
#print(df)
# 12 hours width, 12 hours gap, 
chart  = figure(x_axis_type = 'datetime', width = 1000, height = 300)
chart.title.text = "Chart stocks"
#print(df.index) 
df["Status"] = [inc_dec(open, close) for open, close in zip(df.Open, df.Close)]
df["Middle"] = (df.Open + df.Close)/2
df["Height"] = abs(df.Close - df.Open)

chart.rect(df.index[df.Status == 'Increase'], df.Middle[df.Status == 'Increase'], hours_12_in_ms, df.Height[df.Status == 'Increase'], fill_color = "green", line_color = "black")

chart.rect(df.index[df.Status == 'Decrease'], df.Middle[df.Status == 'Decrease'], hours_12_in_ms, df.Height[df.Status == 'Decrease'], fill_color = "red")


output_file('stocks.html')
show(chart)