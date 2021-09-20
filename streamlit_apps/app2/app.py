import streamlit as st

word = st.text_input("Write a word to see it in reverse.")

st.write(word[::-1])