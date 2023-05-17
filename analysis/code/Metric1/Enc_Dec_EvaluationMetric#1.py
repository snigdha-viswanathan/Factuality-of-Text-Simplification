#install streamlit: pip install streamlit
# run the program: streamlit run T5_EvalMetric1.py


#<Filename>_withGold.csv should be in the format of 
#Index(['source_sentence', 'pred', 'gold', 'sentence_id',
#       'bert_score_precision_pred_with_brevity_penalty', 'dae_score_pred',
#       'bart_score_pred', 'bert_score_precision_gold_with_brevity_penalty',
#       'dae_score_gold', 'bart_score_gold'],

import pandas as pd
import streamlit as st
import plotly.graph_objects as go

#T5 eval metric #1
csv_files = [
    ('input_files/EncDec/EncDec_baseline_Dataset_AllScore_withGold.csv', 'Baseline'),
    ('input_files/EncDec/EncDec_Bart_Dataset_AllScore_withGold.csv', 'BART'),
    ('input_files/EncDec/EncDec_Bert_Dataset_AllScore_withGold.csv', 'BERT'),
    ('input_files/EncDec/EncDec_Dae_Dataset_AllScore_withGold.csv','DAE'),
    ('input_files/EncDec/EncDec_merged_Dataset_AllScore_withGold.csv','Merged'),
]

# Initialize empty lists for categories and groups
categories = []
group1 = []
group2 = []
group3 = []

# Iterate over the CSV files
for csv_file, label in csv_files:
    # Read the CSV file
    df = pd.read_csv(csv_file)
    
    # Extract the necessary columns
    categories.append(label)
    group1.append(df['bart_score_pred'].mean())
    group2.append(df['bert_score_precision_pred_with_brevity_penalty'].mean())
    group3.append(df['dae_score_pred'].mean())

group1_rounded = [round(value, 3) for value in group1]
group2_rounded = [round(value, 3) for value in group2]
group3_rounded = [round(value, 3) for value in group3]

colors = ['royalblue', 'salmon', 'teal']
# Create a Bar chart figure
fig = go.Figure(data=[
    go.Bar(name='Bart Score', x=categories, y=group1, text=group1_rounded, textposition='outside', marker=dict(color=colors[0])),
    go.Bar(name='Bert Score', x=categories, y=group2, text=group2_rounded, textposition='outside', marker=dict(color=colors[1])),
    go.Bar(name='DAE Score', x=categories, y=group3, text=group3_rounded, textposition='outside', marker=dict(color=colors[2]))
])

# Set the layout
fig.update_layout(
    xaxis_title='Models',
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

# Render the chart using Streamlit
st.plotly_chart(fig)
#fig.write_image("EncDec_EvaluationMetric#1.png")









