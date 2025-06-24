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
    if st.button("Login"):
        if pwd == PASSWORD:
            st.session_state.authenticated = True
            st.session_state.rerun_flag = True
        else:
            st.error("Incorrect Password")
    if st.session_state.rerun_flag:
        st.session_state.rerun_flag = False
        st.experimental_rerun()
    st.stop()

st.title("💝 Our Romantic Wishlist 💝")

# Add new item
with st.form("add_item_form"):
    new_item = st.text_input("Add something romantic 💌")
    submitted = st.form_submit_button("Add to Wishlist")
    if submitted and new_item.strip():
        st.session_state.wishlist.append(new_item.strip())
        st.session_state.rerun_flag = True
        st.success("Item added!")

# Show and manage wishlist
delete_index = None
update_index = None
update_value = None

for i, item in enumerate(st.session_state.wishlist):
    col1, col2, col3 = st.columns([6, 1, 1])
    with col1:
        updated = st.text_input(f"item_{i}", item, key=f"edit_{i}")
    with col2:
        if st.button("✏️", key=f"save_{i}") and updated != item:
            update_index = i
            update_value = updated
    with col3:
        if st.button("🗑️", key=f"delete_{i}"):
            delete_index = i

if update_index is not None and update_value is not None:
    st.session_state.wishlist[update_index] = update_value
    st.session_state.rerun_flag = True
    st.success("Item updated!")

if delete_index is not None:
    st.session_state.wishlist.pop(delete_index)
    st.session_state.rerun_flag = True
    st.success("Item deleted!")

# Trigger rerun safely at the very end of your script
if st.session_state.rerun_flag:
    st.session_state.rerun_flag = False
    st.experimental_rerun()

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
</style>
""", unsafe_allow_html=True)
