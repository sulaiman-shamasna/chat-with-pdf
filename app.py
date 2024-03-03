import streamlit as st
from ingestor import PdfIngestor
from footers import footer
import os

# Set the title for the Streamlit app
st.title("🦜🔗 - Chat with a PDF File")

# OpenAI Credentials
with st.sidebar:
    st.title('💬 Chat with your Data')
    if 'OPENAI_API_KEY' in st.secrets:
        st.success('API key already provided!', icon='✅')
        openai_api = st.secrets['OPENAI_API_KEY']
    else:
        openai_api = st.text_input('Enter **OPENAI_API_KEY**:', type='password')
        if not (openai_api.startswith('sk-') and len(openai_api)==51):
            st.warning('Invalid credentials. Please try again!', icon='⚠️')
        else:
            st.success('Proceed by uploading your file, then start chatting!', icon='👇')
os.environ['OPENAI_API_KEY'] = openai_api

# Create a file uploader in the sidebar
uploaded_file = st.sidebar.file_uploader("Upload File", type="pdf")

with st.sidebar:
    st.markdown('📖 Learn more about [LangChain](https://www.deeplearning.ai/short-courses/)')

if uploaded_file:
    file_ingestor = PdfIngestor(uploaded_file)
    file_ingestor.handlefileandingest()

st.markdown(footer, unsafe_allow_html=True)