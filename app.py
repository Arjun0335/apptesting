import streamlit as st
from PIL import Image
import base64

# Page Config
st.set_page_config(
    page_title="For My Love 💖",
    layout="centered"
)

# Add Background Function
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
            text-shadow: 2px 2px 6px #000000;
        }}
        .custom-text {{
            font-family: 'Quicksand', sans-serif;
            font-size: 22px;
            color: #ffffff;
            background-color: rgba(0, 0, 0, 0.5);
            padding: 25px;
            border-radius: 20px;
            box-shadow: 0 0 20px #ff69b4;
        }}
        .stButton>button {{
            background-color: #ff69b4;
            color: white;
            font-weight: bold;
            border: none;
            padding: 0.7rem 1.5rem;
            border-radius: 30px;
            font-size: 20px;
            margin: 10px;
            transition: all 0.3s ease-in-out;
        }}
        .stButton>button:hover {{
            background-color: #ff1493;
            transform: scale(1.1);
            box-shadow: 0 0 15px #ff1493;
        }}
        .counter-text {{
            font-size: 20px;
            font-weight: bold;
            color: white;
            text-shadow: 1px 1px 2px black;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set background
add_bg_from_local("download.jpeg")

# Title
st.markdown("<h1 style='text-align: center; margin-top: 30px;'>You Make My Heart Smile 💖</h1>", unsafe_allow_html=True)

# Heart GIF
with open("heart.gif", "rb") as file_:
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" width="220" style="display: block; margin-left: auto; margin-right: auto;">',
    unsafe_allow_html=True,
)

# Main message
st.markdown(
    """
    <div class='custom-text' style='text-align: center; margin-top: 30px;'>
        Every day with you is my favorite day. <br>
        So today is my new favorite day. ❤️ <br><br>
        Thank you for being the sunshine that brightens my world! 🌟
    </div>
    """,
    unsafe_allow_html=True
)

# Couple Image
st.markdown("### 💑 Our Beautiful Memory")
img = Image.open("couple.jpg")
st.image(img, caption="Together Forever 💕", use_column_width=True)

# Reply input
st.markdown("### 💬 Leave Your Lovely Message")
reply = st.text_input("Type your sweet message 💌:")
if reply:
    st.success(f"Message received: '{reply}' 💖 Thank you!")

# Love Counter Section
st.markdown("### ❤️ Let's Spread More Love!")

if "love_count" not in st.session_state:
    st.session_state.love_count = 0
if "flower_count" not in st.session_state:
    st.session_state.flower_count = 0

col1, col2 = st.columns(2)

with col1:
    if st.button("Send a Hug 🤗"):
        st.session_state.love_count += 1
        st.toast("Hug sent with love! 💞")

with col2:
    if st.button("Send a Flower 🌸"):
        st.session_state.flower_count += 1
        st.toast("Flower sent with blessings! 🌸🌼")

# Display counters
st.markdown(
    f"""
    <div style='text-align:center; margin-top:20px;' class='counter-text'>
        🤗 Total Hugs Sent: {st.session_state.love_count}<br>
        🌸 Total Flowers Sent: {st.session_state.flower_count}
    </div>
    """,
    unsafe_allow_html=True
)

# Surprise Confetti
st.markdown("### 🎉 Feeling Excited?")
if st.button("Click for a Magical Surprise ✨"):
    st.balloons()
    st.toast("You are a magical blessing! 🌟")

# Final message
st.markdown(
    """
    <div style='text-align: center; font-size: 22px; color: white; margin-top: 50px;'>
        You are my favorite person, my today and all of my tomorrows. 💖<br><br>
        <i>Made with endless love 💕 using my love for youuu my love.</i>
    </div>
    """,
    unsafe_allow_html=True
)
