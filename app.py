import streamlit as st

# ---- Romantic Theme Config ----
st.set_page_config(page_title="Romantic Wishlist 💖", page_icon="💘", layout="centered")

# ---- Password protection ----
PASSWORD = "241106"  # You can change this to your secret password

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("💖 Welcome to Our Romantic Wishlist 💑")
    password = st.text_input("Enter the secret password 🔐", type="password")
    
    if password == PASSWORD:
        st.session_state.authenticated = True
        st.experimental_rerun()  # rerun to reload the authenticated session
    elif password != "":
        st.error("Wrong password! Please try again.")
        st.stop()  # stop only after showing error
    else:
        st.stop()  # stop waiting for input


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

# ---- Initialize Wishlist ----
if 'wishlist' not in st.session_state:
    st.session_state.wishlist = default_items.copy()

# ---- App Title ----
st.markdown("<h2 style='color: pink;'>💝 Our Dream Wishlist 💝</h2>", unsafe_allow_html=True)

# ---- Add Item Form ----
with st.form("add_item"):
    new_item = st.text_input("What do you want to add to our wishlist?", placeholder="E.g. Paris Trip 🗼, Candlelight Dinner 🕯️")
    submitted = st.form_submit_button("Add to Wishlist 💌")
    if submitted and new_item:
        st.session_state.wishlist.append(new_item)
        st.success("Added to wishlist!")

# ---- Display Wishlist ----
if st.session_state.wishlist:
    st.markdown("---")
    st.markdown("### 💞 Your Wishlist Items:")
    for i, item in enumerate(st.session_state.wishlist):
        cols = st.columns([5, 1, 1])
        with cols[0]:
            edited = st.text_input(f"Item {i+1}", value=item, key=f"item_{i}")
        with cols[1]:
            if st.button("💘 Edit", key=f"edit_{i}"):
                st.session_state.wishlist[i] = edited
                st.success("Item updated!")
        with cols[2]:
            if st.button("❌ Delete", key=f"delete_{i}"):
                st.session_state.wishlist.pop(i)
                st.experimental_rerun()

else:
    st.info("Your wishlist is empty. Add your first dream 💭!")

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
    .st-bb {
        color: #ff66b2 !important;
    }
</style>
""", unsafe_allow_html=True)
