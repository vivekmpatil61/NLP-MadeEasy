#importing appropriate libraries

import streamlit as st
import modules.home
import modules.basicNLP
import modules.ner
import modules.topicmodel
import modules.translate
import modules.textSummarization
import modules.sentiment
from PIL import Image

#pages in the web app
Modules = {
    "Home": modules.home,
    "Basic NLP": modules.basicNLP,
    "NER": modules.ner,
    "Text Summarization": modules.textSummarization,
    "Machine Translation": modules.translate,
    "Sentiment Analysis": modules.sentiment}


def main():
    #WebApp main image
    st.image('NLP.png',width=700)

    #sidebar design
    st.sidebar.title("NLP MadeEasy")
    st.sidebar.text("Natural Language Processing Toolkit")

    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to",list(Modules.keys()))  #Selecting page to be opened using radio button 

    page = Modules[selection]
    page.main()

    st.sidebar.title("About")
    st.sidebar.info(
        '''
        This app is developed solely for etertainnment purpose in the Hashnode Hackathon Powered by Vercel! I believe this app will motivate many Data Science enthusiasts to start working in NLP domain and they'll contribute more to this solution.''')
    st.sidebar.title("Contact")
    st.sidebar.markdown(
        '''
        This app is developed by [Vivek Patil](https://www.linkedin.com/in/vivekmpatil/).
        ''')
    st.sidebar.code('''Crafted with ❤ at Hashnode
  and powered by Vercel''')



if __name__ == "__main__":
    main()
