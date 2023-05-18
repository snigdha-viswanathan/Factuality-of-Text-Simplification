# factuality_of_text_simplification

In this project, we have proposed a novel methodology that combines factual consistency with text simplification. By integrating these two components, we can identify and remove the problematic instances present in text simplification dataset while ensuring the integrity of the original information.

Install the required packages given in requirements.txt.

We will be using the Wiki Large Dataset which is the benchmark dataset used for text simplification tasks.[WikiLarge Dataset](https://github.com/louismartin/dress-data/raw/master/data-simplification.tar.bz2)

The final training datasets are given in the path: datasets/final_training_data
The test dataset is given in the path: datasets/test_data

Our pipeline is given as follows:

## STEP 1: Factuality Module


### 1.1. Bart Score
```
Follow the instructions given in the repo: https://github.com/neulab/BARTScore/tree/main
(remove the BLEURT score installation from the requirements.txt)
Add the repo to the factuality_checking\dataset_selection\BART_score\code directory
Run all cells in the python notebook in factuality_checking\dataset_selection\BART_score\code\Compute_Bart_score.ipynb
The input for this module is found in the factuality_checking\training_dataset_20k.csv"
The output for these files is stored in this directory factuality_of_text_simplification\datasets\final_training_data
```

### 1.2. Dependency Arc Entailment
```
Follow the instructions given in the repo: https://github.com/tagoyal/dae-factuality/tree/main to run dae. 
Make changes to the evaluate_factuality.py given in the path: factuality_checking/dataset_selection/DAE_score/code/evaluate_factuality.py before running the code.
The input for this module is found in the factuality_checking\training_dataset_20k.csv"
The output for these files is stored in this directory: factuality_of_text_simplification\datasets\final_training_data\

```

### 1.3 BertScoreArt
```
Run all cells in the python notebook in factuality_checking\dataset_selection\BART_score\code\Compute_Bert_score.ipynb
The input for this module is found in the factuality_checking\training_dataset_20k.csv"
The output for these files is stored in this directory datasets\final_training_data
```


## STEP 2: Model Training
###  2.1. T5
```
Run all the cells in the Python Notebook in ‘models/T5/training/T5-simplification.ipynb’
```
### 2.2. Pegasus
```
Run all the cells in the Python Notebook in ‘models/Pegasus/training/Pegasus_Training.ipynb’
```
### 2.3. Encoder-Decoder model
```
Run the cells till “Seq to Seq model for Text Simplification - Training” in the Python Notebook in ‘models/Enc-Dec/training/685_Project_Enc_Dec_Training_Inference.ipynb
```

## STEP 3: Inference
### 3.1. T5
```
Run all the cells in the Python Notebook in ‘models/T5/inference/All_datasets_inference.ipynb’
The inference csv files of T5 model are present in ‘models/T5/inference/output_files’
```
### 3.2. Pegasus
```
Run all the cells in the Python Notebook in ‘models/Pegasus/inference/Pegasus_Inference.ipynb’
The inference csv files of Pegasus model are present in ‘models/Pegasus/inference/output_files’
```
### 3.3. Encoder-Decoder model
```
Run the cells under “Seq to Seq model for Text Simplification “Seq 2 Seq model for text Simplification - Inference” in the Python Notebook in “models/Enc-Dec/inference/685_Project_Enc_Dec_Training_Inference.ipynb”
The Inference files are stored under “models/Enc-Dec/inference/output_files/” folder
```

## STEP 4: Evaluation
### 4.1. BART Score
```
Run all cells under ‘models/Pegasus/evaluation/BART/Compute_Bart_Score.ipynb’ to compute the BART score for Pegasus model using the inference files.
Similarly, follow the same instructions to compute BART score for the other models by running the Python notebook in the corresponding model’s evaluation folder.
```
### 4.2. BERT Score
```
Run all cells under ‘models/Pegasus/evaluation/BERT/Compute_Bert_score.ipynb’ to compute the BERT score for Pegasus model using the inference files.
Similarly, follow the same instructions to compute BERT score for the other models by running the Python notebook in the corresponding model’s evaluation folder.

```
### 4.3. DAE Score
```
Follow instructions in Step 1.2 to execute  ‘models/Pegasus/evaluation/DAE/evaluate_factuality.py’ to compute the DAE score for Pegasus model using the inference files.
Similarly, follow the same instructions to compute DAE score for the other models by running the Python notebook in the corresponding model’s evaluation folder.
```

## STEP 5: Analysis:
To run the evaluation metrics code, follow the steps below:
## 1. Install dependencies

```
pip install -r analysis/requirements.txt
```

## 2. Start the streamlit server to get the graphs accordingly
For example, 

If you want to run Evaluation metric 1 of T5
```
streamlit run analysis/code/Metric1/T5_EvaluationMetric#1.py
```

If you want to run Evaluation metric 2 of Pegasus
```
streamlit run analysis/code/Metric2/Pegasus_EvaluationMetric#2.py
```

## Folder Structure
 <pre>
 ┣ analysis
 ┃ ┣ <b>code - This directory contains the code files to generate the graphs for all the three metrics, for each model
 ┃ ┣ <b>images - This directory contains the images generated for each metric
 ┃ ┣ <b>input_files - This directory contains of the input files for the analysis section
 ┃ ┣ <b>manual evaluation - This directory contains the annotated csv files for the manual evaluation section
 ┣ datasets
 ┃ ┣ <b>final_training_data - This directory consists of the baseline and factual dataset
 ┃ ┗ <b>test_data - This directory consists of the test data
 ┣ factuality_checking
 ┃ ┣ <b>dataset_selection - In this directory we use all three metrics to score and rank the dataset sampled from wiki large
 ┃ ┃ ┣ <b>BART_score - This folder consists of training data, along with the code folder consisting of the BART score and the corresponding output files.
 ┃ ┃ ┣ <b>BERT_score -This folder consists of training data, along with the code folder consisting of the BERT score and the corresponding output files.
 ┃ ┃ ┗ <b>DAE_score -This folder consists of training data, along with the code folder consisting of the DAE score and the corresponding output files.
 ┣ <b>models - This directory consists a folder for each model. For each model, it consists of an evaluation - which has the evaluation code and scores for each metric, inference - which has the inference outputs and training folder- which has the training code.
 s

</pre>