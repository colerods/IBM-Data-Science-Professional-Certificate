#!/usr/bin/env python
# coding: utf-8

# <center>
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/labs/Module%204/logo.png" width="300" alt="cognitiveclass.ai logo" />
# </center>
# 

# # Basic Plotly Charts
# 
# Estimated time needed: 30 minutes
# 

# ## Objectives
# 
# In this lab, you will learn about creating plotly charts using plotly.graph_objects and plotly.express.
# 
# Learn more about:
# 
# *   [Plotly python](https://plotly.com/python/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ENSkillsNetwork20297740-2021-01-01)
# *   [Plotly Graph Objects](https://plotly.com/python/graph-objects/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ENSkillsNetwork20297740-2021-01-01)
# *   [Plotly Express](https://plotly.com/python/plotly-express/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ENSkillsNetwork20297740-2021-01-01)
# *   Handling data using [Pandas](https://pandas.pydata.org/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ENSkillsNetwork20297740-2021-01-01)
# 
# We will be using the [airline dataset](https://developer.ibm.com/exchanges/data/all/airline/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ENSkillsNetwork20297740-2021-01-01) from [Data Asset eXchange](https://developer.ibm.com/exchanges/data/).
# 
# #### Airline Reporting Carrier On-Time Performance Dataset
# 
# The Reporting Carrier On-Time Performance Dataset contains information on approximately 200 million domestic US flights reported to the United States Bureau of Transportation Statistics. The dataset contains basic information about each flight (such as date, time, departure airport, arrival airport) and, if applicable, the amount of time the flight was delayed and information about the reason for the delay. This dataset can be used to predict the likelihood of a flight arriving on time.
# 
# Preview data, dataset metadata, and data glossary [here.](https://dax-cdn.cdn.appdomain.cloud/dax-airline/1.0.1/data-preview/index.html)
# 

# In[2]:


import piplite

await piplite.install(['nbformat', 'plotly'])


# In[3]:


# Import required libraries
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# # Read Data
# 

# In[4]:


# Read the airline data into pandas dataframe
from js import fetch
import io

URL = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv'
resp = await fetch(URL)
text = io.BytesIO((await resp.arrayBuffer()).to_py())

airline_data =  pd.read_csv(text,
                            encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str, 
                                   'Div2Airport': str, 'Div2TailNum': str})

print('Data downloaded and read into a dataframe!')


# In[5]:


# Preview the first 5 lines of the loaded data 
airline_data.head()


# In[6]:


# Shape of the data
airline_data.shape


# In[7]:


# Randomly sample 500 data points. Setting the random state to be 42 so that we get same result.
data = airline_data.sample(n=500, random_state=42)


# In[8]:


# Get the shape of the trimmed data
data.shape


# ### Lab structure
# 
# #### plotly.graph_objects
# 
# 1.  Review scatter plot creation
# 
#     Theme: How departure time changes with respect to airport distance
# 
# 2.  **To do** - Create line plot
# 
#     Theme: Extract average monthly delay time and see how it changes over the year
# 
# #### plotly.express
# 
# 1.  Review bar chart creation
# 
#     Theme: Extract number of flights from a specific airline that goes to a destination
# 
# 2.  **To do** - Create bubble chart
# 
#     Theme: Get number of flights as per reporting airline
# 
# 3.  **To do** - Create histogram
# 
#     Theme: Get distribution of arrival delay
# 
# 4.  Review pie chart
# 
#     Theme: Proportion of distance group by month (month indicated by numbers)
# 
# 5.  **To do** - Create sunburst chart
# 
#     Theme: Hierarchical view in othe order of month and destination state holding value of number of flights
# 

# # plotly.graph_objects¶
# 

# ## 1. Scatter Plot
# 

# Learn more about usage of scatter plot [here](https://plotly.com/python/line-and-scatter/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ENSkillsNetwork20297740-2021-01-01)
# 
# #### Idea: How departure time changes with respect to airport distance
# 

# In[9]:


# First we create a figure using go.Figure and adding trace to it through go.scatter
fig = go.Figure(data=go.Scatter(x=data['Distance'], y=data['DepTime'], mode='markers', marker=dict(color='red')))
# Updating layout through `update_layout`. Here we are adding title to the plot and providing title to x and y axis.
fig.update_layout(title='Distance vs Departure Time', xaxis_title='Distance', yaxis_title='DepTime')
# Display the figure
fig.show()


# ## 2. Line Plot
# 

# Learn more about line plot [here](https://plotly.com/python/line-charts/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ENSkillsNetwork20297740-2021-01-01)
# 
# #### Idea: Extract average monthly arrival delay time and see how it changes over the year.
# 

# In[10]:


# Group the data by Month and compute average over arrival delay time.
line_data = data.groupby('Month')['ArrDelay'].mean().reset_index()


# In[11]:


# Display the data
line_data


# #### To do:
# 
# *   Create a line plot with x-axis being the month and y-axis being computed average delay time. Update plot title,\
#     xaxis, and yaxis title.
# 
# *   Hint: Scatter and line plot vary by updating mode parameter.
# 

# In[12]:


# Create line plot here
fig = go.Figure(data=go.Scatter(x=line_data['Month'], y=line_data['ArrDelay'], mode='lines', marker=dict(color='green')))
fig.update_layout(title='Month vs Average Flight Delay Time', xaxis_title='Month', yaxis_title='ArrDelay')
fig.show()


# Double-click **here** for the solution.
# 
# <!-- The answer is below:
# 
# fig = go.Figure(data=go.Scatter(x=line_data['Month'], y=line_data['ArrDelay'], mode='lines', marker=dict(color='green')))
# fig.update_layout(title='Month vs Average Flight Delay Time', xaxis_title='Month', yaxis_title='ArrDelay')
# fig.show()
# 
# -->
# 

# # plotly.express¶
# 

# ## 1. Bar Chart
# 

# Learn more about bar chart [here](https://plotly.com/python/bar-charts/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ENSkillsNetwork20297740-2021-01-01)
# 
# #### Idea: Extract number of flights from a specific airline that goes to a destination
# 

# In[13]:


# Group the data by destination state and reporting airline. Compute total number of flights in each combination
bar_data = data.groupby(['DestState'])['Flights'].sum().reset_index()


# In[14]:


# Display the data
bar_data


# In[15]:


# Use plotly express bar chart function px.bar. Provide input data, x and y axis variable, and title of the chart.
# This will give total number of flights to the destination state.
fig = px.bar(bar_data, x="DestState", y="Flights", title='Total number of flights to the destination state split by reporting airline') 
fig.show()


# ## 2. Bubble Chart
# 

# Learn more about bubble chart [here](https://plotly.com/python/bubble-charts/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ENSkillsNetwork20297740-2021-01-01)
# 
# #### Idea: Get number of flights as per reporting airline
# 

# In[16]:


# Group the data by reporting airline and get number of flights
bub_data = data.groupby('Reporting_Airline')['Flights'].sum().reset_index()


# In[17]:


bub_data


# **To do**
# 
# *   Create a bubble chart using the `bub_data` with x-axis being reporting airline and y-axis being flights.
# *   Provide title to the chart
# *   Update size of the bubble based on the number of flights. Use `size` parameter.
# *   Update name of the hover tooltip to `reporting_airline` using `hover_name` parameter.
# 

# In[18]:


# Create bubble chart here
fig = px.scatter(bub_data, x="Reporting_Airline", y="Flights", size="Flights",
                 hover_name="Reporting_Airline", title='Reporting Airline vs Number of Flights', size_max=60)
fig.show()


# Double-click **here** for the solution.
# 
# <!-- The answer is below:
# 
#     
# fig = px.scatter(bub_data, x="Reporting_Airline", y="Flights", size="Flights",
#                  hover_name="Reporting_Airline", title='Reporting Airline vs Number of Flights', size_max=60)
# fig.show()
# 
# -->
# 

# # Histogram
# 

# Learn more about histogram [here](https://plotly.com/python/histograms/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ENSkillsNetwork20297740-2021-01-01)
# 
# #### Idea: Get distribution of arrival delay
# 

# In[19]:


# Set missing values to 0
data['ArrDelay'] = data['ArrDelay'].fillna(0)


# **To do**
# 
# *   Use px.histogram and pass the dataset.
# *   Pass `ArrDelay` to x parameter.
# 

# In[20]:


# Create histogram here
fig = px.histogram(data, x="ArrDelay")
fig.show()


# Double-click **here** for the solution.
# 
# <!-- The answer is below:
# 
# fig = px.histogram(data, x="ArrDelay")
# fig.show()
# 
# -->
# 

# # Pie Chart
# 

# Learn more about pie chart [here](https://plotly.com/python/pie-charts/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ENSkillsNetwork20297740-2021-01-01)
# 
# #### Idea: Proportion of distance group by month (month indicated by numbers)
# 

# In[21]:


# Use px.pie function to create the chart. Input dataset. 
# Values parameter will set values associated to the sector. 'Month' feature is passed to it.
# labels for the sector are passed to the `names` parameter.
fig = px.pie(data, values='Month', names='DistanceGroup', title='Distance group proportion by month')
fig.show()


# # Sunburst Charts
# 

# Learn more about sunburst chart [here](https://plotly.com/python/sunburst-charts/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ENSkillsNetwork20297740-2021-01-01)
# 
# #### Idea: Hierarchical view in othe order of month and destination state holding value of number of flights
# 

# **To do**
# 
# *   Create sunburst chart using `px.sunburst`.
# *   Define hierarchy of sectors from root to leaves in `path` parameter. Here, we go from `Month` to `DestStateName` feature.
# *   Set sector values in `values` paramter. Here, we can pass in `Flights` feature.
# *   Show the figure.
# 

# In[22]:


# Create sunburst chart here
fig = px.sunburst(data, path=['Month', 'DestStateName'], values='Flights')
fig.show()


# Double-click **here** for the solution.
# 
# <!-- The answer is below:
#     
# fig = px.sunburst(data, path=['Month', 'DestStateName'], values='Flights')
# fig.show()
# 
# -->
# 

# ## Summary
# 
# Congratulations for completing your first lab.
# 
# In this lab, you have learnt how to use `plotly.graph_objects` and `plotly.express` for creating plots and charts.
# 

# ## Author
# 
# [Saishruthi Swaminathan](https://www.linkedin.com/in/saishruthi-swaminathan/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ENSkillsNetwork20297740-2021-01-01)
# 

# ## Changelog
# 
# | Date       | Version | Changed by | Change Description                   |
# | ---------- | ------- | ---------- | ------------------------------------ |
# | 12-18-2020 | 1.0     | Nayef      | Added dataset link and upload to Git |
# 

# ## <h3 align="center"> © IBM Corporation 2020. All rights reserved. <h3/>
# 
