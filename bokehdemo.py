from bokeh.plotting import figure
from bokeh.io import output_file, show

x = [1,2,3,4,5]
y = [6,7,8,9,10]

f = figure()
#f.circle(x,y)
f.triangle(x,y,4)
show(f)