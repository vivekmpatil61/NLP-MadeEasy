#importing appropriate libraries
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import streamlit as st
import spacy
import en_core_web_sm
import pandas as pd
from PIL import Image
from modules.scrape import *
from textblob import TextBlob
from matplotlib.backends.backend_agg import RendererAgg
_lock = RendererAgg.lock


def get_wordcloud(text):
    '''
    This method creates the visually beautiful wordcloud using the words from the corpus.
    Most frequent word (after removing stop words), gets bigger in the wordcloud
    '''
    wordcloud = WordCloud(max_font_size=200,width=1200, height=600, max_words=100, random_state =101,
                          stopwords=set(STOPWORDS),background_color="white").generate(text)
    with _lock:
        plt.figure()
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()
        st.pyplot()

@st.cache
#We use cache in streamlit so that once the website loads, all data is stored in cache so next refresh will be fast with data access and data loading tasks
def text_analyzer(my_text):
    '''
    This function gives you token (word) and it's lemma (canonical form, dictionary form, or citation form of a set of words)
    '''
    nlp = en_core_web_sm.load()
    docx = nlp(my_text)
    allData = [('"Token":{},\n"Lemma":{}'.format(token.text,token.lemma_))for token in docx ]
    return allData

# Function for pos tagging
@st.cache
def pos_tagging(my_text):
    '''
    A Part-Of-Speech Tagger (POS Tagger) reads text in language and assigns parts of speech to each word (and other tokens)
    '''
    data ={}
    nlp = en_core_web_sm.load()
    doc = nlp(my_text)
    c_tokens = [token.text for token in doc]
    c_pos = [token.pos_ for token in doc]
    new_df = pd.DataFrame(zip(c_tokens,c_pos),
    columns=['Tokens', 'POS'])
    return new_df

def main():
    '''
    main  function
    '''
    st.title('Basic NLP')
    data = st.text_area("Enter Text Data","Type here..")
    data = data.strip()
    if st.checkbox('Show Tokens and Lemma'):
            message = data
            nlp_result = text_analyzer(message)
            st.json(nlp_result)

    if st.checkbox('Show Parts of Speech'):
        st.subheader('POS tagging on your text')
        message = data
        nlp_result = pos_tagging(message)
        st.dataframe(nlp_result)

    if st.checkbox('Correct spelling mistakes within the text data'):
        message = TextBlob(data)
        message = message.correct()
        st.code(message)


    if st.checkbox('Show Word Cloud', key='cloud'):
        message = data
        get_wordcloud(message)
