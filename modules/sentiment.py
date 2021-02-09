#importing appropriate libraries
import streamlit as st
#NLP Pkgs
import nltk
from nltk.stem import PorterStemmer
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import sentiwordnet as swn
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import word_tokenize,pos_tag

def tokenize(aString):
    '''
    Function to tokenize given input
    '''
    a = word_tokenize(aString)
    return a


def cal_score(array_of_lemma_tag_for_a_comment):
    '''
    This function returns the polarity of the statement using NLTK library's submodule sentiwordnet.
    This module is developed using deeplearning techniques over a large set of labelled data.
    '''
    alist = [array_of_lemma_tag_for_a_comment]
    totalScore = 0
    count_words_included = 0
    for word in array_of_lemma_tag_for_a_comment:
        synset_forms = list(swn.senti_synsets(word[0], word[1]))
        if not synset_forms:
            continue
        synset = synset_forms[0]
        totalScore = totalScore + synset.pos_score() - synset.neg_score()
        count_words_included = count_words_included +1
    final_dec = ''
    if count_words_included == 0:
        final_dec = 'N/A'
    elif totalScore == 0.0:
        final_dec = 'Neutral'
    elif float(totalScore/count_words_included) < 0:
        final_dec = 'Negative'
    elif float(totalScore/count_words_included) > 0:
        final_dec = 'Positive'
    return final_dec

def pos(tokenized_text):
    '''
    A Part-Of-Speech Tagger (POS Tagger) reads text in language and assigns parts of speech to each word (and other tokens)
    '''
    sent_tag_list = pos_tag(tokenized_text)
    aList = []
    for word, tag in sent_tag_list:
        tagToUse = ''
        if tag.startswith('J'):
            tagToUse = 'a'
        elif tag.startswith('N'):
            tagToUse = 'n'
        elif tag.startswith('R'):
            tagToUse = 'r'
        elif tag.startswith('V'):
            tagToUse = 'v'
        else:
            continue
        aList.append((word, tagToUse))
    return aList


def polarity(text):
    '''
    This function reeturns the polarity score
    '''
    tokenized = tokenize(text)
    pos_df = pos(tokenized)
    lem_df = lemmatize(pos_df)
    cal_df = cal_score(lem_df)
    return cal_df

lemmatizer = WordNetLemmatizer()


def lemmatize(array_of_word_for_a_comment):
    '''
    This function lemmatize the given text'''
    all_words_in_comment = []
    for word in array_of_word_for_a_comment:
        lemma = lemmatizer.lemmatize(word[0], pos=word[1])
        if not lemma:
            continue
        all_words_in_comment.append([lemma,word[1]])
    return all_words_in_comment

def main():
    '''
    main function
    '''
    st.title('Sentiment Analysis ')
    data = st.text_area("Enter Text Data","Type here..")
    data = data.strip()
    if st.button('Polarity'):
        var = polarity(data)
        if var == 'Negative':
            st.info("Overall Polarity of corpus is")
            st.error(var)
        elif var == 'Positive':
            st.info("Overall Polarity of corpus is")
            st.success(var)
        else:
            st.info("Overall Polarity of corpus is")
            st.warning(var)
