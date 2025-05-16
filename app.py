import streamlit as st
import yagmail

# --- Configuration ---
USER_CREDENTIALS = {
    "Aruu": "241106",
    "admin": "admin123"
}

RECEIVER_EMAIL = "arjungupta0335@gmail.com"       # Your receiving email
SENDER_EMAIL = "arjungupta0335@gmail.com"              # Your sending Gmail
SENDER_PASSWORD = "Arj7678#181"              # App password from Google

def send_email(subject, content):
    try:
        yag = yagmail.SMTP(SENDER_EMAIL, SENDER_PASSWORD)
        yag.send(to=RECEIVER_EMAIL, subject=subject, contents=content)
        return True
    except Exception as e:
        return str(e)

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
                st.experimental_rerun()
            else:
                st.error("Invalid username or password")

# --- Grievance Submission Page ---
def grievance_page():
    st.title("📨 Submit Your Grievance")
    st.write(f"Welcome, **{st.session_state.user}**!")

    with st.form("grievance_form", clear_on_submit=True):
        mood = st.selectbox("How are you feeling?", ["Angry", "Sad", "Sorry", "Happy", "Grateful"])
        message = st.text_area("Your grievance or message:")
        submitted = st.form_submit_button("Press Enter to Submit")
        
        if submitted:
            if message.strip() == "":
                st.warning("Message cannot be empty.")
            else:
                email_subject = f"Grievance from {st.session_state.user} ({mood})"
                email_body = f"User: {st.session_state.user}\nMood: {mood}\nMessage:\n{message}"
                status = send_email(email_subject, email_body)
                if status == True:
                    st.success("✅ Message sent directly to Me hehe!")
                else:
                    st.error(f"❌ Failed to send email: {status}")
    
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.experimental_rerun()

# --- Main Flow ---
st.set_page_config(page_title="Grievance Portal", page_icon="📩")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login_page()
else:
    grievance_page()
