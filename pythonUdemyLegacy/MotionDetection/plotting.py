from tracemalloc import start
from turtle import right
from folium import Tooltip
from numpy import source
import pandas
from motion_detection import df 
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

df["Start_string"] = pandas.to_datetime(df["Start"]).dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"] = pandas.to_datetime(df["End"]).dt.strftime("%Y-%m-%d %H:%M:%S")

cds = ColumnDataSource(df)

p = figure(x_axis_type='datetime', height=100, width=500, sizing_mode = "scale_width", title="Motion Graph")
p.yaxis.minor_tick_line_color=None
p.yaxis.ticker.desired_num_ticks=1

hover = HoverTool(tooltips=[("Start: ", "@Start_string"),("End: ", "@End_string")])
p.add_tools(hover)

q = p.quad(left="Start", right="End", bottom=0, top=1, color="Blue", source=cds)

output_file("Graph.html")
show(p)