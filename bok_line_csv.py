#Making a basic Bokeh line graph
    
#importing Bokeh
from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas
    
#read data into a dataframe with pandas
#df = pandas.read_csv("bachelors.csv")
df=pandas.read_csv("http://pythonhow.com/data/bachelors.csv")
"""
x=[3,7.5,10]
y=[3,6,9]
"""
x = df['Year']
y = df['Engineering']    
#prepare the output file
output_file("Bachelors_degree.html")
    
#create a figure object
f=figure()
    
#create line plot
f.line(x,y)
#f.circle(x,y)    

#write the plot in the figure object
show(f)