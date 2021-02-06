#importing appropriate libraries
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import punkt
from gensim import corpora
from gensim import models
import gensim
import pyLDAvis.gensim
import re
import streamlit as st
import pandas as pd
from modules.scrape import *
from textblob import TextBlob
import sys
from matplotlib import pyplot as plt

import spacy
from spacy import displacy
import en_core_web_sm
from spacy import load

#Entity Analyzer funnction
def entity_analyzer(my_text):
    '''
    This function analyzes etities associated with give text
    using en_core_web_sm module within powerful SpaCy NLP library
    '''
    nlp = en_core_web_sm.load()
    docx = nlp(my_text)
    tokens = [token.text for token in docx]
    entities = [(entity.text, entity.label_)for entity in docx.ents]
    allData = ['"Token":{},\n"Entities":{}'.format(tokens, entities)]
    return allData

def ner(my_text):
    '''
    This function displays entities in html format with
    appropriate color coding
    '''
    nlp = en_core_web_sm.load()
    doc = nlp(my_text)
    html = displacy.render([doc], style="ent", page=False)
    st.markdown(html, unsafe_allow_html=True)
    st.markdown(" <br> </br>", unsafe_allow_html= True)

def process_text(text):
    '''
    This function uses power of regex to clean the corpus, remove non english characters,
    then it tokenizes each word by removing stop words like 'is','the','an' etc and returns clean text
    '''
    text = re.sub('[^A-Za-z]', ' ', text.lower())
    tokenized_text = word_tokenize(text)
    clean_text = [word for word in tokenized_text if word not in stopwords.words('english')]
    return clean_text


def main():
    '''
    This is main function
    '''
    st.title('Named Entity Recognition and Topic Modelling ')
    data = st.text_area("Eter Text Data","Type here..")
    data = data.strip()
    if st.button('Show Named Entities'):
        st.subheader('NER Plot')
        message = data
        ner(message)
