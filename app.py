import streamlit as st
import pandas as pd
import os
import openpyxl

# --- Configuration ---
USER_CREDENTIALS = {
    "Vanii": "241106",
    "Aru": "123"
}

# --- Function to Save Grievance to Excel ---
def save_to_excel(username, mood, message):
    data = {
        "Username": [username],
        "Mood": [mood],
        "Message": [message]
    }

    df_new = pd.DataFrame(data)
    file_path = "grievances.xlsx"

    if os.path.exists(file_path):
        df_existing = pd.read_excel(file_path)
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    else:
        df_combined = df_new

    df_combined.to_excel(file_path, index=False)

# --- Login Page ---
def login_page():
    st.title("🔐 Grievance Portal Login")
    with st.form("login_form", clear_on_submit=True):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_btn = st.form_submit_button("Login")
        if login_btn:
            if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
                st.session_state.logged_in = True
                st.session_state.user = username
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Invalid username or password")

# --- Grievance Submission Page ---
def grievance_page():
    st.title("📨 Submit Your Grievance")
    st.write(f"Welcome, **{st.session_state.user}**!")

    with st.form("grievance_form", clear_on_submit=True):
        mood = st.selectbox("How are you feeling?", ["😠 Angry", "😢 Sad", "😐 Neutral", "😊 Happy", "😇 Grateful"])
        message = st.text_area("Your grievance or message:")
        submitted = st.form_submit_button("Press Enter to Submit")

        if submitted:
            if message.strip() == "":
                st.warning("Message cannot be empty.")
            else:
                save_to_excel(st.session_state.user, mood, message)
                st.success("✅ Message sent!")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

# Only allow Aruu to download the Excel file
if st.session_state.user == "Aru" and os.path.exists("grievances.xlsx"):
    with open("grievances.xlsx", "rb") as f:
        st.download_button("📥 Download Excel", f, file_name="grievances.xlsx")

# --- Main Flow ---
st.set_page_config(page_title="Grievance Portal", page_icon="📩")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login_page()
else:
    grievance_page()
