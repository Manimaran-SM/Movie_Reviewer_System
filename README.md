<h1 align="center">
  <img src="https://sourceessay.com/essay/wp-content/uploads/2018/07/demonstration-767983_1920-e1532070341714.jpg" alt="MOVIE REVIEWER"><br>
  Movie Reviewer System
</h1>

![Python](https://img.shields.io/badge/Python-3.8-blueviolet)
![Framework](https://img.shields.io/badge/Framework-Flask-red)
![Frontend](https://img.shields.io/badge/Frontend-HTML/CSS/JS-green)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](https://github.com/Manimaran-SM/Movie_Reviewer_System/blob/master/LICENSE)

* [Overview](#Overview)
   * [Introduction](#Introduction)
   * [Why?](#Why_this_Algorithm)
   * [Challenges Faced](#Challenges_Faced)
   * [Limitation](#Limitation)
   
* [Guide](#Guide)
  * [System Configuration](#System_Configuration)
  * [Procedure](#Procedure)
  * [Pre-requisite](#Prerequisite)
  * [Dataset](#Dataset)
  


# Overview:
## Introduction
  >* Movie reviewer system is quite different from all other system related to movies.It gets input from user in form of text of any length and predicts the output as positive or negative. It also provides an additional feature based on the given dataset, it can give the correctness of the prediction. It gets the input from the user processes it using Hashing vectorizer and converts it to matrix of token occurences.
  >* [NLTK.corpus.stopwords](https://www.geeksforgeeks.org/removing-stop-words-nltk-python/) comes into play in removing words from the processed data which are considered to be useless. we would not want these words to take up space in our system, or taking up valuable processing time. [Flask](https://flask.palletsprojects.com/en/1.1.x/) enables it to become a web application in which the user can interact. 

## Why_this_Algorithm
  >* I used SGD Classifier([Stochastic Gradient Descent](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html)) due to its simplicity and ease of implementation and also It has been considered as the efficient algorithm for training models related to Text classification. It supports multiple loss function and more suitable for training a model.
  >* It also includes concept of natural language processing such as [hashingvectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html) due to its ability to apply a hashing function to term frequency counts in each document. Moreover you can ask i could've chose tfidfvectorizer instead, but due to dataset an d problem domain constraints, I didn't chose tfidfvectorizer for the following reason tfidf scales those term frequency counts in each document by penalising terms that appear more widely across the corpus. 
  

## Challenges_Faced
  >* First and foremost thing is that you have to install all necessary IDE's, packages, etc..,.
  >* It is hard working with the dataset and i managed it to do so and that instructions will be directed in [procedures](#procedure).
  >* Time to compile every part of the code using for loop and training part takes more time depending on your system processor. It is mandatory that you stay patient still it gets fully compiled. There is a high chances in overloading your RAM if it is 2Gb or lesser.
  >* Regular expresion generation is pretty much a complicated task it is done to eliminate the emoticons or expression from the text. 
  >* Do refer flask documentation affixed above before running [app.py](https://github.com/Manimaran-SM/Movie_Reviewer_System/blob/master/app.py) file
  >* This system being a heavy project cannot be deployed globally due to drawback of dataset.
  >* Kindly refer this documentation linked above in blue text and understand the parameters and concepts before using it in your system. 


## Limitation
  >* The collisions can introduce too much noise in the data and degrade prediction quality. There is no easy way to inverse the mapping and find the feature names from the feature index.
  >* SGD requires a number of hyperparameters such as the regularization parameter and the number of iterations. SGD is very sensitive to feature scaling.
  
  
# Guide:

## System_Configuration
>* Graphic card: NVIDIA GeForce GTX1050
>* CPU: Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
>* RAM: 8GB
>* Disksapce: 1TB


## Procedure
>* Click clone/download
>* If you github desktop click open in desktop hit the clone button. 
>* If you use download zip, then extract the zip file  
>* If you want to use HTTPS say (https://github.com/Manimaran-SM/Movie_Reviewer_System.git),  then use the command
``` 
$ git clone https://github.com/Manimaran-SM/Movie_Reviewer_System.git
```
>* After completing the above steps, You must have anaconda or jupyter notebook to execute this code.
>* I will be explaining the procedures for jupyter notebook both follows same instruction, Open jupyter notebook, your default browser opens up ], Navigate to your local repository containing this project.
>* Once you are there, first open and run the [movieclassifier.ipynb](https://github.com/Manimaran-SM/Movie_Reviewer_System/blob/master/movie_classifier.ipynb) file. Second,  open and run the [pandadataframe.ipynb](https://github.com/Manimaran-SM/Movie_Reviewer_System/blob/master/Panda_data_frame.ipynb) file. finally, go to the windows explorer open folder containing the [app.py](https://github.com/Manimaran-SM/Movie_Reviewer_System/blob/master/app.py) file. open the file You will get a link like this http://127.0.0.1:5000/ . copy paste this to your browser and give your input and check for output.
>* If you have any problems regarding this repository or while opening or while running the files, feel free ask me [here](https://github.com/Manimaran-SM/Movie_Reviewer_System/issues/new) with the issues you are facing.
## Sample outputs:
<p align="center"><img src="https://github.com/Manimaran-SM/Movie_Reviewer_System/blob/master/sampleoutput1.png" width="1000" height="500"><br><img src="https://github.com/Manimaran-SM/Movie_Reviewer_System/blob/master/sampleoutput2.png" width="1000" height="500">
</p>

### Note:
* If you have problem related with git command refer this documentation [link](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository)

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
Install flask with:

```
pip install flask
```
## Note:
>* Python IDE and Following packages must be installed in system:
>* Given commands works only for windows
>* pip install pickle not required for python v3.7 or above    

## Dataset

>* Refer in this repostory or click here [dataset](http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz). It just holds the text reviews from various sites under a single .tarz file

