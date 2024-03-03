import streamlit as st
from ingestor import PdfIngestor

# Set the title for the Streamlit app
st.title("Chat with PDF - 🦜🔗")

# Create a file uploader in the sidebar
uploaded_file = st.sidebar.file_uploader("Upload File", type="pdf")

if uploaded_file:
    file_ingestor = PdfIngestor(uploaded_file)
    file_ingestor.handlefileandingest()