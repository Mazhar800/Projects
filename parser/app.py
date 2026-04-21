from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

# Model
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    task="conversational"
)

model = ChatHuggingFace(llm=llm)

st.title("🤖 MH---AI ")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# input state (IMPORTANT)
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# Show chat history
for msg in st.session_state.messages:
    st.write(msg)

# FORM (for Enter + button)
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input(
        "Type your message:",
        key="user_input"
    )
    submit = st.form_submit_button("Send")

# When user sends message
if submit and user_input:
    st.session_state.messages.append(f"🧑 You: {user_input}")

    response = model.invoke(user_input)

    st.session_state.messages.append(f"🤖 AI: {response.content}")

    # refresh page
    st.rerun()