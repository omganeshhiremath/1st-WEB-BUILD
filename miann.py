import streamlit as st

st.title("My First Age Calculator")
name = st.text_input("Enter your name: ")

if name:
    st.write("Hello", name, "!, Welcome to our website.")
    A = st.number_input("Enter your Birth year: ", min_value=1900, max_value=2026, step=1)
    
    if st.button("Calculate Age"):
        age = 2026 - A
        st.success(f"Your present Age is: {age}. Thank you for visiting our Website!")