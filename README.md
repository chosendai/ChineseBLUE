# ChineseBLUE, the Chinese Biomedical Language Understanding Evaluation benchmark
 
Work in progress

## Introduction

Chinesse BLUE benchmark consists of  different biomedicine text-mining tasks with  corpora.
These tasks cover a diverse range of text genres (biomedical web data and clinical notes), dataset sizes, and degrees of difficulty and, more importantly, highlight common biomedicine text-mining challenges.

## Tasks

| Corpus          | Train |  Dev | Test | Task                    | Metrics             | Domain     |
|-----------------|------:|-----:|-----:|-------------------------|---------------------|------------|
| CEMRNER*        |    |    |   | Name Entity Recognition    | F1             | Clinical   |
| CMedQANER          |    |    |   | Name Entity Recognition    | F1             | Medical   |
| CMedQQ*        |    |    |   | Sentence Similarity    | F1             | Medical   |
| CMedQA        |    |    |   | Sentence Similarity    | F1             | Medical   |
| CMedQSA       |    |    |   | Sentence Similarity    | F1             |Medical    |
| CMedQT       |    |    |   | Information Rerival    |            |Medical    |
| CMedQR       |    |    |   |  Sentence Classification   |        F1      | Medical   |
| CMedQC       |    |    |   |  Sentence Classification   |       F1       | Medical   |
| CMedSQC*       |    |    |   |   Sentence Classification  |       F1       | Medical   |

** Those dataset are not publicy available now because of privcy issues and will be released as soon as possible. 


### Named entity recognition


### Sentence similarity

 
### Document multilabel classification


### Relation extraction
To be come soon. 




### Inference task
To be come soon. 

### Datasets

All datasets can be downloaded at []()

### Pretrained Model

All pretrained model can be downloaded at [C-BERT](). 

## Baselines

To be come soon. 

### Fine-tuning with BERT

Code to be released soon. 

## Citing Chinese BLUE

*  Ningyu Zhang, Qianghuai Jia, Kangping Yin, Liang Dong, Feng Gao, Nengwei Hua. [Conceptualized Representation Learning for ChineseBiomedical Text]()

```
@InProceedings{zhang2019cbert,
  author    = {Ningyu Zhang, Qianghuai Jia, Kangping Yin, Liang Dong, Feng Gao, Nengwei Hua},
  title     = {Conceptualized Representation Learning for ChineseBiomedical Text},
  booktitle = {},
  year      = {2019},
}
```

## Acknowledgments

We are also grateful to the authors of BERT to make the data and codes publicly available. 

## Disclaimer
This project is not the official product of Alibaba. The information produced on this website is not intended for direct diagnostic use or medical decision-making without review and oversight by a clinical professional. Individuals should not change their health behavior solely on the basis of information produced on this website.   If you have questions about the information produced on this website, please see a health care professional. 

The experimental results presented in the technical report only indicate the performance under the specific data set and super-parameter combination, and do not represent the essence of each model. The experimental results may change due to random number seeds and computing devices. The content of this project is for technical research purposes only and is not intended to be a conclusive basis. The user may use the model arbitrarily within the scope of the license, but we are not responsible for any direct or indirect damages resulting from the use of the content of the project.
