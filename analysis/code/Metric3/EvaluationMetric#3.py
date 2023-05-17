import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import numpy as np
from scipy.stats import norm


csv_files = [
    ('input_files/Metric3/all_scores_merged.csv')
]

for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    #print(df['Human Score'] - df['LLM Score'])
    df['Score Difference'] = df['Human Score'] - df['LLM Score']

    difference = df['Human Score'] - df['LLM Score']

    # Count the number of samples with each difference
    difference_counts = difference.value_counts().sort_index()
    #print(difference_counts[df['Score Difference']])
    # Create line plot for the difference counts
    #filtered_difference = difference[(difference >= -5) & (difference <= 5)]

# Create histogram for the filtered differences
fig = go.Figure()
fig.add_trace(go.Histogram(x=df['Score Difference'], y=difference_counts[df['Score Difference']]))

# Configure the layout
fig.update_layout(title='Distribution of Differences between Human Score and LLM Score',
                  xaxis_title='Difference',
                  yaxis_title='No. of Samples')

# Set x-axis range from -5 to +5
fig.update_xaxes(range=[-5, 5]) 
st.plotly_chart(fig)



csv_files = [
    ('input_files/Metric3/all_scores_cleaned.csv'),
    ('input_files/Metric3/all_scores_uncleaned.csv')
]

box_traces = []

# Custom labels for the box plots
labels = ['Cleaned Data', 'Uncleaned Data']

# Iterate over each CSV file and custom label
for csv_file, label in zip(csv_files, labels):
    df = pd.read_csv(csv_file)
    df['Score Difference'] = df['Human Score'] - df['LLM Score']
    
    # Add the box trace with custom label
    box_trace = go.Box(y=df['Score Difference'], name=label, hovertext=df['Score Difference'],
                       hoverinfo='y+text')
    box_traces.append(box_trace)

# Create the figure with box traces
fig = go.Figure(data=box_traces)

# Configure the layout
fig.update_layout(title='Difference between Human Score and LLM Score',
                  yaxis_title='Score Difference')

# Display the plot using Streamlit
st.plotly_chart(fig)





