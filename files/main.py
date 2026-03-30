import streamlit as st
import dotenv
import langchain
from langchain_google_genai import GoogleGenerativeAI
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()
import os
os.environ["GOOGLE_API_KEY"]=os.getenv("gemini")



st.set_page_config(page_title="chat bot", page_icon="🧠")

st.title("Chat bot with langchain and streamlit")

if "conv" not in st.session_state:
    st.session_state["conv"]=[]
    st.session_state["memory"]=[]
    st.session_state["memory"].append(("system","You are an engineer with 10 years experience"))

for y in st.session_state["conv"]:

    with st.chat_message(y["role"]):
        st.write(y["content"])

prompt=st.chat_input("type your queries")

if prompt:
    st.session_state["conv"].append({"role":"user","content":prompt})
    st.session_state["memory"].append(("user",prompt))

    with st.chat_message("user"):
        st.write(prompt)

    model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

    response=model.invoke(st.session_state["memory"])

    with st.chat_message("ai"):
        st.write(response.content)

    st.session_state["conv"].append({"role":"ai","content":response.content})
    st.session_state["memory"].append(("ai",response.content))










