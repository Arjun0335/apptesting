import streamlit as st

# Set page config
st.set_page_config(page_title="Just for You 💌", page_icon="💖")

# Title
st.title("💌 A Special Message for You")

# Define the correct password
correct_password = "241106"  # example: 13th Sept (or nickname)

# Password input
password = st.text_input("Enter the special date or nickname:", type="password")

if password == correct_password:
    st.success("Access granted 💖")

    # --- Love Letter ---
    st.header("💌 My Love Letter to You")
    st.write("""
    Dear Love,

    Every day with you is a page in the most beautiful story I've ever known. 
    From our first smile to every shared dream, you've made my life extraordinary.

    I love you more with every heartbeat. 💖

    Forever yours,
    [Your Name]
    """)

    # --- Reasons I Love You ---
    st.header("🌹 Reasons I Love You")
    reasons = {
        "Your smile": "It lights up even my darkest days.",
        "Your kindness": "You treat everyone with so much warmth and respect.",
        "Your laugh": "It's contagious and makes my day better every time.",
        "Your support": "You've always believed in me.",
        "Your quirks": "They make you even more unique and special.",
    }

    for reason, detail in reasons.items():
        with st.expander(reason):
            st.write(detail)

    # --- Hidden Future Promise ---
    st.header("🔒 A Little Secret...")

    if st.button("Reveal a hidden promise"):
        st.markdown("### 💍 Future Promise")
        st.write("This is where I’ll post our 1st official date pic and all the moments after... 💑📸")
        st.image("couple.jpeg", caption="Youuu my love", use_column_width=True)

else:
    st.warning("Enter the correct password to unlock the love letter 💘")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")
