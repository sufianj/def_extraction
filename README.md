# Extracting Definienda in Mathematical Scholarly Articles with~Transformers



This repository containes the datasets, codes and experimental results of our paper: "Extracting Definienda in Mathematical Scholarly Articles with~Transformers" (link of the PDF to be appeared).

If you have no access to our ArXiv papers store, you may start from Step 2.

## Step 0. Collect .tex sources of ArXiv papers

"get_paper_IDs.ipynb" pulls ArXiv IDs of paper in combinatoric category and stores the IDs to a csv file "28477_id+dir.csv".

Then you need to run "get_paper_list.sh" ( make sure that "28477_id+dir.csv", "get_paper.sh" and "add_extthm.py" are copied to the same repository ) on the server where you store the ArXiv paper sources to copy the .tex files to a folder "que_tex/".


## Step 1. Extract definition-definiendum pairs from .tex files

Always on the same server as in raw data collection step, run "python get_def-term_pairs.py que_tex out_def_all.csv" to print the definitions in all the .tex to a single .csv "out_def_all.csv". 

## Step 2. Clean the dataset

Run "prepare_term-def_dataset.ipynb" to clean the noises in extracted definition-definiendum pairs and generate IOB-format dataset for named entity recognition. If you start with this step, you can load "out_def_all_1007.csv".


## Step 3.

### Fine-tune pre-trained language models for token classification:

You may run the following notebooks with our labeled data in "data/":

- RobertaForTokenCLS.ipynb
- CCRobertaForTokenCLS.ipynb
- SciBERTForTokenCLS.ipynb

Transformer's native evaluation of our experiments can be found in "finetuning_results".
Our fine-tuned models are available here: https://huggingface.co/InriaValda (todo)


### Ask ChatGPT to extract definienda with your own API KEY:

- Ask_ChatGPT_to_Extract.ipynb 

Our results on the test set can be found in "GPT_results/Human_corrected_annotations+gpt_res.csv"

## Step 4. Evaluation

Run "Eval_Finetuning_10-fold.ipynb" to align fine-tuned models' predictions with ChatGPT's answers. 
Our experimental results are in "GPT_results/".


