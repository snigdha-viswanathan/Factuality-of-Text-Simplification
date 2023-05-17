import pandas as pd
import streamlit as st
import plotly.graph_objects as go

# Define the file paths and labels for each file
file_paths = [
  ('input_files/T5/T5_Baseline_AllScores_withGold.csv', 'Baseline'),
    ('input_files/T5/T5_Bart_AllScores_withGold.csv', 'BART'),
    ('input_files/T5/T5_Bert_AllScores_withGold.csv', 'BERT'),
    ('input_files/T5/T5_dae_AllScores_withGold.csv','DAE'),
    ('input_files/T5/T5_Merged_AllScores_withGold.csv','Merged'),
]

# Define the categories and groups
categories = ['BART_Score', 'BERT_Score', 'DAE_Score']
groups = ['pred', 'gold']

# Create a list to store the figures
figures = []

# Iterate over the file paths and generate a figure for each file
for file_path, label in file_paths:
    # Read the CSV file
    df = pd.read_csv(file_path)
    print(label)
    # Initialize empty lists for the average performance scores
    avg_scores = {category: [] for category in categories}
    count_higher_pred = {category: [0,0] for category in categories}
    # Calculate the average performance scores for each category and group
    for category in categories:
        for group in groups:
            if group == 'pred':
                if category == 'BART_Score':
                    column_name = 'bart_score_pred'
                elif category == 'BERT_Score':
                    column_name = 'bert_score_precision_pred_with_brevity_penalty'
                else:  # DAE_Score
                    column_name = 'dae_score_pred'
            else:  # group == 'gold'
                if category == 'BART_Score':
                    column_name = 'bart_score_gold'
                elif category == 'BERT_Score':
                    column_name = 'bert_score_precision_gold_with_brevity_penalty'
                else:  # DAE_Score
                    column_name = 'dae_score_gold'
            avg_score = df[column_name].mean()
            avg_scores[category].append(round(avg_score, 2))

    for category in categories:
        if category == 'BART_Score':
            #print(df['bart_score_pred'].count, df['bert_score_precision_pred_with_brevity_penalty'].count)
            num_higher_values = (df['bart_score_pred'] > df['bart_score_gold']).sum()
            #print(f"{category}: {num_higher_values}")
        elif category == 'BERT_Score':
            #print(df['bart_score_pred'].count, df['bert_score_precision_pred_with_brevity_penalty'].count)
            num_higher_values = (df['bert_score_precision_pred_with_brevity_penalty'] > df['bert_score_precision_gold_with_brevity_penalty']).sum()
            #print(f"{category}: {num_higher_values}")
        else:
            #print(df['bart_score_pred'].count, df['bert_score_precision_pred_with_brevity_penalty'].count)
            num_higher_values = (df['dae_score_pred'] > df['dae_score_gold']).sum()
            #print(f"{category}: {num_higher_values}")
        count_higher_pred[category][0] = num_higher_values
        count_higher_pred[category][1] = len(df) - num_higher_values


    fig2 = go.Figure()
    for group in groups:
        fig2.add_trace(go.Bar(
            name=group.capitalize(),
            x=categories,
            y=[count_higher_pred[category][groups.index(group)] for category in categories],
            text=[count_higher_pred[category][groups.index(group)] for category in categories],
            textposition='outside',
        ))
    
    # Set the layout
    fig2.update_layout(
        xaxis_title='Metrics',
        yaxis_title='No. of words',
        barmode='stack',
        legend = dict(
        orientation = 'h',
        yanchor = 'bottom',
        y=1.02,
        xanchor = 'right',
        x=1
    )
    )

    # Create a Bar chart figure
    fig = go.Figure()

    # Add the bars for each group
    for group in groups:
        fig.add_trace(go.Bar(
            name=group.capitalize(),
            x=categories,
            y=[avg_scores[category][groups.index(group)] for category in categories],
            text=[avg_scores[category][groups.index(group)] for category in categories],
            textposition='outside',
        ))

    # Set the layout
    fig.update_layout(
        xaxis_title='Metrics',
        yaxis_title='Average Performance',
        barmode='group',
        legend = dict(
        orientation = 'h',
        yanchor = 'bottom',
        y=1.02,
        xanchor = 'right',
        x=1
    )
    )

    # Add the figure to the list
    figures.append(fig)
    figures.append(fig2)

# Render the charts using Streamlit
for index, fig in enumerate(figures):
    st.plotly_chart(fig, use_container_width=True, label=f'Figure {index+1}')
