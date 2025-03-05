# import streamlit as st
# import random
# import string
# import re

# # Set Page Configuration
# st.set_page_config(page_title="Advanced Password Strength Meter", layout="centered")

# # Custom CSS for styling and dark mode
# st.markdown("""
#     <style>
#         body {
#             background-color: white;
#             color: black;
#             font-family: 'Arial', sans-serif;
#         }
#         .dark-mode {
#             background-color: black !important;
#             color: white !important;
#         }
#         h2 {
#             text-align: center;
#             font-size: 28px;
#             font-weight: bold;
#             color: #007bff;
#         }
#         .stButton>button {
#             width: 100%;
#             font-size: 18px;
#             padding: 10px;
#             border-radius: 10px;
#             transition: 0.3s ease-in-out;
#         }
#         .stButton>button:hover {
#             background-color: #ff4757 !important;
#             color: white !important;
#         }
#         .slider-text {
#             color: red;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # Dark Mode Toggle
# dark_mode = st.sidebar.checkbox("🌙 Dark Mode")
# if dark_mode:
#     st.markdown('<style>body{background-color: black; color: white;}</style>', unsafe_allow_html=True)

# # App Title
# st.markdown("<h2>🔒 Advanced Password Strength Meter</h2>", unsafe_allow_html=True)
# st.write("Check password strength and generate secure passwords.")

# # Password Strength Checker
# st.subheader("Enter Password:")
# password = st.text_input("Enter Password:", type="password")

# def check_strength(password):
#     length = len(password)
#     has_upper = bool(re.search(r'[A-Z]', password))
#     has_lower = bool(re.search(r'[a-z]', password))
#     has_digit = bool(re.search(r'[0-9]', password))
#     has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

#     strength = 0
#     if length >= 8:
#         strength += 1
#     if has_upper:
#         strength += 1
#     if has_lower:
#         strength += 1
#     if has_digit:
#         strength += 1
#     if has_special:
#         strength += 1

#     return strength

# if st.button("Check Strength"):
#     strength = check_strength(password)
#     if strength == 5:
#         st.success("✅ Strong Password!")
#     elif strength >= 3:
#         st.warning("⚠️ Moderate Password!")
#     else:
#         st.error("❌ Weak Password! Use uppercase, numbers, and special characters.")

# # Password Generator
# st.subheader("🔑 Generate Secure Password")

# length = st.slider("Password Length:", min_value=8, max_value=24, value=12)

# def generate_password(length):
#     characters = string.ascii_letters + string.digits + string.punctuation
#     return ''.join(random.choice(characters) for _ in range(length))

# if st.button("Generate Password"):
#     new_password = generate_password(length)
#     st.success(f"Generated Password: `{new_password}`")

# # Clear History Button
# if st.button("🗑️ Clear History"):
#     st.session_state.clear()

# # Footer
# st.markdown("<h4 style='text-align: center; color: #ff4757;'>Made with ❤️ by Mohsin</h4>", unsafe_allow_html=True)












import streamlit as st
import random
import string
import re

# Set Page Configuration
st.set_page_config(page_title="Advanced Password Strength Meter", layout="centered")

# Dark Mode Toggle
dark_mode = st.sidebar.checkbox("🌙 Dark Mode")

# Apply Dark Mode CSS dynamically
if dark_mode:
    st.markdown("""
        <style>
            body, .stApp {
                background-color: black !important;
                color: white !important;
            }
            h2, h3, label {
                color: #ffa502 !important;
            }
            .stButton>button {
                background-color: #ff4757 !important;
                color: white !important;
            }
            .stButton>button:hover {
                background-color: #ff6b81 !important;
            }
            .stSlider > div {
                color: white !important;
            }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
            body, .stApp {
                background-color: white !important;
                color: black !important;
            }
            h2, h3, label {
                color: #007bff !important;
            }
        </style>
    """, unsafe_allow_html=True)

# App Title
st.markdown("<h2>🔒 Advanced Password Strength Meter</h2>", unsafe_allow_html=True)
st.write("Check password strength and generate secure passwords.")

# Password Strength Checker
st.subheader("Enter Password:")
password = st.text_input("Enter Password:", type="password")

def check_strength(password):
    length = len(password)
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    strength = 0
    if length >= 8:
        strength += 1
    if has_upper:
        strength += 1
    if has_lower:
        strength += 1
    if has_digit:
        strength += 1
    if has_special:
        strength += 1

    return strength

if st.button("Check Strength"):
    strength = check_strength(password)
    if strength == 5:
        st.success("✅ Strong Password!")
    elif strength >= 3:
        st.warning("⚠️ Moderate Password!")
    else:
        st.error("❌ Weak Password! Use uppercase, numbers, and special characters.")

# Password Generator
st.subheader("🔑 Generate Secure Password")

length = st.slider("Password Length:", min_value=8, max_value=24, value=12)

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

if st.button("Generate Password"):
    new_password = generate_password(length)
    st.success(f"Generated Password: `{new_password}`")

# Clear History Button
if st.button("🗑️ Clear History"):
    st.session_state.clear()

# Footer
st.markdown("<h4 style='text-align: center; color: #ff4757;'>Made with ❤️ by Rehana Ali</h4>", unsafe_allow_html=True)
