import streamlit as st
import requests

API_URL="https://emailprocessingapp-9.onrender.com/generate"

st.title("Email Assistant For User")

email=st.text_area("Paste email here....")

def call_backend(email_input):
    res=requests.post(API_URL,json={"email":email_input})
    return res.json().get("result",res.json().get("error", "No output returned"))

if st.button("Generate"):
    if email.strip():
        with st.spinner("Processing..."):
            try:
                output=call_backend(email)
                st.subheader("Output")
                st.write(output)
            except Exception as e:
                st.error("Error: "+str(e))
    else:
        st.warning("Please paste an email first...")