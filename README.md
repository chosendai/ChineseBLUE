# ChineseBLUE, the Chinese Biomedical Language Understanding Evaluation benchmark
 

## Introduction

Chinesse BLUE benchmark consists of five different biomedicine text-mining tasks with ten corpora.
Here, we rely on preexisting datasets because they have been widely used by the BioNLP community as shared tasks.
These tasks cover a diverse range of text genres (biomedical literature and clinical notes), dataset sizes, and degrees of difficulty and, more importantly, highlight common biomedicine text-mining challenges.

## Tasks

| Corpus          | Train |  Dev | Test | Task                    | Metrics             | Domain     |
|-----------------|------:|-----:|-----:|-------------------------|---------------------|------------|
| CEMRNER*        |    |    |   | Name Entity Recognition    | F1             | Clinical   |
| CMedQANER          |    |    |   | Name Entity Recognition    | F1             | Medical   |
| CMedQQMatch*        |    |    |   | Sentence Similarity    | F1             | Medical   |
| CMedQAMatch        |    |    |   | Sentence Similarity    | F1             | Medical   |
| CMedQSAMatch        |    |    |   | Sentence Similarity    | F1             |Medical    |
| CMedQR       |    |    |   |     |        MSE      | Medical   |
| CMedQC       |    |    |   |     |       F1       | Medical   |
| CMedSQC*       |    |    |   |     |       F1       | Medical   |
| CMedBaikeC       |    |    |   |     |      F1        | Medical   |
* Those dataset are not publicy avaible now because of privcy issues and will be released as soon as possible. 

### Sentence similarity
 

### Named entity recognition



### Relation extraction
To do 


### Document multilabel classification

 

### Inference task

 

### Datasets

All datasets can be downloaded at []()

### Pretrained Model

All pretrained model can be downloaded at [C-BERT](). 

## Baselines

| Corpus          | Metrics | SOTA* | BERT | C-BERT | 
|-----------------|--------:|------:|-----:|--------:|
| CMedNER          |  |   | |    |  


### Fine-tuning with BERT

Code to be released. 

## Citing Chinese BLUE

*  Ningyu Zhang, Qianghuai Jia, Kangping Yin, Liang Dong, Feng Gao, Nengwei Hua. []()

```
@InProceedings{zhang2019cbert,
  author    = {},
  title     = {},
  booktitle = {},
  year      = {2019},
}
```

## Acknowledgments

We are also grateful to the authors of BERT to make the data and codes publicly available. 

## Disclaimer
This project is not the official product of Alibaba. The information produced on this website is not intended for direct diagnostic use or medical decision-making without review and oversight by a clinical professional. Individuals should not change their health behavior solely on the basis of information produced on this website.   If you have questions about the information produced on this website, please see a health care professional. 

The experimental results presented in the technical report only indicate the performance under the specific data set and super-parameter combination, and do not represent the essence of each model. The experimental results may change due to random number seeds and computing devices. The content of this project is for technical research purposes only and is not intended to be a conclusive basis. The user may use the model arbitrarily within the scope of the license, but we are not responsible for any direct or indirect damages resulting from the use of the content of the project.
