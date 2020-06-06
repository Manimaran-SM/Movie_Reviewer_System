#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import os
import pickle
import numpy as np
from sklearn.feature_extraction.text import HashingVectorizer


# In[2]:


def predict(example):
    example=list(example)
    X = vect.transform(example)
    prediction=label[clf.predict(X)[0]]
    percentage=np.max(clf.predict_proba(X))*100
    return prediction,percentage


# In[3]:


def tokenizer(text):
    text = re.sub('<[^>]*>', '', text)
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)',
                           text.lower())
    text = re.sub('[\W]+', ' ', text.lower())                    + ' '.join(emoticons).replace('-', '')
    tokenized = [w for w in text.split() if w not in stop]
    return tokenized


# In[4]:


cur_dir = os.getcwd()
stop = pickle.load(open(os.path.join(cur_dir,'stopwords.pkl'),'rb'))
vect = HashingVectorizer(decode_error='ignore',n_features=2**21, preprocessor=None,tokenizer=tokenizer)


# In[5]:


clf=pickle.load(open(os.path.join('classifier.pkl'),'rb'))
label = {0:'negative', 1:'positive'}


# In[6]:


example = ['Tired of sobby melodramas and stupid comedies? Why not watch a film with a difference? American Beauty by Sam Mendes is both a drama and a comedy, which definitely absorbed the best features of the genres, creating a powerful and mind-boggling cocktail of love, hatred, sinful passion, rebellion, loneliness, fear and total liberation.']
X = vect.transform(example)


# In[7]:


print('Prediction: %s \nProbability: %.2f%%' %(label[clf.predict(X)[0]], 
                                   np.max(clf.predict_proba(X))*100))

