import streamlit as st
import requests
import streamlit.components.v1 as components


def display_contact_form():
    with st.container():
        st.write("You can find me on social media, where I share content on data science, AI, Machine Learning, ethics,"
                 " tech, entrepreneurship and more. To enquire about working together, contact me on my socials or use "
                 "the form below.")
        li_col, tw_col, me_col, oth = st.columns((4, 4, 4, 1))
        with li_col:
            st.write(f"[LinkedIn]({'https://www.linkedin.com/in/katherine-munro/'}) 🤝")
        with tw_col:
            st.write(f"[Medium]({'https://medium.com/@katherineamunro'}) 📖")
        with me_col:
            st.write(f"[Twitter]({'https://twitter.com/KatherineAMunro'}) 🐦")
        st.write("##")

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
            st.markdown(contact_form, unsafe_allow_html=True)
        with m_col:
            st.empty()
        with r_col:
            Tweet("https://twitter.com/KatherineAMunro/status/1463090617832071174").component()

class Tweet(object):
    def __init__(self, s, embed_str=False):
        if not embed_str:
            # Use Twitter's oEmbed API
            # https://dev.twitter.com/web/embedded-tweets
            api = "https://publish.twitter.com/oembed?url={}".format(s)
            response = requests.get(api)
            self.text = response.json()["html"]
        else:
            self.text = s

    def _repr_html_(self):
        return self.text

    def component(self):
        return components.html(self.text, height=600)
