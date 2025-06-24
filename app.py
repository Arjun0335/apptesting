import streamlit as st

st.set_page_config(page_title="Romantic Wishlist 💖", page_icon="💘", layout="centered")

PASSWORD = "241106"

# Initialize session state
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

# Login interface
if not st.session_state.authenticated:
    st.markdown("## 💖 Welcome to Our Romantic Wishlist 💑")
    pwd = st.text_input("Enter the secret password 🔐", type="password")
    if st.button("Submit"):
        if pwd == PASSWORD:
            st.session_state.authenticated = True
            st.experimental_rerun()
        else:
            st.error("❌ Wrong password — try again!")
    st.stop()

# Main app: shown after login
st.markdown("<h2 style='color: pink;'>💝 Our Dream Wishlist 💝</h2>", unsafe_allow_html=True)

# Add new item
with st.form("add"):
    new_item = st.text_input("Add something romantic 💌")
    submitted = st.form_submit_button("Add 💘")
    if submitted:
        st.session_state.wishlist.append(new_item)
        st.success("Added!")
        st.experimental_rerun()

# Display list with edit/delete
del_index = None
for i, item in enumerate(st.session_state.wishlist):
    cols = st.columns([6, 1, 1])
    with cols[0]:
        edited = st.text_input(f"{i+1}.", value=item, key=f"edit_{i}")
    if cols[1].button("✏️", key=f"edit_btn_{i}"):
        st.session_state.wishlist[i] = edited
        st.success("Updated!")
        st.experimental_rerun()
    if cols[2].button("🗑️", key=f"del_btn_{i}"):
        del_index = i

if del_index is not None:
    st.session_state.wishlist.pop(del_index)
    st.success("Deleted!")
    st.experimental_rerun()

# Style
st.markdown("""
<style>
.stTextInput>div>div>input { background: #ffe6f0; color: #cc0066; font-weight: bold; }
div.stButton>button { background: #ff99cc; color: white; border-radius:10px; font-size:18px; }
</style>
""", unsafe_allow_html=True)
