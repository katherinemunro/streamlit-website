import streamlit as st
import web_copy


def display_data_science():
    st.header('Data Science 👩‍💻')
    l_col, r_col = st.columns((8, 6))
    with l_col:
        st.write('I am an experienced data scientist with a background in Natural Language Processing and extensive '
                 'experience in the ecommerce domain.')
        st.markdown(
            """
            My specialities include:
            - Data analysis and visualisation
            - Machine Learning and ML Ops
            - Working in agile, cross-functional teams
            - Designing, building, deploying and operationalising data-based solutions
            """
        )
    with r_col:
        st.video("https://www.youtube.com/watch?v=gCvxpMhDJ_s&t=17s")
        html_str = web_copy.caption("My 'Ask the Expert' video on Customer Lifetime Value prediction.")
        st.components.v1.html(html_str)
