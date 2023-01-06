import requests
import streamlit as st
import streamlit.components.v1 as components


def display_contact():
    with st.container():

        # Documentation: https://formsubmit.co/
        contact_form = f"""
    <form action="https://formsubmit.co/katherinemunro@89gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Hi, I'm interested in working together." required></textarea>
        <button type="submit">Send</button>
    </form>
    """
        l_col, m_col, r_col = st.columns((8, 1, 8))
        with l_col:
            st.write(
                "You can find me on social media, where I share content on data science, AI, Machine Learning, ethics,"
                " tech, entrepreneurship and more. To enquire about working together, contact me on my socials or use "
                "the form below.")
            st.write(f"[LinkedIn]({'https://www.linkedin.com/in/katherine-munro/'}) 🤝"
                     f"[Medium]({'https://medium.com/@katherineamunro'}) 📖"
                     f"[Twitter]({'https://twitter.com/KatherineAMunro'}) 🐦")
            st.write("##")
            st.markdown(contact_form, unsafe_allow_html=True)
        with m_col:
            st.empty()
        with r_col:
            widget_code = """<a class="twitter-timeline" data-height="490" data-theme="light" href="https://twitter.com/KatherineAMunro?ref_src=twsrc%5Etfw">Tweets by KatherineAMunro</a> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> """
            components.html(widget_code, height=490)
