# factuality_of_text_simplification

factuality_of_text_simplification
 ┣ .git
 ┃ ┣ hooks
 ┃ ┃ ┣ applypatch-msg.sample
 ┃ ┃ ┣ commit-msg.sample
 ┃ ┃ ┣ fsmonitor-watchman.sample
 ┃ ┃ ┣ post-update.sample
 ┃ ┃ ┣ pre-applypatch.sample
 ┃ ┃ ┣ pre-commit.sample
 ┃ ┃ ┣ pre-merge-commit.sample
 ┃ ┃ ┣ pre-push.sample
 ┃ ┃ ┣ pre-rebase.sample
 ┃ ┃ ┣ pre-receive.sample
 ┃ ┃ ┣ prepare-commit-msg.sample
 ┃ ┃ ┣ push-to-checkout.sample
 ┃ ┃ ┗ update.sample
 ┃ ┣ info
 ┃ ┃ ┗ exclude
 ┃ ┣ logs
 ┃ ┃ ┣ refs
 ┃ ┃ ┃ ┣ heads
 ┃ ┃ ┃ ┃ ┗ main
 ┃ ┃ ┃ ┗ remotes
 ┃ ┃ ┃ ┃ ┗ origin
 ┃ ┃ ┃ ┃ ┃ ┗ HEAD
 ┃ ┃ ┗ HEAD
 ┃ ┣ objects
 ┃ ┃ ┣ info
 ┃ ┃ ┗ pack
 ┃ ┃ ┃ ┣ pack-de9c111c883a8523f88a0e673d460d2a5ad462a4.idx
 ┃ ┃ ┃ ┗ pack-de9c111c883a8523f88a0e673d460d2a5ad462a4.pack
 ┃ ┣ refs
 ┃ ┃ ┣ heads
 ┃ ┃ ┃ ┗ main
 ┃ ┃ ┣ remotes
 ┃ ┃ ┃ ┗ origin
 ┃ ┃ ┃ ┃ ┗ HEAD
 ┃ ┃ ┗ tags
 ┃ ┣ HEAD
 ┃ ┣ config
 ┃ ┣ description
 ┃ ┣ index
 ┃ ┗ packed-refs
 ┣ analysis
 ┃ ┣ code
 ┃ ┃ ┣ Metric1
 ┃ ┃ ┃ ┣ Enc_Dec_EvaluationMetric#1.py
 ┃ ┃ ┃ ┣ Pegasus_EvaluationMetric#1.py
 ┃ ┃ ┃ ┗ T5_EvaluationMetric#1.py
 ┃ ┃ ┣ Metric2
 ┃ ┃ ┃ ┣ EncDec_EvaluationMetric#2.py
 ┃ ┃ ┃ ┣ Pegasus_EvaluationMetric#2.py
 ┃ ┃ ┃ ┗ T5_EvaluationMetric#2.py
 ┃ ┃ ┣ Metric3
 ┃ ┃ ┃ ┗ EvaluationMetric#3.py
 ┃ ┃ ┗ .DS_Store
 ┃ ┣ images
 ┃ ┃ ┣ EncDec
 ┃ ┃ ┃ ┣ Metric1
 ┃ ┃ ┃ ┃ ┣ .DS_Store
 ┃ ┃ ┃ ┃ ┗ EM1_EncDec.png
 ┃ ┃ ┃ ┣ Metric2
 ┃ ┃ ┃ ┃ ┣ .DS_Store
 ┃ ┃ ┃ ┃ ┣ EM2_ED_BART.png
 ┃ ┃ ┃ ┃ ┣ EM2_ED_BART1.png
 ┃ ┃ ┃ ┃ ┣ EM2_ED_BERT.png
 ┃ ┃ ┃ ┃ ┣ EM2_ED_BERT1.png
 ┃ ┃ ┃ ┃ ┣ EM2_ED_DAE.png
 ┃ ┃ ┃ ┃ ┣ EM2_ED_DAE1.png
 ┃ ┃ ┃ ┃ ┣ EM2_ED_Merged.png
 ┃ ┃ ┃ ┃ ┗ EM2_ED_Merged1.png
 ┃ ┃ ┃ ┗ .DS_Store
 ┃ ┃ ┣ Metric3
 ┃ ┃ ┃ ┣ .DS_Store
 ┃ ┃ ┃ ┣ EM3_Diff.png
 ┃ ┃ ┃ ┗ EM3_cl_uncl.png
 ┃ ┃ ┣ Pegasus
 ┃ ┃ ┃ ┣ Metric1
 ┃ ┃ ┃ ┃ ┣ .DS_Store
 ┃ ┃ ┃ ┃ ┗ EM1_Pegasus.png
 ┃ ┃ ┃ ┣ Metric2
 ┃ ┃ ┃ ┃ ┣ .DS_Store
 ┃ ┃ ┃ ┃ ┣ EM2_Pegasus_BART.png
 ┃ ┃ ┃ ┃ ┣ EM2_Pegasus_BART1.png
 ┃ ┃ ┃ ┃ ┣ EM2_Pegasus_BERT.png
 ┃ ┃ ┃ ┃ ┣ EM2_Pegasus_BERT1.png
 ┃ ┃ ┃ ┃ ┣ EM2_Pegasus_DAE.png
 ┃ ┃ ┃ ┃ ┣ EM2_Pegasus_DAE1.png
 ┃ ┃ ┃ ┃ ┣ EM2_Pegasus_Merged.png
 ┃ ┃ ┃ ┃ ┗ EM2_Pegasus_Merged1.png
 ┃ ┃ ┃ ┗ .DS_Store
 ┃ ┃ ┣ T5
 ┃ ┃ ┃ ┣ Metric1
 ┃ ┃ ┃ ┃ ┣ .DS_Store
 ┃ ┃ ┃ ┃ ┗ EM1_T5.png
 ┃ ┃ ┃ ┣ Metric2
 ┃ ┃ ┃ ┃ ┣ .DS_Store
 ┃ ┃ ┃ ┃ ┣ T5_BART.png
 ┃ ┃ ┃ ┃ ┣ T5_BART1.png
 ┃ ┃ ┃ ┃ ┣ T5_BERT.png
 ┃ ┃ ┃ ┃ ┣ T5_BERT1.png
 ┃ ┃ ┃ ┃ ┣ T5_DAE.png
 ┃ ┃ ┃ ┃ ┣ T5_DAE1.png
 ┃ ┃ ┃ ┃ ┣ T5_Merged.png
 ┃ ┃ ┃ ┃ ┗ T5_Merged1.png
 ┃ ┃ ┃ ┗ .DS_Store
 ┃ ┃ ┗ .DS_Store
 ┃ ┣ input_files
 ┃ ┃ ┣ EncDec
 ┃ ┃ ┃ ┣ .DS_Store
 ┃ ┃ ┃ ┣ EncDec_Bart_Dataset_AllScore_withGold.csv
 ┃ ┃ ┃ ┣ EncDec_Bert_Dataset_AllScore_withGold.csv
 ┃ ┃ ┃ ┣ EncDec_Dae_Dataset_AllScore_withGold.csv
 ┃ ┃ ┃ ┣ EncDec_baseline_Dataset_AllScore_withGold.csv
 ┃ ┃ ┃ ┗ EncDec_merged_Dataset_AllScore_withGold.csv
 ┃ ┃ ┣ Metric3
 ┃ ┃ ┃ ┣ all_scores_cleaned.csv
 ┃ ┃ ┃ ┣ all_scores_merged.csv
 ┃ ┃ ┃ ┗ all_scores_uncleaned.csv
 ┃ ┃ ┣ Pegasus
 ┃ ┃ ┃ ┣ Pegasus_Bart_Dataset_AllScore_withGold.csv
 ┃ ┃ ┃ ┣ Pegasus_Baseline_Dataset_AllScore_withGold.csv
 ┃ ┃ ┃ ┣ Pegasus_Bert_Dataset_AllScore_withGold.csv
 ┃ ┃ ┃ ┣ Pegasus_Dae_Dataset_AllScore_withGold.csv
 ┃ ┃ ┃ ┣ Pegasus_Merged_Dataset_AllScore_withGold.csv
 ┃ ┃ ┃ ┗ Pegasus_Merged_Dataset_AllScore_withGold_cleaned.csv
 ┃ ┃ ┣ T5
 ┃ ┃ ┃ ┣ T5_Bart_AllScores_withGold.csv
 ┃ ┃ ┃ ┣ T5_Baseline_AllScores_withGold.csv
 ┃ ┃ ┃ ┣ T5_Bert_AllScores_withGold.csv
 ┃ ┃ ┃ ┣ T5_Merged_AllScores_withGold.csv
 ┃ ┃ ┃ ┣ T5_Merged_AllScores_withGold_cleaned.csv
 ┃ ┃ ┃ ┗ T5_dae_AllScores_withGold.csv
 ┃ ┃ ┣ .DS_Store
 ┃ ┃ ┗ gold-scores-test.csv
 ┃ ┣ manual evaluation
 ┃ ┃ ┣ ErrorAnalysis_worstModel.csv
 ┃ ┃ ┗ Human_LLM_Evaluation_Annotated.csv
 ┃ ┣ .DS_Store
 ┃ ┣ README.md
 ┃ ┗ requirements.txt
 ┣ datasets
 ┃ ┣ final_training_data
 ┃ ┃ ┣ bart_score_dataset.csv
 ┃ ┃ ┣ baseline_dataset.csv
 ┃ ┃ ┣ bert_score_dataset.csv
 ┃ ┃ ┣ dae_score_dataset.csv
 ┃ ┃ ┗ merge_dataset.csv
 ┃ ┗ test_data
 ┃ ┃ ┗ test.csv
 ┣ factuality_checking
 ┃ ┣ dataset_selection
 ┃ ┃ ┣ BART_score
 ┃ ┃ ┃ ┣ code
 ┃ ┃ ┃ ┃ ┗ Compute_Bart_Score.ipynb
 ┃ ┃ ┃ ┗ output_files
 ┃ ┃ ┃ ┃ ┗ bart_dataset top15k.csv
 ┃ ┃ ┣ BERT_score
 ┃ ┃ ┃ ┣ code
 ┃ ┃ ┃ ┃ ┗ Compute_Bert_score.ipynb
 ┃ ┃ ┃ ┗ output_files
 ┃ ┃ ┃ ┃ ┗ bert_dataset_top15k.csv
 ┃ ┃ ┗ DAE_score
 ┃ ┃ ┃ ┣ code
 ┃ ┃ ┃ ┃ ┗ evaluate_factuality.py
 ┃ ┃ ┃ ┗ output_files
 ┃ ┃ ┃ ┃ ┗ dae_dataset_top15k.csv
 ┃ ┗ training_dataset_20k.csv
 ┣ models
 ┃ ┣ Enc-Dec
 ┃ ┃ ┣ evaluation
 ┃ ┃ ┃ ┣ BART
 ┃ ┃ ┃ ┃ ┣ Compute_Bart_Score.ipynb
 ┃ ┃ ┃ ┃ ┣ Enc-dec_bart_model_bart_score.csv
 ┃ ┃ ┃ ┃ ┣ Enc-dec_baseline_model_bart_score.csv
 ┃ ┃ ┃ ┃ ┣ Enc-dec_bert_model_bart_score.csv
 ┃ ┃ ┃ ┃ ┣ Enc-dec_dae_model_bart_score.csv
 ┃ ┃ ┃ ┃ ┗ Enc-dec_merged_model_bart_score.csv
 ┃ ┃ ┃ ┣ BERT
 ┃ ┃ ┃ ┃ ┣ Compute_Bert_score.ipynb
 ┃ ┃ ┃ ┃ ┣ Enc-dec_bart_model_bert_score.csv
 ┃ ┃ ┃ ┃ ┣ Enc-dec_baseline_model_bert_score.csv
 ┃ ┃ ┃ ┃ ┣ Enc-dec_bert_model_bert_score.csv
 ┃ ┃ ┃ ┃ ┣ Enc-dec_dae_model_bert_score.csv
 ┃ ┃ ┃ ┃ ┗ Enc-dec_merged_model_bert_score.csv
 ┃ ┃ ┃ ┗ DAE
 ┃ ┃ ┃ ┃ ┣ Enc-dec_bart_model_dae_score.csv
 ┃ ┃ ┃ ┃ ┣ Enc-dec_baseline_model_dae_score.csv
 ┃ ┃ ┃ ┃ ┣ Enc-dec_bert_model_dae_score.csv
 ┃ ┃ ┃ ┃ ┣ Enc-dec_dae_model_dae_score.csv
 ┃ ┃ ┃ ┃ ┣ Enc-dec_merged_dataset_dae_score.csv
 ┃ ┃ ┃ ┃ ┗ evaluate_factuality.py
 ┃ ┃ ┣ inference
 ┃ ┃ ┃ ┣ output_files
 ┃ ┃ ┃ ┃ ┣ bart_score_model_inference.csv
 ┃ ┃ ┃ ┃ ┣ baseline_model_inference.csv
 ┃ ┃ ┃ ┃ ┣ bert_score_model_inference.csv
 ┃ ┃ ┃ ┃ ┣ dae_score_inference.csv
 ┃ ┃ ┃ ┃ ┗ merged_model_inference.csv
 ┃ ┃ ┃ ┗ 685_Project_Enc_Dec_Training_Inference.ipynb
 ┃ ┃ ┗ training
 ┃ ┃ ┃ ┗ 685_Project_Enc_Dec_Training_Inference.ipynb
 ┃ ┣ Pegasus
 ┃ ┃ ┣ evaluation
 ┃ ┃ ┃ ┣ BART
 ┃ ┃ ┃ ┃ ┣ Compute_Bart_Score.ipynb
 ┃ ┃ ┃ ┃ ┣ pegasus_bart_model_bart_score.csv
 ┃ ┃ ┃ ┃ ┣ pegasus_baseline_model_bart_score.csv
 ┃ ┃ ┃ ┃ ┣ pegasus_bert_model_bart_score.csv
 ┃ ┃ ┃ ┃ ┣ pegasus_dae_model_bart_score.csv
 ┃ ┃ ┃ ┃ ┗ pegasus_merged_model_bart_score.csv
 ┃ ┃ ┃ ┣ BERT
 ┃ ┃ ┃ ┃ ┣ Compute_Bert_score.ipynb
 ┃ ┃ ┃ ┃ ┣ Pegasus_dae_dataset_bert_score.csv
 ┃ ┃ ┃ ┃ ┣ pegasus_bart_model_bert_score.csv
 ┃ ┃ ┃ ┃ ┣ pegasus_baseline_model_bert_score.csv
 ┃ ┃ ┃ ┃ ┣ pegasus_bert_model_bert_score.csv
 ┃ ┃ ┃ ┃ ┗ pegasus_merged_model_bert_score.csv
 ┃ ┃ ┃ ┗ DAE
 ┃ ┃ ┃ ┃ ┣ evaluate_factuality.py
 ┃ ┃ ┃ ┃ ┣ pegasus_bart_model_dae_score.csv
 ┃ ┃ ┃ ┃ ┣ pegasus_baseline_model_dae_score.csv
 ┃ ┃ ┃ ┃ ┣ pegasus_bert_model_dae_score.csv
 ┃ ┃ ┃ ┃ ┣ pegasus_dae_model_dae_score.csv
 ┃ ┃ ┃ ┃ ┗ pegasus_merged_model_dae_score.csv
 ┃ ┃ ┣ inference
 ┃ ┃ ┃ ┣ output_files
 ┃ ┃ ┃ ┃ ┣ bart_score_model_inference.csv
 ┃ ┃ ┃ ┃ ┣ baseline_model_inference.csv
 ┃ ┃ ┃ ┃ ┣ bert_score_model_inference.csv
 ┃ ┃ ┃ ┃ ┣ dae_score_model_inference.csv
 ┃ ┃ ┃ ┃ ┗ merged_model_inference.csv
 ┃ ┃ ┃ ┗ Pegasus_Inference.ipynb
 ┃ ┃ ┗ training
 ┃ ┃ ┃ ┗ Pegasus_Training.ipynb
 ┃ ┗ T5
 ┃ ┃ ┣ evaluation
 ┃ ┃ ┃ ┣ BART
 ┃ ┃ ┃ ┃ ┣ Compute_Bart_Score.ipynb
 ┃ ┃ ┃ ┃ ┣ T5_bart_model_bart_score.csv
 ┃ ┃ ┃ ┃ ┣ T5_baseline_model_bart_score.csv
 ┃ ┃ ┃ ┃ ┣ T5_bert_model_bart_score.csv
 ┃ ┃ ┃ ┃ ┣ T5_dae_model_bart_score.csv
 ┃ ┃ ┃ ┃ ┗ T5_merged_model_bart_score.csv
 ┃ ┃ ┃ ┣ BERT
 ┃ ┃ ┃ ┃ ┣ Compute_Bert_score.ipynb
 ┃ ┃ ┃ ┃ ┣ T5_bart_model_bert_score.csv
 ┃ ┃ ┃ ┃ ┣ T5_baseline_model_bert_score.csv
 ┃ ┃ ┃ ┃ ┣ T5_bert_model_bert_score.csv
 ┃ ┃ ┃ ┃ ┣ T5_dae_model_bert_score.csv
 ┃ ┃ ┃ ┃ ┗ T5_merged_model_bert_score.csv
 ┃ ┃ ┃ ┗ DAE
 ┃ ┃ ┃ ┃ ┣ T5_bart_model_dae_score.csv
 ┃ ┃ ┃ ┃ ┣ T5_baseline_model_dae_score.csv
 ┃ ┃ ┃ ┃ ┣ T5_bert_model_dae_score.csv
 ┃ ┃ ┃ ┃ ┣ T5_dae_model_dae_score.csv
 ┃ ┃ ┃ ┃ ┣ T5_merged_model_dae_score.csv
 ┃ ┃ ┃ ┃ ┗ evaluate_factuality.py
 ┃ ┃ ┣ inference
 ┃ ┃ ┃ ┣ output_files
 ┃ ┃ ┃ ┃ ┣ bart_score_model_inference.csv
 ┃ ┃ ┃ ┃ ┣ baseline_model_inference.csv
 ┃ ┃ ┃ ┃ ┣ bert_score_model_inference.csv
 ┃ ┃ ┃ ┃ ┣ dae_score_model_inference.csv
 ┃ ┃ ┃ ┃ ┗ merged_model_inference.csv
 ┃ ┃ ┃ ┗ All_datasets_inference.ipynb
 ┃ ┃ ┗ training
 ┃ ┃ ┃ ┗ T5-simplification.ipynb
 ┗ README.md