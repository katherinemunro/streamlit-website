import os
import streamlit as st

INTRO = 'I\'m a Data Scientist and Data Science Ambassador in the e-commerce domain, conducting both research' \
        ' and corporate training in AI, machine learning, Natural Language Processing (NLP) and data science. I\'m ' \
        'also a speaker, writer, teacher, and passionate workaholic.'

CTA = 'Use the left menu to learn more, and to access my social links and contact form.'

PROFILE_URL = os.path.join('Images', 'smec_portrait_round.jpg')
ON_CAMERA_URL = os.path.join('Images', 'On_Camera.jpg')
BOOK_URL = os.path.join('Images', 'Textbook.jpg')

SECTIONS = ['Home', 'Data Science', 'Writing', 'Speaking', 'Teaching', 'Contact']


def caption(text: str) -> str:
    """
        Prepares a formatted caption string using HTML
        :param text: the caption text
        :return: the formatted string
        """
    html = '<div style="text-align: center;font-family:verdana;color:white;font-size:75%"><i>{}</i></div>'.format(text)
    return html


def cv_download():
    st.write('You can also download my CV:')
    filename = 'Katherine_Munro_CV.pdf'
    f = open(os.path.join('Images', filename), 'rb')
    st.download_button(label='Download CV', data=f, file_name=filename, mime='pdf', key='download_cv')
