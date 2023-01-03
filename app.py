import streamlit as st
from streamlit_option_menu import option_menu

import home
import speaking
import teaching
import web_copy
import contact
import data_science
import writing

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
with st.sidebar:
    st.write('##')
    section = option_menu(menu_title='Menu:',
                          options=web_copy.SECTIONS,
                          default_index=0)

if section == 'Home':
    home.display_home()
elif section == 'Data Science':
    data_science.display_data_science()
elif section == 'Writing':
    writing.display_writing()
elif section == 'Speaking':
    speaking.display_speaking()
elif section == 'Teaching':
    teaching.display_teaching()
elif section == 'Contact':
    contact.display_contact_form()
else:
    st.write('')

# with st.container():
#    image_col, text_col = st.columns((1, 3))
#    with image_col:
#        st.image(web_copy.BOOK_IMG_URL)
#    with text_col:
#        st.write(web_copy.BOOK_BLURB)