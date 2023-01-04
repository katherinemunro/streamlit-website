import streamlit as st


def display_speaking():
    st.header('Speaking 🎤')
    st.write('With my background in teaching and leading a professional covers band, I will bring a unique energy and '
             'expertise to the stage for your next event. I have hosted numerous community talks on AI, moderated TedX '
             'Innsbruck and the Austrian student competition for AI (BWKI), and appeared in diverse webinars, podcasts '
             'and conferences.')
    st.markdown(
        f"""
        Some of my recorded appearances include:
        - [Ask the expert]({'https://www.youtube.com/watch?v=gCvxpMhDJ_s'}): What is Customer Lifetime Value?
        - [Artificial Intelligence and Natural Language Processing in E-Commerce]({'https://www.youtube.com/watch?v=r7JI_5mt3To'})
        - Drive CX and Revenue with NLP in marketing and ecommerce, E26 of [The Applied AI Pod]({'https://podcasts.apple.com/ie/podcast/drive-cx-and-revenue-with-nlp-in-marketing-and-ecommerce-e26/id1494700099?i=1000513540565'})
        - Representing Austria at the Women in AI Global Summit: [Future Roles in AI]({'https://www.youtube.com/watch?v=ao3IW1u4tsM'})
        """
    )
