import streamlit as st
from openai import OpenAI
# from langchain.llms import OpenAI
# from langchain.chat_models import ChatOpenAI
# from utils import load_pdf_content, split_text, summarize


# OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

# Page title
st.set_page_config(page_title='AudioTranscript')
st.title('AudioTranscript')

openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

# File input
file = st.file_uploader(label='Upload MP3 file (Limit 25MB per file)',
                        type=['mp3', 'MP3', 'm4a', 'M4A'],
                        )

transcription = None

if file and openai_api_key.startswith('sk-'):
    with st.spinner('Calculating...'):
        client = OpenAI(api_key=openai_api_key)
        # llm = OpenAI(temperature=0, openai_api_key=openai_api_key)
        # llm = ChatOpenAI(temperature=0,
        #                  openai_api_key=OPENAI_API_KEY,
        #                  model='gpt-3.5-turbo')

        transcription = client.audio.transcriptions.create(
            model='whisper-1',
            file=file,
            response_format='text'
        )
        # docs = split_text(llm, text)
        # output = summarize(llm, docs)

if transcription:
    st.info(transcription)
