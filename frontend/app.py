import streamlit as st
import requests

st.title("AI Data & Research Intelligence Agent")

uploaded_file = st.file_uploader("Upload CSV/Excel or PDF", type=["csv", "xlsx", "pdf"])
question = st.text_input("Enter your query")

if uploaded_file and question:
    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())

    with open(uploaded_file.name, "rb") as f:
        response = requests.post(
            "http://localhost:8000/query",
            data={"question": question},
            files={"file": f}
        )

    st.json(response.json())
