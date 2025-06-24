import streamlit as st

st.set_page_config(page_title="Romantic Wishlist 💖", page_icon="💘", layout="centered")

PASSWORD = "241106"

# ---- Initialize state ----
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if 'wishlist' not in st.session_state:
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

# ---- Password page ----
if not st.session_state.authenticated:
    st.title("💖 Welcome to Our Romantic Wishlist 💑")
    pwd = st.text_input("Enter the secret password 🔐", type="password")
    login_btn = st.button("Submit")

    if login_btn:
        if pwd == PASSWORD:
            st.session_state.authenticated = True
            st.success("Login successful! 💕 Scroll down ⬇️")
        else:
            st.error("Wrong password 😢")
    st.stop()
# ---- Wishlist Page ----
st.markdown("<h2 style='color: pink;'>💝 Our Dream Wishlist 💝</h2>", unsafe_allow_html=True)

# Add new item
with st.form("add_form"):
    new_item = st.text_input("Add something romantic 💌", placeholder="e.g. Sunset walk 🌇")
    if st.form_submit_button("Add 💘") and new_item:
        st.session_state.wishlist.append(new_item)
        st.success("Item added!")

# Show items
if st.session_state.wishlist:
    st.markdown("### 💞 Your Wishlist Items:")
    for i, item in enumerate(st.session_state.wishlist):
        col1, col2, col3 = st.columns([5, 1, 1])
        edited_text = col1.text_input(f"Item {i+1}", value=item, key=f"text_{i}")
        if col2.button("✏️", key=f"edit_{i}"):
            st.session_state.wishlist[i] = edited_text
            st.success("Updated!")
        if col3.button("🗑️", key=f"delete_{i}"):
            st.session_state.wishlist.pop(i)
            st.success("Deleted!")
            break  # Prevent multiple deletions in one run

# ---- Romantic Styling ----
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
</style>
""", unsafe_allow_html=True)
