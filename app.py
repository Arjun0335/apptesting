import streamlit as st
import os
from datetime import datetime

# Page setup
st.set_page_config(page_title="Romantic Wishlist 💖", layout="centered")

# File to store wishlist items (for persistence across sessions)
WISHLIST_FILE = "wishlist.txt"

# Functions to load and save wishlist
def load_wishlist():
    # Default wishlist if file doesn't exist
    default_wishlist = [
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
    
    try:
        if os.path.exists(WISHLIST_FILE):
            with open(WISHLIST_FILE, "r", encoding="utf-8") as f:
                items = [line.strip() for line in f.readlines() if line.strip()]
                return items if items else default_wishlist
        return default_wishlist
    except:
        return default_wishlist

def save_wishlist(wishlist):
    try:
        with open(WISHLIST_FILE, "w", encoding="utf-8") as f:
            for item in wishlist:
                f.write(item + "\n")
        return True
    except:
        return False

# Load wishlist
wishlist = load_wishlist()

# App header with personalized title
st.title(f"💝 My Vani's Wishlist 💝")
st.write(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Add new item section
with st.form("add_item_form"):
    new_item = st.text_input("Add your wishlist 💌")
    submitted = st.form_submit_button("Add to Wishlist")
    
    if submitted and new_item.strip():
        wishlist.append(new_item.strip())
        save_success = save_wishlist(wishlist)
        if save_success:
            st.success("Item added successfully! ❤️")
        else:
            st.session_state["wishlist"] = wishlist  # Fallback to session state
            st.warning("Added to current session only (file saving failed)")

# Display wishlist items
st.subheader("Our Romantic Wishes 💘")
for i, item in enumerate(wishlist, 1):
    st.markdown(f"**{i}.** {item}")

# Footer
st.markdown("---")
st.markdown("Made with love 💕")

# Styling
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
        border-radius: 8px;
        font-size: 16px;
    }
    h1, h2, h3 {
        color: #cc0066;
    }
    .stMarkdown {
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
</style>
""", unsafe_allow_html=True)
