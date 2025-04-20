import streamlit as st
from PIL import Image
import base64

# Set page config
st.set_page_config(
    page_title="For My Love 💖",
    layout="centered",
    initial_sidebar_state="auto"
)

# Function to add background image
def add_bg_from_local(img_path):
    with open(img_path, "rb") as f:
        encoded_img = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url("data:image/jpg;base64,{encoded_img}");
             background-size: cover;
             background-position: center;
             background-repeat: no-repeat;
         }}
         </style>
         """,
        unsafe_allow_html=True
    )

# Add background
add_bg_from_local("download.jpeg")

# Title
st.markdown("<h1 style='text-align: center; color: pink;'>For the One Who Lights Up My World 🌟</h1>", unsafe_allow_html=True)

# Display gif
file_ = open("heart.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()
st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" width="300" style="display: block; margin-left: auto; margin-right: auto;">',
    unsafe_allow_html=True,
)

# Message
st.markdown(
    """
    <div style='text-align: center; font-size: 20px; color: white; margin-top: 20px;'>
        Every moment with you is a memory worth cherishing. <br>
        Your smile, your laugh, your love — they mean everything to me. <br>
        I made this just to remind you how special you are! ❤️
    </div>
    """,
    unsafe_allow_html=True
)

# Display a couple image
img = Image.open("couple.jpg")
st.image(img, caption="Us Together", use_column_width=True)

# Button
if st.button("Click to Feel Loved 💌"):
    st.balloons()
    st.success("You're the most amazing person in the universe! 💘")

