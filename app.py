import streamlit as st
import random

# --------------------------
# Custom Page Configuration
# --------------------------
st.set_page_config(page_title="Just for You 💌", page_icon="💘", layout="centered")

# --------------------------
# Romantic Background with CSS
# --------------------------
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1503694978374-8a2fa686963a?auto=format&fit=crop&w=1600&q=80");
    background-size: cover;
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
.stMarkdown h1, h2, h3, h4 {
    color: #ffffff;
}
.stMarkdown p {
    color: #f5f5f5;
    font-size: 18px;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# --------------------------
# Title and Greeting
# --------------------------
st.markdown("<h1 style='text-align: center;'>💌 A Secret Message Just for You</h1>", unsafe_allow_html=True)

# --------------------------
# Quote of the Day
# --------------------------
quotes = [
    "“I look at you and see the rest of my life in front of my eyes.”",
    "“You are my today and all of my tomorrows.” — Leo Christopher",
    "“In all the world, there is no heart for me like yours.” — Maya Angelou",
    "“Whatever our souls are made of, yours and mine are the same.” — Emily Brontë"
]
st.subheader("💭 Quote of the Day:")
st.info(random.choice(quotes))

# --------------------------
# Password Protection
# --------------------------
correct_password = "241106"
password = st.text_input("🔐 Enter the special password:", type="password")

if password == correct_password:
    st.success("Access granted 💖")

    # ----------------------
    # Love Letter Section
    # ----------------------
    st.header("💌 My Love Letter")
    st.write("""
    My Dearest,

    Every moment with you feels like magic. 
    You're the reason behind my smile, my strength, and my dreams.

    No matter how far or close we are, you're always in my heart. 💖

    Yours forever,
    Arjun
    """)

    st.image("https://media.giphy.com/media/3o6ZsZKn72nI8zDkkw/giphy.gif", caption="Thinking of You...", use_column_width=True)

    # ----------------------
    # Reasons I Love You
    # ----------------------
    st.header("💗 Reasons Why I Love You")
    with st.container():
        reasons = {
            "🌟 Your Smile": "It’s pure sunshine. It melts all my worries.",
            "🧠 Your Mind": "The way you think and understand the world amazes me.",
            "🎉 Your Spirit": "You're fun, vibrant, and make everything exciting.",
            "🫂 Your Empathy": "You care deeply, and that touches me the most.",
            "💬 Your Conversations": "You always know what to say and when to listen."
        }
        for key, value in reasons.items():
            with st.expander(key):
                st.write(value)

    # ----------------------
    # Personal Timeline
    # ----------------------
    st.header("📅 Our Journey So Far")
    st.write("""
    - 💬 First Talk: That sweet first conversation that changed everything.
    - 📸 First Picture Together: A memory saved forever.
    - 💑 First Date: Nervous, happy, perfect.
    - 🫶 First 'I Love You': The words that meant the world.
    - 🌅 Many more memories to come...
    """)

    # ----------------------
    # Secret Future Promise
    # ----------------------
    st.header("🔮 A Secret for the Future...")
    if st.button("Click to reveal a promise 💍"):
        st.markdown("""
        ### 🌈 Our Forever Page
        Someday soon, this will be the place where I’ll post our first official date pic and every moment after that.

        I promise to fill this space with our memories, joys, and smiles 💑📸
        """)
        st.image("couple.jpg", caption="Our Future Awaits...", use_column_width=True)

else:
    st.warning("Please enter the correct password to unlock the message 💘")

# ----------------------
# Footer
# ----------------------
st.markdown("---")
st.markdown("<p style='text-align: center;'>Made with ❤️ by [Your Name]</p>", unsafe_allow_html=True)
