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
st.set_option('deprecation.showPyplotGlobalUse', False)


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
    st.image('Images/NLP.png',width=700)

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
        This app is developed solely for etertainnment purpose. I believe this app will motivate many Data Science enthusiasts to start working in NLP domain and they'll contribute more to this solution.''')
    st.sidebar.title("Contact")
    st.sidebar.markdown(
        '''
        This app is developed by [Vivek Patil](https://www.linkedin.com/in/vivekmpatil/).
        ''')
    st.sidebar.text('''Crafted with ❤ from India''')



if __name__ == "__main__":
    main()
