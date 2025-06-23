import streamlit as st
import json
import os

# ---- Config ----
st.set_page_config(page_title="Romantic Wishlist 💖", page_icon="💘", layout="centered")
DATA_FILE = "wishlist.json"
PASSWORD = "241106"

# ---- Load and Save Functions ----
def load_wishlist():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return default_items.copy()

def save_wishlist(wishlist):
    with open(DATA_FILE, "w") as f:
        json.dump(wishlist, f)

# ---- Romantic Default Wishlist ----
default_items = [
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

# ---- Authentication ----
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("💖 Welcome to Our Romantic Wishlist 💑")
    password = st.text_input("Enter the secret password 🔐", type="password")
    if password == PASSWORD:
        st.session_state.authenticated = True
        st.success("Welcome! Loading your wishlist...")
        st.stop()
    elif password != "":
        st.error("Wrong password! Try again.")
        st.stop()
    else:
        st.stop()

# ---- Load current wishlist ----
wishlist = load_wishlist()

# ---- App Title ----
st.markdown("<h2 style='color: pink;'>💝 Our Dream Wishlist 💝</h2>", unsafe_allow_html=True)

# ---- Add New Item ----
with st.form("add_item"):
    new_item = st.text_input("Add something romantic to the wishlist 💌", placeholder="E.g. Candlelight Dinner 🕯️")
    if st.form_submit_button("Add to Wishlist 💘") and new_item:
        wishlist.append(new_item)
        save_wishlist(wishlist)
        st.success("Added to wishlist!")
        st.experimental_rerun()

# ---- Display Wishlist ----
if wishlist:
    st.markdown("### 💞 Your Wishlist Items:")
    delete_index = None

    for i, item in enumerate(wishlist):
        cols = st.columns([5, 1, 1])
        with cols[0]:
            edited = st.text_input(f"Item {i+1}", value=item, key=f"edit_input_{i}")
        with cols[1]:
            if st.button("💘 Edit", key=f"edit_btn_{i}"):
                wishlist[i] = edited
                save_wishlist(wishlist)
                st.success("Item updated!")
                st.experimental_rerun()
        with cols[2]:
            if st.button("❌ Delete", key=f"delete_btn_{i}"):
                delete_index = i

    if delete_index is not None:
        wishlist.pop(delete_index)
        save_wishlist(wishlist)
        st.success("Item deleted!")
        st.experimental_rerun()
else:
    st.info("Your wishlist is empty. Add your first romantic plan 💭!")

# ---- Styling ----
st.markdown("""
<style>
    .stTextInput > div > div > input {
        background-color: #ffe6f0;
        color: #cc0066;
        font-weight: bold;
    }
    div.stButton > button {
        background-color: #ff99cc;
        color: white;
        border-radius: 10px;
        font-size: 18px;
    }
    .st-bb {
        color: #ff66b2 !important;
    }
</style>
""", unsafe_allow_html=True)
