import streamlit as st

st.title("DATA APP")
st.header("WELCOME TO WEB!")
st.write("This is a sample webapp")


name=st.text_input("NAME?")
if name:
    st.success(f"HELLO,{name}")

age=st.slider("AGE?",1,100,25)
st.write(f"YOU SELECTED {age}")