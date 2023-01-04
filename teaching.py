import streamlit as st


def display_teaching():
    st.header('Teaching 👩‍🏫')
    st.write('At just 15, I started giving guitar and piano lessons. Later, I became a telemarketing sales coach. '
             'Later still, I taught academic English, and ESL (English as a Second Language) in Germany. '
             'Now, I create courses on applied data science for LinkedIn Learning, and as a volunteer mentor for Female'
             ' Coders, I give free coding lessons to women trying to get into tech.')
    st.markdown(
        f"""
        You can find my LinkedIn learning courses (in German) here:
        - [NLP Tools and Methods]({'https://www.linkedin.com/learning/natural-language-processing-nlp-mit-python-werkzeuge-und-methoden'})
        - [Machine Learning in Practice: Marketing]({'https://www.linkedin.com/learning/machine-learning-in-der-praxis-marketing'})
        """
    )
