#importing appropriate libraries
import streamlit as st
from modules.scrape import *

def main():
    st.success('''Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between computers and human language,
    in particular how to program computers to process and analyze large amount of natural language data.''')

    st.info('''This is a NLP MadeEasy Super App which provides interactive way to play with few NLP tasks. This web app is implemented using state-of-the art NLP methods and it is built over powerfulstreamlit framework.''')
    st.header('Features')
    st.markdown("""
    #### Basic NLP Tasks:
    + In this section, app covers the most basic NLP tasks of tokenisation, parts of speech tagging, correcting spellings in the sentences and a fancy way
    of showcasing natural language data using the WordCloud.
    #### Named Entity Recognition (NER):
    + Named-entity recognition (NER) (also known as entity identification, entity chunking, and entity extraction) is a subtask of information extraction that seeks to locate and classify named entities mentioned in unstructured text into pre-defined categories such as person names,
    organizations, locations, medical codes, time expressions, quantities, monetary values, percentages, etc.
    #### Text Summarization:
    + Automatic summarization is the process of shortening a set of data computationally, to create a subset that represents the most important or relevant information within the original content. This tool has options two extractive summarizers - Gensim and Sumy.
    #### Machine Translations:
    + Machine translation (MT) is an automatic translation from one language to another. Here, we have used English as a source laguage. The benefit
    of machine translation is that it is possible to translate large swathes of text in a very short time. It uses state of the art deep learning powered library to translate texts into multiple other lagugages.
    #### Sentiment Analysis
    + Sentiment analysis (or opinion mining) is a natural language processing technique used to determine whether data is positive, negative or neutral. Sentiment analysis is often performed on textual data to help businesses monitor brand and
    product sentiment in customer feedback, and understand customer needs.
    """)
