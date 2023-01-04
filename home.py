import streamlit as st
import web_copy


def display_home():
    st.header('Katherine Munro')
    l_col, r_col = st.columns((8, 6))
    with l_col:
        st.subheader('Data Scientist. Computational Linguist. Speaker, author, teacher, consultant, geek.')
        st.write(web_copy.INTRO)
        st.write(web_copy.CTA)
        st.write('\n')
    with r_col:
        st.image(web_copy.PROFILE_URL, width=400)
