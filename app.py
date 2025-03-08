import re
import random
import string
import streamlit as st

# Blacklist of common passwords
BLACKLIST = ["password", "python", "12345678", "qwerty", "12345", "123456789", "mahnoor123", "1234567", "football", "iloveyou"]

# Custom Scoring Weights
WEIGHTS = {
    "length": 2,
    "uppercase_lowercase": 2,
    "digit": 1,
    "special_char": 2,
    "blacklist": -3
}

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 12:
        score += WEIGHTS["length"]
    else:
        feedback.append("❌ Password should be at least 12 characters long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += WEIGHTS["uppercase_lowercase"]
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += WEIGHTS["digit"]
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += WEIGHTS["special_char"]
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # Blacklist Check
    if password.lower() in BLACKLIST:
        score += WEIGHTS["blacklist"]
        feedback.append("❌ This password is too common and easy to guess.")

    return score, feedback

# Function to generate a strong password
def generate_password():
    length = 16
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to generate multiple password suggestions
def generate_password_suggestions():
    return [generate_password() for _ in range(5)]

# Streamlit Interface
st.set_page_config(page_title="Password Strength Meter", layout="wide")

# Sidebar Navbar
menu = st.sidebar.radio("Password Strength", ["Home", "Password", "Generate Password", "About", "Contact"])

if menu == "Home":
    st.title("Welcome to Password Strength Meter")
    st.write("Easily check your password strength and generate secure passwords.") 
    st.write("This app helps you protect your online accounts by checking password strength and suggesting secure passwords.")
    st.image("image.png")

elif menu == "Password":
    st.title("Check Password Strength")
    st.write("""
        🔒 **Why checking your password is important?**  
        - A weak password makes it easy for hackers to access your account.  
        - This tool helps you identify weak passwords and gives instant suggestions to improve them.  
        - Make sure to use a mix of uppercase, lowercase, numbers, and special characters to make your password stronger.  
    """)
    
    password = st.text_input("Enter your password:", type="password")

    # Live Feedback & Progress Bar
    if password:
        score, feedback = check_password_strength(password)

        progress = min(max(score / 8, 0), 1)
        st.progress(progress)

        # Show strength status
        if score <= 2:
            st.error("❌ Weak Password")
        elif score <= 4:
            st.warning("⚠️ Moderate Password")
        else:
            st.success("✅ Strong Password")

        # Real-time feedback and hints
        st.write(f"📝 Length: {len(password)} characters (Min: 12)")
        if not re.search(r"[A-Z]", password):
            st.warning("⚠️ Missing uppercase letter.")
        if not re.search(r"[a-z]", password):
            st.warning("⚠️ Missing lowercase letter.")
        if not re.search(r"\d", password):
            st.warning("⚠️ Missing number.")
        if not re.search(r"[!@#$%^&*]", password):
            st.warning("⚠️ Missing special character (!@#$%^&*).")

        for msg in feedback:
            st.write(msg)

elif menu == "Generate Password":
    st.title("Generate Strong Password")
    st.write("""
        🔑 **Need help creating a strong password?**  
        - Click the button below to generate some secure password suggestions.  
        - Choose the one you like or create a new one if needed.  
        - A strong password should be a mix of uppercase, lowercase, numbers, and special characters.  
    """)
    
    if st.button("Generate Password Suggestions", use_container_width=True):
        suggestions = generate_password_suggestions()
        for i, suggestion in enumerate(suggestions):
            if st.button(f"Use Suggestion {i + 1}: {suggestion}", key=f"btn_{i}"):
                st.success(f"Selected Password: {suggestion}")

elif menu == "About":
    st.title("About Password Strength Checker")

    st.write("### Why We Built This App:")
    st.write("- Online security is very important today.")
    st.write("- Weak passwords make it easy for hackers to access your personal data.")
    st.write("- This app helps you create and use strong passwords to keep your accounts safe.")

    st.write("### How It Works:")
    st.write("1. **Password Checker:** Checks how strong your password is based on length, uppercase/lowercase letters, numbers, and special characters.")
    st.write("2. **Real-Time Feedback:** Gives instant advice to make your password stronger.")
    st.write("3. **Password Generator:** Creates secure and random passwords for you to use.")
    st.write("4. **Blacklist Protection:** Stops you from using common, easy-to-guess passwords.")

    st.write("### Benefits:")
    st.write("✅ Helps prevent hacking by suggesting strong passwords.")
    st.write("✅ Protects your accounts from weak passwords.")
    st.write("✅ Makes it easy to create unique and secure passwords.")
    st.write("✅ Saves time by generating ready-to-use strong passwords.")
    st.write("✅ Simple to use — no technical knowledge needed!")

    st.write("✅ Built with **Python** and **Streamlit** for a smooth and easy experience.")

elif menu == "Contact":
    st.title("Contact")

    st.write("**Contact Details:**")
    st.write("**Name:** Mahnoor")
    st.write("**Education:** MPhil in IT")
    st.write("**City:** Hyderabad")
    st.write("**Course:** GIAIC Q3")
    st.write("**Slot:** Sunday Afternoon")
    st.write("**LinkedIn:** [Mahnoor's LinkedIn](https://www.linkedin.com/in/mahnoor-shaikh/)")
    st.write("**GitHub:** [Mahnoor's GitHub](https://github.com/MAHNOORSHK/)")

# Styling for buttons
st.markdown(
    """
    <style>
        .stButton>button {
            background-color: #5D1049;
            color: white;
            border-radius: 8px;
            padding: 10px;
            font-size: 16px;
            transition: background-color 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #720d5d;
        }
    </style>
    """,
    unsafe_allow_html=True
)
