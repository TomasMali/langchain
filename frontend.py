import streamlit as st
import numpy as np
import doit as ag


st.title("Echo Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    respond = ag.ask(prompt)
    # Display user message in chat message container
    st.chat_message("user").markdown(respond)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
        # st.bar_chart(np.random.randn(30, 3))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})