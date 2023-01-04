import streamlit as st

import web_copy

AMZN_URL = 'https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiDmMql_Kv8AhXRya' \
           'QKHa4hBVEQFnoECBYQAQ&url=https%3A%2F%2Fwww.amazon.com%2FHandbook-Data-Science-AI-Analytics%2Fdp%2F1569908' \
           '869&usg=AOvVaw1J7kyQZE0MKi7_diAAF1Bi'


def display_writing():
    st.header('Writing ✍️')
    l_col, r_col = st.columns((8, 6))
    with l_col:
        st.write(f"I edited and co-authored ['The Handbook of Data Science and AI']({AMZN_URL}) (Hanser, 2022)")
        st.markdown(
            f"""
        I also write about data science, programming, and technology, over on 
        [Medium]({'https://medium.com/@katherineamunro'}) and for my former employer, Smarter Ecommerce.
        Some of my articles include:
        - [AI-driven Personalised Marketing:]({'https://katherineamunro.medium.com/ai-in-marketing-the-power-of-personalisation-part-1-b4790b490731?source=user_profile---------4----------------------------'}) How We Got Here and Where We’re Going Next
        - [How Your Digital Personal Assistant Understands What You Want]({'https://katherineamunro.medium.com/how-your-virtual-assistant-knows-what-you-want-and-gets-it-done-8de4b0845614?source=user_profile---------2----------------------------'}) (And Gets it Done)
        - [Can AI Solve My Business Problem?]({'https://medium.com/womeninai/can-artificial-intelligence-solve-my-business-problem-4ff3bcbffe32'}) (co-written with Women in AI Upper Austria)
        - [Designing the solution:]({'https://smarter-ecommerce.com/blog/en/data-science/designing-the-solution-ai-based-item-level-bidding-automation-in-google-shopping/'}) AI-based, item-level bidding automation in Google Shopping
        """
        )
    with r_col:
        st.image(web_copy.BOOK_URL)
