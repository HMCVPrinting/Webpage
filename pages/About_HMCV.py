import streamlit as st
import base64
from PIL import Image
from streamlit_lottie import st_lottie
import requests

# --- Assets ---
img = Image.open('tabicon.png')

# --- Config ---
st.set_page_config(page_title="HMCV | maxxdev", page_icon=img, layout="wide")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

hide_decoration_bar_style = '''
    <style>
        header {visibility: hidden;}
    </style>
'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #31333f;'>HMCV</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #31333f;'>About Us</h2>", unsafe_allow_html=True)

# --- About ---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("##")
        st.write(
                """
                 The HMCV Team:

                 - Harry: He owns the 3D Printer, runs this whole thing (It's pretty cool).
                 - Max: Web Dev (Hey, that's me!)
                 - Charlie: 3D Modeling (CAD, etc.)
                 - Vinnie: Design concepts (What he draws, Charlie makes)

                 """
                 )