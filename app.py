# 2. The Streamlit Web Layer (Zero AI Logic - Pure UI & Memory)
import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from main import chain

st.set_page_config(page_title="Odyssey AI Chatbot", page_icon="🤖")
st.title("🤖 Odyssey AI Chatbot")

# Persistent memory across re-runs
if "messages" not in st.session_state:
    st.session_state.messages = []

# Draw past conversation bubbles
for msg in st.session_state.messages:
    with st.chat_message("user" if isinstance(msg, HumanMessage) else "assistant"):
        st.markdown(msg.content)

# Floating input bar
if prompt := st.chat_input("Ask something..."):
    with st.chat_message("user"):
        st.markdown(prompt)

    # Streamlit natively streams LangChain's chain.stream()!
    with st.chat_message("assistant"):
        response = st.write_stream(
            chain.stream({"chat_history": st.session_state.messages, "question": prompt})
        )

    st.session_state.messages.append(HumanMessage(content=prompt))
    st.session_state.messages.append(AIMessage(content=response))