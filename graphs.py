"""
Name: graphs.py
Author: Wesley Lee
Assignment: Visualization Project
Date: 11-02-2017
"""

#!/usr/bin/python
import plotly.plotly as py
import plotly.graph_objs as go

def pie_chart(x_axis, y_axis):
	trace = go.Pie(labels = x_axis, values = y_axis)
	py.plot([trace], filename ='basic_pie_chart')

def bar_chart(x_axis, y_axis):
	data = [go.Bar(x = x_axis, y = y_axis)]
	py.plot(data, filename ='basic_bar_chart')
	
def bubble_chart(x_axis, y_axis):
	trace0 = go.Scatter(
		x = x_axis,
		y = y_axis,
		mode = 'markers',
		marker = dict(
			size = [40, 60, 80, 100],
		)
	)

	data = [trace0]
	py.plot(data, filename = 'basic_bubble_chart')
	
def scatter_plot(x_axis, y_axis):
	trace = go.Scattergl(
		x = x_axis,
		y = y_axis,
		mode = 'markers',
		marker = dict(
			color = '#FFBAD2',
			line = dict(width = 1)
		)
	)
	data = [trace]
	py.plot(data, filename = 'basic_scatter_plot')
	
def simple_line_plot(x_axis, y_axis):
	trace = go.Scatter(
		x = x_axis,
		y = y_axis
	)

	data = [trace]

	py.plot(data, filename = 'simple_line_plot')
