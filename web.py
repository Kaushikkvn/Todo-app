import streamlit as st
import functions
st.title("MY TO-DO APP")
todos=functions.get_todo()
for todo in todos:
    st.checkbox(todo)