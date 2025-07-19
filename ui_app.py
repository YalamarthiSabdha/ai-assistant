import streamlit as st
from command_parser import parse_command
from voice import listen
import os

# Streamlit UI setup
st.set_page_config(page_title="AI Assistant", layout="centered")
st.title("🤖 Your Local AI Assistant")
st.caption("Control files/folders using voice or text commands!")

# Input: Default path
base_path = st.text_input(
    "📁 Enter default path for file/folder operations:",
    value=os.getcwd(),
    key="base_path"
)

# Divider
st.divider()

# Input: Command (text or voice)
input_text = st.text_input("💬 Type your command here", key="input_command")

# Voice input
if st.button("🎤 Speak"):
    input_text = listen()
    st.success(f"🗣️ You said: {input_text}")

# Run command button
if st.button("🚀 Run Command"):
    if input_text and base_path:
        result = parse_command(input_text, base_path)
        st.subheader("📄 Result")
        st.success(result)
    else:
        st.warning("⚠️ Please provide both a base path and a command.")
