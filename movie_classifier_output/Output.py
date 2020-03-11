import re,os,pickle
import numpy as np
from vectorizer import vect
clf=pickle.load(open(os.path.join('pkl_objects','classifier.pkl'),'rb'))
label = {0:'negative', 1:'positive'}

def predict(example):
    example=list(example)
    X = vect.transform(example)
    Prediction=label[clf.predict(X)[0]]
    percentage=np.max(clf.predict_proba(X))*100
    return Prediction,percentage
