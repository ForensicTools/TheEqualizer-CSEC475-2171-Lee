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
	trace = go.Scatter(
		x = x_axis,
		y = y_axis,
		mode = 'markers',
		marker = dict(
			size = [40, 60, 80, 100],
		)
	)

	data = [trace]
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

def stacked_bar_chart(x_axis, y_axis1, y_axis2, y_axis3, y_axis4):
	trace1 = go.Bar(
		x = x_axis,
		y = y_axis1,
		name = 'Critical',
			marker = dict(
				color = 'rgb(196, 10, 10)',
			)
	)
	
	trace2 = go.Bar(
		x = x_axis,
		y = y_axis2,
		name = 'High',
			marker = dict(
				color = 'rgb(224, 151, 4)',
			)
	)
	
	trace3 = go.Bar(
			x = x_axis,
			y = y_axis3,
			name = 'Medium',
				marker = dict(
					color = 'rgb(237, 187, 7)',
				)
		)

	trace4 = go.Bar(
			x = x_axis,
			y = y_axis4,
			name = 'Low',
				marker = dict(
					color = 'rgb(15, 183, 3)',
				)
		)
		
		
	data = [trace1, trace2, trace3, trace4]
	layout = go.Layout(
		barmode='stack',
	)

	fig = go.Figure(data = data, layout = layout)
	py.plot(fig, filename = 'Vulnerabilitiy_Stacked_Bar_Chart')
	
	
def basic_area_chart(x_axis, y_axis1, y_axis2, y_axis3, y_axis4):
	trace1 = go.Scatter(
		x = x_axis,
		y = y_axis1,
		fill = 'tozeroy',
		name = 'Critical',
			marker = dict(
				color = 'rgb(196, 10, 10)',
			)
	)
	
	trace2 = go.Scatter(
		x = x_axis,
		y = y_axis2,
		fill = 'tonexty',
		name = 'High',
			marker = dict(
				color = 'rgb(224, 151, 4)',
			)
	)
	
	trace3 = go.Scatter(
			x = x_axis,
			y = y_axis3,
			fill = 'tozeroy',
			name = 'Medium',
				marker = dict(
					color = 'rgb(237, 187, 7)',
				)
		)
	
	trace4 = go.Scatter(
			x = x_axis,
			y = y_axis4,
			fill = 'tonexty',
			name = 'Low',
				marker = dict(
					color = 'rgb(15, 183, 3)',
				)
		)
		
	data = [trace1, trace2, trace3, trace4]
	py.plot(data, filename = 'basic_area_chart')