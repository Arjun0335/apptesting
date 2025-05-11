import streamlit as st
from streamlit_lottie import st_lottie
import requests
import time

# Page config
st.set_page_config(page_title="For My Love Vaniii ❤️", page_icon="💌", layout="wide")

# Load Lottie animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

love_animation = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_kxsd2ytq.json")

# Main layout
with st.container():
    st.title("❤️ For My Love A ❤️")
    st.subheader("A simple website to tell you how much you are important for me.")
    st_lottie(love_animation, height=300)

# Love note section
with st.container():
    st.header("💌 My Message to You")
    love_letter = """
    Dear A,

    Every day with you is a beautiful memory.  
    Your smile lights up my world and your presence brings peace.  
    This little site is just a tiny effort to express how much I love and cherish you.

    Forever yours,  
    Arjun 💖
    """
    st.markdown(f"<div style='font-size:20px; line-height:1.7;'>{love_letter}</div>", unsafe_allow_html=True)

# Display default photo
st.header("📸 your the most beautiful photo")
st.image("couple.jpg", 
         caption="Every moment with you is magic 💖", use_column_width=True)

# Timeline of special moments
with st.container():
    st.header("🕰️ Our Special Timeline")
    events = {
        "Met You": "✨ The best day of my life!",
        "First Meet": "💫 Butterflies and heartbeats!",
        "Second meet": "📸 The memory that still makes me smile!",
        "Still in Love": "💖 Every moment, every day."
    }
    for event, desc in events.items():
        st.markdown(f"**{event}:** {desc}")
        time.sleep(0.5)

# Secret message / contact form
st.header("💬 Want to leave me a secret message?")
with st.form(key="contact_form"):
    name = st.text_input("Your name")
    msg = st.text_area("Your message to me")
    submit = st.form_submit_button("Send 💌")
    if submit:
        st.success("Thank you for your message! 💕")

# Footer
st.markdown("---")
st.markdown("<center><i>Made with love by Arjun for A 💘</i></center>", unsafe_allow_html=True)
