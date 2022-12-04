import streamlit as st
import web_copy

# todo poss. add animation: https://www.youtube.com/watch?v=VqgUkExPvLY and https://lottiefiles.com/

st.set_page_config(layout='wide', page_title='Katherine Munro\s Personal Website', page_icon='👩‍💻')


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")  # todo personalise css

# Banner image # TODO set size properly or else delete. Can use PIL: https://stackoverflow.com/questions/72131751/how-do-i-resize-the-image-shown-by-st-image
# st.image(web_copy.BANNER_URL, caption='Hi. This is me, moderating TedX Innsbruck 2021')

# Side menu
section = st.sidebar.radio(label='What I do:',
                           options=web_copy.SECTIONS.keys(), index=0)

st.header('Katherine Munro')
st.subheader('Data Scientist. Computational Linguist. Speaker, author, teacher. Geek.')
st.write(web_copy.INTRO)
st.write(web_copy.CTA)
st.write('\n')

# todo create function. Possibly already set the default message here
if section == 'Data Science':
    st.header(web_copy.SECTIONS['Data Science']['head'])
    st.write(web_copy.SECTIONS['Data Science']['body'])
elif section == 'Writing':
    st.header(web_copy.SECTIONS['Writing']['head'])
    st.write(web_copy.SECTIONS['Writing']['body'])
elif section == 'Speaking':
    st.header(web_copy.SECTIONS['Speaking']['head'])
    st.write(web_copy.SECTIONS['Speaking']['body'])
elif section == 'Teaching':
    st.header(web_copy.SECTIONS['Teaching']['head'])
    st.write(web_copy.SECTIONS['Teaching']['body'])
else:
    st.write('')

# with st.container():
#    image_col, text_col = st.columns((1, 3))
#    with image_col:
#        st.image(web_copy.BOOK_IMG_URL)
#    with text_col:
#        st.write(web_copy.BOOK_BLURB)

with st.container():
    st.write("---")
    st.header("Let's work together!")
    st.write("##")

    # Documentation: https://formsubmit.co/
    contact_form = f"""
    <form action="https://formsubmit.co/katherinemunro@89gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Hi, I'd like to enquire about your {section.lower()} services." required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    l_col, m_col, r_col = st.columns((2, 1, 1))
    with l_col:
        st.markdown(contact_form, unsafe_allow_html=True)
    with m_col:
        st.empty()
    with r_col:
        st.image(web_copy.PROFILE_URL, width=200)
