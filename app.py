import streamlit as st

# Page config
st.set_page_config(page_title="Romantic Wishlist 💖", page_icon="💘", layout="centered")

# Password protection
PASSWORD = "241106"
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# Initialize default wishlist once
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

# Login Page
if not st.session_state.authenticated:
    st.title("💘 Romantic Wishlist Login")
    password = st.text_input("Enter the secret password 🔐", type="password")
    if st.button("Login"):
        if password == PASSWORD:
            st.session_state.authenticated = True
            st.success("Login successful! Scroll down 👇")
        else:
            st.error("Incorrect password. Please try again.")
    st.stop()

# Main Page
st.markdown("<h2 style='color: pink;'>💝 Our Dream Wishlist 💝</h2>", unsafe_allow_html=True)

# Add new item
with st.form("add"):
    new_item = st.text_input("Add something sweet 💌")
    if st.form_submit_button("Add to Wishlist 💘") and new_item.strip():
        st.session_state.wishlist.append(new_item.strip())
        st.success("Added!")

# Show wishlist
if st.session_state.wishlist:
    for i, item in enumerate(st.session_state.wishlist):
        cols = st.columns([6, 1, 1])
        with cols[0]:
            new_value = st.text_input(f"item_{i}", value=item, label_visibility="collapsed")
        with cols[1]:
            if st.button("✏️", key=f"edit_{i}"):
                st.session_state.wishlist[i] = new_value
                st.success("Item updated!")
        with cols[2]:
            if st.button("🗑️", key=f"del_{i}"):
                st.session_state.wishlist.pop(i)
                st.success("Item deleted!")
                st.experimental_rerun()
                break
else:
    st.info("No items yet. Add your first dream!")

# Romantic theme
st.markdown("""
<style>
    .stTextInput > div > div > input {
        background-color: #fff0f5;
        color: #cc0066;
        font-weight: bold;
    }
    div.stButton > button {
        background-color: #ff69b4;
        color: white;
        border-radius: 10px;
        font-size: 16px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)
