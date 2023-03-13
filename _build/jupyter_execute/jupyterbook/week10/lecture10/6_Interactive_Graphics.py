#!/usr/bin/env python
# coding: utf-8

# # 📝 Interactive Plotting with Bokeh

# Python Bokeh is a Data Visualization library that provides interactive charts and plots. Bokeh renders its plots using HTML and JavaScript that uses modern web browsers for presenting elegant, concise construction of novel graphics with high-level interactivity
# 
# * Flexibility: Bokeh can be used for common plotting requirements and for custom and complex use-cases.

# * Productivity: Its interaction with other popular Pydata tools (such as Pandas and Jupyter notebook) is very easy.

# * Interactivity: It creates interactive plots that change with the user interaction.

# * Powerful: Generation of visualizations for specialized use-cases can be done by adding JavaScript.

# * Shareable: Visual data are shareable. They can also be rendered in Jupyter notebooks.

# * Open source: Bokeh is an open-source project.

# In[1]:


get_ipython().run_cell_magic('capture', '', '!pip install bokeh\n')


# ## A Simple Multiline Plot

# In[2]:


import numpy as np
from bokeh.layouts import gridplot
from bokeh.plotting import figure
from bokeh.io import output_notebook, show


x = np.linspace(0, 4*np.pi, 100)
y = np.sin(x)

TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select"

p1 = figure(title="Legend Example", tools=TOOLS)

p1.circle(x,   y, legend_label="sin(x)")
p1.circle(x, 2*y, legend_label="2*sin(x)", color="orange")
p1.circle(x, 3*y, legend_label="3*sin(x)", color="green")

p1.legend.title = 'Markers'

p2 = figure(title="Another Legend Example", tools=TOOLS)

p2.circle(x, y, legend_label="sin(x)")
p2.line(x, y, legend_label="sin(x)")

p2.line(x, 2*y, legend_label="2*sin(x)",
        line_dash=(4, 4), line_color="orange", line_width=2)

p2.square(x, 3*y, legend_label="3*sin(x)", fill_color=None, line_color="green")
p2.line(x, 3*y, legend_label="3*sin(x)", line_color="green")

p2.legend.title = 'Lines'
output_notebook()
show(gridplot([p1, p2], ncols=2, width=400, height=400))


# ## Elements with labels

# In[3]:


import pandas as pd

from bokeh.models import ColumnDataSource, LabelSet
from bokeh.plotting import figure, show
from bokeh.sampledata.periodic_table import elements

elements = elements.copy()
elements = elements[elements["atomic number"] <= 82]
elements = elements[~pd.isnull(elements["melting point"])]
mass = [float(x.strip("[]")) for x in elements["atomic mass"]]
elements["atomic mass"] = mass

palette = ["#053061", "#2166ac", "#4393c3", "#92c5de", "#d1e5f0",
           "#f7f7f7", "#fddbc7", "#f4a582", "#d6604d", "#b2182b", "#67001f"]

melting_points = elements["melting point"]
low = min(melting_points)
high = max(melting_points)
melting_point_inds = [int(10*(x-low)/(high-low)) for x in melting_points] #gives items in colors a value from 0-10
elements['melting_colors'] = [palette[i] for i in melting_point_inds]

TITLE = "Density vs Atomic Weight of Elements (colored by melting point)"
TOOLS = "hover,pan,wheel_zoom,box_zoom,reset,save"

p = figure(tools=TOOLS, toolbar_location="above", width=1200, title=TITLE)
p.toolbar.logo = "grey"
p.background_fill_color = "#efefef"
p.xaxis.axis_label = "atomic weight (amu)"
p.yaxis.axis_label = "density (g/cm^3)"
p.grid.grid_line_color = "white"
p.hover.tooltips = [
    ("name", "@name"),
    ("symbol:", "@symbol"),
    ("density", "@density"),
    ("atomic weight", "@{atomic mass}"),
    ("melting point", "@{melting point}")
]

source = ColumnDataSource(elements)

p.scatter("atomic mass", "density", size=12, source=source,
          color='melting_colors', line_color="black", alpha=0.9)

labels = LabelSet(x="atomic mass", y="density", text="symbol", y_offset=8,
                  text_font_size="11px", text_color="#555555",
                  source=source, text_align='center')
p.add_layout(labels)
output_notebook()

show(p)


# ## Images as Scatter Objects

# In[4]:


import numpy as np

from bokeh.core.properties import value
from bokeh.plotting import figure, show

url = "https://courses.coe.drexel.edu/ENGR/ENGR131W23/_static/Drexel_Vertical%20stacked_Lockup_HEX.png"
x = np.random.random(150) * 100
y = np.random.random(150) * 100

p = figure(match_aspect=True, toolbar_location=None,
           background_fill_color="#efefef")

# value is used here to prevent the string URL from being
# interpreted as a column name from the data source.
p.image_url(url=value(url), x=x, y=y, alpha=0.7, anchor="center",
            w=18, w_units="screen", h=18, h_units="screen")

output_notebook()
show(p)


# ## Recreating Activity 2

# In[5]:


import bokeh.plotting as bp
from bokeh.models import ColumnDataSource, LinearColorMapper, ColorBar, HoverTool, LabelSet
from bokeh.palettes import Viridis256
import pandas as pd

# read the employment projection data
path = "./data/employment-projections.csv"

# open the file at the specified path for reading and give it the name f
with open(path, "r") as f:
    # create a pandas dataframe from the comma-separated file
    df = pd.read_csv(f, delimiter=",")

# add a new column to the dataframe, which is the size of the employment2021 scaled down by a factor of 5
df['employment2021size_scaled'] = [x/5 for x in df['Employment 2021']]
    
# create a new bokeh plot
p = bp.figure(
    x_axis_label='Employment Change, 2021-2031 (%)',
    y_axis_label='Median Annual Wage 2021 ($)',
    title='Bubble Plot of Employment Projections for Engineers'
)

# create a column data source for the plot using the pandas dataframe
source = ColumnDataSource(df)

# create a color mapper for the scatter plot
color_mapper = LinearColorMapper(palette=Viridis256, low=0, high=len(df))

# create a scatter plot of the data, with the size of the bubbles determined by the scaled employment2021 size
# and the color of the bubbles determined by the index of the data points and the color mapper
scatter = p.scatter(
    x='Employment Percent Change, 2021-2031',
    y='Median Annual Wage 2021',
    source=source,
    size='employment2021size_scaled',
    color={'field': 'index', 'transform': color_mapper},
    alpha=0.3
)

# create a label set for the plot, which will display the occupation title for each bubble
labels = LabelSet(
    x='Employment Percent Change, 2021-2031',
    y='Median Annual Wage 2021',
    text='Occupation Title',
    level='glyph',
    x_offset=5,
    y_offset=5,
    source=source,
    text_font_size='10pt'
)

# create a hover tool for the scatter plot, which will display information about each data point on mouseover
hover = HoverTool(
    tooltips=[
        ("Occupational Openings, 2021-2031", "@{Occupational Openings, 2021-2031 Annual Average}%"), 
        ("Median Annual Wage", "@{Median Annual Wage 2021}{$0,0}")
    ],
    renderers=[scatter]
)

# create a color bar for the scatter plot, which will show the color mapping used for the bubbles
color_bar = ColorBar(color_mapper=color_mapper, label_standoff=12, location=(0, 0))

# add the color bar, hover tool, and label set to the plot
p.add_layout(color_bar, 'right')
p.add_tools(hover)
p.add_layout(labels)

output_notebook()
# display the plot
bp.show(p)


# In[ ]:




