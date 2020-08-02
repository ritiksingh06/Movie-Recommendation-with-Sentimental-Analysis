#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import pickle
#import streamlit as st


# In[2]:
#st.write("""
# > Welcome to My Site
#""")

file=pd.read_csv("Modified_main_data.csv")
ri_model=pickle.load(open("nlp_model.pkl","rb"))
vectorizer=pickle.load(open("tranform.pkl","rb"))
file.set_index("movie_title",inplace=True)
data=pd.read_csv("main_data.csv")
data.set_index("movie_title",inplace=True)


# In[ ]:





# In[3]:


count=CountVectorizer()
c_marix=count.fit_transform(file["Words"])
indexs=pd.Series(file.index)


# In[4]:


cos_similarity=cosine_similarity(c_marix,c_marix)
cos_similarity


# In[5]:


def recommend(movie,cos_similarity=cos_similarity):
    recommend_movie=[]
    ind=indexs[indexs==movie].index[0]
    similar=pd.Series(cos_similarity[ind]).sort_values(ascending=False)
    top_20_similar=list(similar.iloc[1:21].index)
    for i in top_20_similar:
        recommend_movie.append(list(file.index)[i])
    return recommend_movie,top_20_similar,ind


# In[6]:


def rec_from_rev(arr):
    recommend=[]
    movie_review=np.array(arr)
    movie_vector=vectorizer.transform(movie_review)
    prediction=ri_model.predict(movie_vector)
    for i in range(len(prediction)):
        if prediction[i]==1:
            recommend.append(arr[i])
    return recommend


# In[7]:
def remove_irrelevent_index(rec,recommended_movie,inde):
    for i in range(len(rec)):
        if rec[i] not in recommended_movie:
            inde.pop(i)
    return inde


# rec,inde=recommend("the tax collector")


# In[8]:


# recommend=rec_from_rev(rec)


# In[9]:


# movie_detail=data.loc[recommend,:]
# print(movie_detail)
#st.write("""
# DONE
#""")


# In[ ]:




