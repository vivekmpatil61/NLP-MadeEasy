import streamlit as st
from gensim.summarization.summarizer import summarize
import sumy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

import copy
import readtime
from difflib import SequenceMatcher
import readtime
stop_words = set(stopwords.words('english'))


def sumy_summarizer(docx):
	parser = PlaintextParser.from_string(docx, Tokenizer("english"))
	lex_summarizer = LexRankSummarizer()
	summary = lex_summarizer(parser.document, 3)
	summary_list = [str(sentence) for sentence in summary]
	result = ' '.join(summary_list)
	return result


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def calc_time(result):
    t = readtime.of_text(result)
    return t

def optimize_summary(p,q):
    corpus=[]
    for i in range(len(p)-1):
        for j in range(i+1,len(p)):
            # print("similarity between s{} and s{} is : {}".format(i+1,j+1,similar(p[i],p[j])))
            if similar(p[i],p[j]) > 0.8:
                corpus.append(j) if len(p[i])>len(p[j]) else corpus.append(i)
            break

    dict.fromkeys(corpus)
    corpus = list(dict.fromkeys(corpus))

    for i,j in enumerate(corpus):
        del q[j-i]

    return q


def sumy_summarizer(docx):
    parser = PlaintextParser.from_string(docx,Tokenizer("english"))
    lex_summarizer = LexRankSummarizer()
    summary = lex_summarizer(parser.document,3)
    summary_list = [str(sentence) for sentence in summary]
    result = " ".join(summary_list)
    return result

regex = 'https.\/\/\S+.html'

def get_unique_links(res):
    links = re.findall(regex,res)
    links = set(links)
    return links


def main():
    '''NLP App'''
    st.title("Text Summarization")
    msg = st.text_area("Eter your data to be summarized","Type here..")
    msg = msg.strip()
    summary_options = st.selectbox("Choice your Summarizer",("Summarizer - 1","Summarizer - 2"))
    try:
        if st.button("Summarize"):
            if summary_options == 'Summarizer - 1':
                result = summarize(msg)
                st.subheader("Summary")
                links = get_unique_links(result)
                result = re.sub('https.\/\/\S+.html', ' ', result)
                result = re.sub(' +', ' ', result)
                a = result.split('. ')
                b = copy.deepcopy(a)
                result = optimize_summary(a, b)
                result = ". ".join(result)
                if len(result) > 2:
                    st.success(result)
                else:
                    st.warning('Feed more data as input to Summarizer Tool')

                t = calc_time(result)
                d = calc_time(msg)
                st.info("Actual data - {} seconds read, Summarised data - {} seconds read".format(d.seconds, t.seconds))

            else:
                st.subheader("Summary")
                result = sumy_summarizer(msg)
                links = get_unique_links(result)
                result = re.sub('https.\/\/\S+.html', ' ', result)
                result = re.sub(' +', ' ', result)
                a=result.split('. ')
                b=copy.deepcopy(a)
                result = optimize_summary(a,b)
                result = ". ".join(result)
                st.success(result)
                t = calc_time(result)
                d = calc_time(msg)
                st.info("Actual data - {} seconds read, Summarised data - {} seconds read".format(d.seconds,t.seconds))

    except:
        st.warning("Input must have more than one sentence if you are using Summarizer - 1, please try again!")
