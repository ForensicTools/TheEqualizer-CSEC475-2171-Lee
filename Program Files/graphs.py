"""
Name: graphs.py
Author: Wesley Lee
Assignment: Visualization Project
Date Created: 11-02-2017
Last Updated: 11-23-2017

Description:
	Graphs the necessary chart when called.
"""

#!/usr/bin/python
import plotly.plotly as py
import plotly.graph_objs as go

# Function that displays a basic pie chart
def pie_chart(x_axis, y_axis):
	trace = go.Pie(labels = x_axis, values = y_axis)
	py.plot([trace], filename ='basic_pie_chart')

# Function that displays a basic bar chart
def bar_chart(x_axis, y_axis):
	data = [go.Bar(x = x_axis, y = y_axis)]
	py.plot(data, filename ='basic_bar_chart')

# Function that displays a bubble chart
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

# Function that displays a scatter plot chart	
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

# Function that displays a simple line plot	
def simple_line_plot(x_axis, y_axis):
	trace = go.Scatter(
		x = x_axis,
		y = y_axis
	)

	data = [trace]

	py.plot(data, filename = 'simple_line_plot')

# Function that displays a stacked bar chart 
# Only for the vulnerabilities (Info vulnerability no included)
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
	
# Function that displays a stacked area chart 
# Only for the vulnerabilities (Info vulnerability no included)	
def stacked_area_chart(x_axis, y_axis1, y_axis2, y_axis3, y_axis4):
	Crititcal = go.Scatter(
			x = x_axis,
			y = y_axis1,
			mode = 'lines',
			name = 'Critical',
				line = dict(width=0.5,
									color = 'rgb(196, 10, 10)'),
			fill = 'tonexty'
	)
	High = go.Scatter(
			x = x_axis,
			y = y_axis2,
			mode = 'lines',
			name = 'High',
				line = dict(width=0.5,
									color='rgb(224, 151, 4)'),
			fill = 'tonexty'
	)
	Medium = go.Scatter(
			x = x_axis,
			y = y_axis3,
			mode = 'lines',
			name = 'Medium',
				line = dict(width = 0.5,
									color = 'rgb(237, 187, 7)'),
			fill = 'tonexty'
	)
	Low = go.Scatter(
			x = x_axis,
			y = y_axis4,
			mode = 'lines',
			name = 'Low',
				line = dict(width=0.5,
									color = 'rgb(15, 183, 3)'),
			fill='tonexty'
	)
	data = [Crititcal, High, Medium, Low]
	layout = go.Layout(
			showlegend = True,
			xaxis = dict(
					type = 'category',
			),
			yaxis=dict(
					type = 'linear',
					range = [1, 100],
					dtick = 20,
					ticksuffix = '%'
			)
	)
	fig = go.Figure(data = data, layout = layout)
	py.plot(fig, filename = 'stacked_area_plot')