# ChineseBLUE, the Chinese Biomedical Language Understanding Evaluation benchmark

[![HitCount](http://hits.dwyl.io/zxlzr/https://githubcom/AliMedical/Chinese_BLUE_Benchmark.svg)](http://hits.dwyl.io/zxlzr/https://githubcom/AliMedical/Chinese_BLUE_Benchmark)
## Introduction

ChinesseBLUE benchmark consists of different biomedicine text-mining tasks with corpora.
These tasks cover a diverse range of text genres (biomedical web data and clinical notes), dataset sizes, and degrees of difficulty and, more importantly, highlight common biomedicine text-mining challenges.

C-BERT is a novel conceptualized representation learning approach. First, we use a different mask generation procedure to mask spans of tokens, rather than only random ones. We also introduce two kinds of masking strategies, namely whole entity masking and whole span masking.  Finally, C-BERT split the input document into segments based on the actual "sentences" provided by the user as positive samples and sample random sentences from other documents as negative samples for the next sentence prediction.  

![c-bert model](figs/c_bert_model.jpg)


## Tasks

| Dataset          | Train |  Dev | Test | Task                    | Metrics             | Domain     |
|-----------------|------:|-----:|-----:|-------------------------|---------------------|------------|
| [cEHRNER](https://raw.githubusercontent.com/AliMedical/Chinese_BLUE_Benchmark/master/data/cEHRNER/cEHRNER.tar.gz) |  915  | 44   | 41  | Name Entity Recognition    | F1             | Clinical   |
| [cMedQANER](https://raw.githubusercontent.com/AliMedical/Chinese_BLUE_Benchmark/master/data/cMedQANER/cMedQANER.tar.gz)         |  800  | 100   | 100  | Name Entity Recognition    | F1             | Medical   |
| [cMedQQ](https://raw.githubusercontent.com/AliMedical/Chinese_BLUE_Benchmark/master/data/cMedQQ/cMedQQ.tar.gz) | 20K   | 5K   | 5K  | Paraphrase Identification   | F1             | Medical   |
| [cMedQNLI](https://raw.githubusercontent.com/AliMedical/Chinese_BLUE_Benchmark/master/data/cMedQNLI/cMedQNLI.tar.gz) |  80K  |  10K  |10K   | Question Natural Language Inference  | F1             | Medical   |
| [cMedQA](https://raw.githubusercontent.com/AliMedical/Chinese_BLUE_Benchmark/master/data/cMedQA/cMedQA.tar.gz) | 10M   | 800K   | 800K | Question Answering    | F1             |Medical    |
| [cMedIR](https://raw.githubusercontent.com/AliMedical/Chinese_BLUE_Benchmark/master/data/cMedIR/cMedIR.tar.gz) |  80K  |  10K  | 10K  | Information Rerival    |     MRR       |Medical    |
| [cMedIC](https://raw.githubusercontent.com/AliMedical/Chinese_BLUE_Benchmark/master/data/cMedIC/cMedIC.tar.gz) |  1000  |  200  | 200  |  Intent Classification   |        F1      | Medical   |
| [cMedTC](https://raw.githubusercontent.com/AliMedical/Chinese_BLUE_Benchmark/master/data/cMedTC/cMedTC.tar.gz) | 20K   | 1K   | 1K  |  Sentence Classification   |       F1       | Medical   |
| [CMDD](http://www.sdspeople.fudan.edu.cn/zywei/data/emnlp2019-cmdd.zip) | 1240 | 412 | 412 | Symptom Diagnosis |       F1       | Dialogue |


### Named Entity Recognition (NER) 

Named entity recognition aims to recognize various entities, including diseases, drugs, syndromes, etc.   The **cEHRNER** dataset labeled from the Chinese electronic health records and the **cMedQANER** dataset labeled from Chinese community question answering is chosen.

### Paraphrase Identification (PI)

Paraphrase Identification aims to identify whether two sentences express the same meaning. We use **cMedQQ**, which consists of search query pairs. 

### Question Natural Language Inference (QNLI)

Question natural language inference aims to identify   whether the answer corresponds to the question in the question-answering pair.  We use **cMedQNLI**, which consists of question-answer pairs. 

### Question Answering (QA)

Question answering can be approximated as ranking candidate answer sentences based on their similarity. We assign 0,1 labels to the QA pairs, which convert to the binary classification problem. We use **cMedQA**  released from the paper  "[Multi-Scale Attentive Interaction Networks for Chinese Medical Question Answer Selection](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8548603)", which consists of questions and their answers.

### Information  Retrieval (IR)

Information retrieval aims to retrieve most related documents given search queries. IR can be regarded as a ranking task.   We use the **cMedIR** dataset,  which consists of queries with multiple documents and their relative scores. 

### Intent Classification (IC)

Intent classification aims to assign intent labels to the queries, which can be regarded as multiple label classification tasks. We use the **cMedIC** dataset, which consists of queries with three intent labels (e.g., no intention, weak intention, and firm intention).

### Text Classification (TC)

Text classification aims to assign multiple labels to the sentence. We use the **cMedTC** dataset, which consists of biomedical texts with multiple labels.

### Symptom Diagnosis 

Symptom diagnosis is a challenging yet profound problem in natural language processing. We use the **CMDD** dataset released from the paper"[Enhancing Dialogue Symptom Diagnosis with Global Attention and Symptom Graph](https://www.aclweb.org/anthology/D19-1508.pdf)".

### Relation extraction (RE)
Coming soon. 

### Datasets

All datasets can be downloaded at [ChineseBLUE1.0](https://raw.githubusercontent.com/AliMedical/Chinese_BLUE_Benchmark/master/data/ChineseBLUE.tar.gz)

### Pretrained Model

All pre-trained models can be downloaded at [C-BERT](). 

## Citing Chinese BLUE

Paper will be released soon.

*  [Ningyu Zhang](https://zxlzr.github.io), Qianghuai Jia, Kangping Yin, Liang Dong, Feng Gao, Nengwei Hua. [Conceptualized Representation Learning for Chinese Biomedical Text]()

```
@InProceedings{zhang2019cbert,
  author    = {Ningyu Zhang, Qianghuai Jia, Kangping Yin, Liang Dong, Feng Gao, Nengwei Hua},
  title     = {Conceptualized Representation Learning for Chinese Biomedical Text},
  booktitle = {},
  year      = {2019},
}
```

## Acknowledgments

We are also grateful to the authors of [BERT](https://github.com/google-research/bert)  and [wwm-BERT](https://github.com/ymcui/Chinese-BERT-wwm)  to make the data and codes publicly available. We are also grateful to the authors of paper "[Enhancing Dialogue Symptom Diagnosis with Global Attention and Symptom Graph](https://www.aclweb.org/anthology/D19-1508.pdf)"  and  "[Multi-Scale Attentive Interaction Networks for Chinese Medical Question Answer Selection](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8548603)"  who released the dataset [CMDD](http://www.sdspeople.fudan.edu.cn/zywei/data/emnlp2019-cmdd.zip) and [cMedQA2](https://github.com/zhangsheng93/cMedQA2). 


## Disclaimer
This project is not the official product of Alibaba. The information produced on this website is not intended for direct diagnostic use or medical decision-making without review and oversight by a clinical professional. Individuals should not change their health behavior solely on the basis of information produced on this website.   If you have questions about the information produced on this website, please see a health care professional. 

The experimental results presented in the technical report only indicate the performance under the specific data set and super-parameter combination and do not represent the essence of each model. The experimental results may change due to random number seeds and computing devices. The content of this project is for technical research purposes only and is not intended to be a conclusive basis. The user may use the model arbitrarily within the scope of the license, but we are not responsible for any direct or indirect damages resulting from the use of the content of the project.
