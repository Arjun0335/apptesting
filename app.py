import streamlit as st

st.set_page_config(page_title="Romantic Wishlist 💖", layout="centered")

PASSWORD = "241106"

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "wishlist" not in st.session_state:
    st.session_state.wishlist = [
        "Chandni Chowk ki tikki and ice cream",
        "Ghumna and baatein krna",
        "Love to make me irritate",
        "Handle her mood swings",
        "Make her happy and calm",
        "Love her indefinitely",
        "Feets touch krna",
        "Give my shoes to her if her feets pain from heels",
        "My job to protect her from other boys",
        "Always listen her",
        "She like me for my efforts",
        "Last periods date - 3rd June 2025",
        "Call her everyday - only 2 left out of 5",
        "Loves blue lays, chocolate ice cream, Natraj ki tikki, coke and momos bhi",
        "Never have to leave alone when overthinking or when mood off.",
        "Go to gym and become her cute gym guy and learn bike also",
        "20th June her feet was in pain and mood swings also"
    ]

if "rerun_flag" not in st.session_state:
    st.session_state.rerun_flag = False

# Login Page
if not st.session_state.authenticated:
    st.title("💘 Romantic Wishlist Login")
    pwd = st.text_input("Enter Password 🔐", type="password")
    login_clicked = st.button("Login")
    if login_clicked:
        if pwd == PASSWORD:
            st.session_state.authenticated = True
            st.session_state.rerun_flag = True  # <--- SET FLAG BEFORE STOP
        else:
            st.error("Incorrect Password")
    # Safe rerun after UI logic
    if st.session_state.rerun_flag:
        st.session_state.rerun_flag = False
        st.experimental_rerun()
    st.stop()

# Main Page...
st.title("💝 Our Romantic Wishlist 💝")

# ... rest of your app as already written ...
