import streamlit as st
import web_copy


def display_teaching():
    st.header('Teaching 👩‍🏫')
    l_col, r_col = st.columns((8, 6))
    with l_col:
        st.write('At just 15, I started giving guitar and piano lessons. Later, I became a telemarketing sales coach. '
                 'Later still, I taught academic English, and ESL (English as a Second Language) in Germany. '
                 'Now, I create courses on applied data science for LinkedIn Learning, and as a volunteer mentor for '
                 'Female Coders, I give free coding lessons to women trying to get into tech.')
        st.markdown(
            f"""
            You can find my LinkedIn learning courses (in German) here:
            - [NLP Tools and Methods]({'https://www.linkedin.com/learning/natural-language-processing-nlp-mit-python-werkzeuge-und-methoden'})
            - [Machine Learning in Practice: Marketing]({'https://www.linkedin.com/learning/machine-learning-in-der-praxis-marketing'})
            """
        )
    with r_col:
        st.video("https://youtu.be/i3S_KBz1nqA", start_time=10)
        html_str = web_copy.caption("My lecture on predicting Customer Lifetime Value at PyData Yerevan, 2022")
        st.components.v1.html(html_str)
