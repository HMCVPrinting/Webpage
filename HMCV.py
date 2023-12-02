import streamlit as st
import base64
from PIL import Image
from streamlit_lottie import st_lottie
import requests

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# -- Assets --
img = Image.open('tabicon.png')
lottie_3dprinter = load_lottieurl("https://lottie.host/a9b56deb-9f6b-456f-bb07-fa1e636c8aed/NcWLJD1iCL.json")

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

# --- Title ---
with st.container():
    st.title("HMCV")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("3D Printing")
        st.write("pls take interest so harry pays me")
    with right_column:
        st_lottie(lottie_3dprinter, height=300, key="3dprinter")

# --- About ---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About HMCV")
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