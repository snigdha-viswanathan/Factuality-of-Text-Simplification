#Comprehensive Folder structure
```
analysis
 ┣ code
 ┃ ┣ Metric1
 ┃ ┃ ┣ Enc_Dec_EvaluationMetric#1.py
 ┃ ┃ ┣ Pegasus_EvaluationMetric#1.py
 ┃ ┃ ┗ T5_EvaluationMetric#1.py
 ┃ ┣ Metric2
 ┃ ┃ ┣ EncDec_EvaluationMetric#2.py
 ┃ ┃ ┣ Pegasus_EvaluationMetric#2.py
 ┃ ┃ ┗ T5_EvaluationMetric#2.py
 ┃ ┣ Metric3
 ┃ ┃ ┗ EvaluationMetric#3.py
 ┃ ┗ .DS_Store
 ┣ images
 ┃ ┣ EncDec
 ┃ ┃ ┣ Metric1
 ┃ ┃ ┣ Metric2
 ┃ ┣ Metric3
 ┃ ┣ Pegasus
 ┃ ┃ ┣ Metric1
 ┃ ┃ ┣ Metric2
 ┃ ┣ T5
 ┃ ┃ ┣ Metric1
 ┃ ┃ ┣ Metric2
 ┣ input_files
 ┃ ┣ EncDec
 ┃ ┣ Metric3
 ┃ ┣ Pegasus
 ┃ ┣ T5
 ┣ README.md
 ┗ requirements.txt
```

To run the evaluation metrics code, follow the steps below:
## 1. Install dependencies

```pip install -r requirements.txt```

## 2. Start the server
For example, 

If you want to run Evaluation metric 1 of T5
```streamlit run code/Metric1/T5_EvaluationMetric#1.py```

If you want to run Evaluation metric 2 of Pegasus
```streamlit run code/Metric2/Pegasus_EvaluationMetric#2.py```