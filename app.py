import streamlit as st
from PIL import Image
import base64

# Page configuration
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
        @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Quicksand:wght@400;600&display=swap');

        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded_img}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        h1 {{
            font-family: 'Pacifico', cursive;
            color: #ff69b4;
            text-shadow: 2px 2px 4px #000000;
        }}
        .custom-text {{
            font-family: 'Quicksand', sans-serif;
            font-size: 20px;
            color: #ffffff;
            background-color: rgba(0, 0, 0, 0.4);
            padding: 20px;
            border-radius: 15px;
        }}
        .love-button .stButton>button {{
            background-color: #ff69b4;
            color: white;
            font-weight: bold;
            border: None;
            padding: 0.6rem 1.2rem;
            border-radius: 20px;
            transition: all 0.3s ease-in-out;
            font-size: 18px;
        }}
        .love-button .stButton>button:hover {{
            background-color: #ff1493;
            transform: scale(1.05);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Apply background
add_bg_from_local("download.jpeg")

# Title
st.markdown("<h1 style='text-align: center;'>For the One Who Lights Up My World 🌟</h1>", unsafe_allow_html=True)

# Heart animation (GIF)
with open("heart.gif", "rb") as file_:
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" width="250" style="display: block; margin-left: auto; margin-right: auto;">',
    unsafe_allow_html=True,
)

# Loving message
st.markdown(
    """
    <div class='custom-text' style='text-align: center;'>
        Every moment with you is a memory worth cherishing. <br>
        Your smile, your laugh, your love — they mean everything to me. <br>
        I made this just to remind you how incredibly special you are! ❤️
    </div>
    """,
    unsafe_allow_html=True
)

# Couple image
img = Image.open("couple.jpg")
st.image(img, caption="My love 💑", use_column_width=True)

# Interactive love button
with st.container():
    st.markdown("<div class='love-button' style='text-align: center;'>", unsafe_allow_html=True)
    if st.button("Click to Feel Loved 💌"):
        st.balloons()
        st.success("You're the most amazing person in the universe! 💘")
    st.markdown("</div>", unsafe_allow_html=True)
