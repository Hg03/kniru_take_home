#pip install streamlit langchain openai faiss-cpu tiktoken

import streamlit as st
from streamlit_chat import message
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.vectorstores import FAISS
import tempfile
from markdownlit import mdlit

st.set_page_config(layout='wide')

mdlit('# [green]Personal Financial[/green] [yellow]Chatbot[/yellow] 🤖')

col1, col2 = st.columns(2)

with col1:
    with st.expander('Enter your API key'):
        user_api_key = st.text_input(
            label="#### Your OpenAI API key (In case, mine will exhausted) 👇",
            placeholder="sk-.....",
            type="password")

with col2:
    with st.expander('Upload your financial related csv file'):
        uploaded_file = st.file_uploader("upload", type="csv")

if uploaded_file :
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_file_path = tmp_file.name

    loader = CSVLoader(file_path=tmp_file_path, encoding="utf-8")
    data = loader.load()

    embeddings = OpenAIEmbeddings(openai_api_key=user_api_key)
    vectors = FAISS.from_documents(data, embeddings)

    chain = ConversationalRetrievalChain.from_llm(llm = ChatOpenAI(temperature=0.0,model_name='gpt-3.5-turbo', openai_api_key=user_api_key),
                                                                      retriever=vectors.as_retriever())

    def conversational_chat(query):
        
        result = chain({"question": query, "chat_history": st.session_state['history']})
        st.session_state['history'].append((query, result["answer"]))
        
        return result["answer"]
    
    if 'history' not in st.session_state:
        st.session_state['history'] = []

    if 'generated' not in st.session_state:
        st.session_state['generated'] = ["Hello ! Ask me anything about " + uploaded_file.name + " 🤗"]

    if 'past' not in st.session_state:
        st.session_state['past'] = ["Hey ! 👋"]
        
    #container for the chat history
    response_container = st.container()
    #container for the user's text input
    container = st.container()

    with container:
        with st.form(key='my_form', clear_on_submit=True):
            
            user_input = st.text_input("Query:", placeholder="Talk about your csv data here (:", key='input')
            submit_button = st.form_submit_button(label='Send')
            
        if submit_button and user_input:
            output = conversational_chat(user_input)
            
            st.session_state['past'].append(user_input)
            st.session_state['generated'].append(output)

    if st.session_state['generated']:
        with response_container:
            for i in range(len(st.session_state['generated'])):
                message(st.session_state["past"][i], is_user=True, key=str(i) + '_user', avatar_style="big-smile")
                message(st.session_state["generated"][i], key=str(i), avatar_style="thumbs")
    
with st.container():
    mdlit('## [blue]About : [/blue]')
    mdlit('First of all, Thanks 🙏 to [kniru](https://kniru.com) for giving me this opportunity. I have referred the [problem statement](https://kniru.notion.site/Personal-Financial-Management-Chatbot-with-OpenAI-b65b7e1ed83542b8937e1d811bc932a6). In this project<br>1. I have used the data provided in the problem statement and created a synthetic version of it.<br>2. ')
    mdlit('**Project Repository - [kniru take home](https://github.com/Hg03/kniru_take_home)**')
    mdlit('**Linkedin - [harish gehlot](https://www.linkedin.com/in/harish-gehlot-5338a021a/)**')

#streamlit run tuto_chatbot_csv.py