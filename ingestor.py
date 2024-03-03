import streamlit as st
from langchain.document_loaders import PyMuPDFLoader
from streamlit_chat import message
import tempfile
from langchain.embeddings import OpenAIEmbeddings


from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma

from langchain_community.chat_models import ChatOpenAI

from langchain.memory import ConversationBufferMemory

from langchain.chains import RetrievalQA

DB_CHROMA_PATH = 'vectorstore/db1'

class PdfIngestor:
    def __init__(self, uploaded_file):
        self.uploaded_file = uploaded_file
        
    def handlefileandingest(self):
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(self.uploaded_file.getvalue())
            tmp_file_path = tmp_file.name

        loader = PyMuPDFLoader(file_path=tmp_file_path)
        data = loader.load()

        # Create embeddings using Sentence Transformers
        embeddings = OpenAIEmbeddings()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        chunks = text_splitter.split_documents(data)

        db = Chroma.from_documents(chunks, embeddings) 
        # db.save_local(DB_CHROMA_PATH)

        llm = ChatOpenAI(model_name="gpt-3.5-turbo",
                           temperature=0,
                           )
        
        memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
            )
        
        retriever = db.as_retriever(search_type="similarity",
                                    search_kwargs={"k": 2},
                                    )
        
        chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever,
            memory=memory,
            )
        
        # Create a conversational chain
        # Function for conversational chat
        def conversational_chat(query):
            result = chain({"query": query})
            st.session_state['history'].append((query, result['result']))
            return result['result']

        # Initialize chat history
        if 'history' not in st.session_state:
            st.session_state['history'] = []

        # Initialize messages
        if 'generated' not in st.session_state:
            st.session_state['generated'] = ["Hello! Ask me about " + self.uploaded_file.name + " 🤗"]

        if 'past' not in st.session_state:
            st.session_state['past'] = ["Hey ! 👋"]

        # Create containers for chat history and user input
        response_container = st.container()
        container = st.container()

        # User input form
        with container:
            with st.form(key='my_form', clear_on_submit=True):
                user_input = st.text_input("Query:", placeholder="Enter your question, please! 💬", key='input')
                submit_button = st.form_submit_button(label='Send')

            if submit_button and user_input:
                output = conversational_chat(user_input)
                st.session_state['past'].append(user_input)
                st.session_state['generated'].append(output)

        # Display chat history
        if st.session_state['generated']:
            with response_container:
                for i in range(len(st.session_state['generated'])):
                    message(st.session_state["past"][i], is_user=True, key=str(i) + '_user', avatar_style="adventurer")
                    message(st.session_state["generated"][i], key=str(i), avatar_style="thumbs")