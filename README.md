<h1 align="center">
  <img src="https://sourceessay.com/essay/wp-content/uploads/2018/07/demonstration-767983_1920-e1532070341714.jpg" alt="MOVIE REVIEWER"><br>
  Movie Reviewer System
</h1>

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](https://github.com/Manimaran-SM/Movie_Reviewer_System/blob/master/LICENSE)

* [Overview](#Overview)
   * [Introduction](#Introduction)
   * [Why?](#Why_this_Algorithm)
   * [Challenges Faced](#Challenges_Faced)
   * [Limitation](#Limitation)
   
* [Guide](#Guide)
  * [Procedure](#Procedure)
  * [Pre-requisite](#Prerequisite)
  * [Dataset](#Dataset)


# Overview:
## Introduction
>Fake news is a major concern in our society right now. It has gone hand-in-hand with the rise of the data-driven era – not a coincidence when you consider the sheer volume of data we are generating every second! Fake news is such a widespread issue that even the world’s leading dictionaries are trying to combat it in their own way.
>I’ve been working in the Machine learning (ML) space and so i proposed a system which would analyze the fake news using classification algorithm and report it back 

## Why_this_Algorithm
  >I used Passive Aggressive Classifier. Passive-aggressive classification is one of the available incremental learning algorithms and it is very simple to implement, since it has a closed-form update rule.
  >refer this for detailed description [passive_aggressive_classifier](https://www.bonaccorso.eu/2017/10/06/ml-algorithms-addendum-passive-aggressive-algorithms/)
  >Here is another key term text "Term frequency and inverse document frequency". 
  <br>Term Frequency measures the frequency of a word in a document. This highly depends on the length of the document and the generality of word. 
  <br>```tf(t,d) = count of t in d / number of words in d ```
  <br>DF is the number of documents in which the word is present. IDF is the inverse of the document frequency which measures the informativeness of term t.
  <br>```df(t) = occurrence of t in documents```
  <br>```idf(t) = N/df```
  

## Challenges_Faced
  >I found it hard working with the data extraction feature. Since the version varied it kind of affected the required accuracy of the system.
  >Kindly refer this documentation [TFIDFVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html) and understand the parameters before using it in your system. 


## Limitation
  >* This system cannot accept inputs from user. 
  >* It is not compatable for deploying.
  >* It also requires much more understanding of the dataset
  

# Guide:
## Procedure
>* Click clone/download
>* If you github desktop click open in desktop hit the clone button. 
>* If you use download zip, then extract the zip file  
>* If you want to use HTTPS say (https://github.com/Manimaran-SM/Fake_News_Detection.git),  then use the command
``` 
$ git clone https://github.com/Manimaran-SM/Fake_News_Detection.git
```
### Note:
* If you have problem related with git command refer this documentation [link](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository)
>* After completing the above steps, You must have anaconda or jupyter notebook to execute this code.
>* Now run the [file1.pynb](https://github.com/Manimaran-SM/Fake_News_Detection/blob/master/file1.ipynb) file. You wil get output as shown in the above file.
>* If you have any problems regarding this repository while opening feel free ask me [here](https://github.com/Manimaran-SM/Fake_News_Detection/issues/new)

## Prerequisite
Install Numpy with:

```
pip install numpy
```
Install Pandas with:

```
pip install pandas
```
Install Sklearn with:

```
pip install scikit-learn
```
Install Pickle with:

```
pip install pickle
```
Install nltk with:

```
pip install nltk
```
## Note:
>* python IDE and Following packages must be installed in system:
>* Given commands works only for windows
>* pip install pickle not required for python v3.7 for sure    

## Dataset

>Refer in this repostory or click here [dataset](http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz)
