import streamlit as st

st.title("☕️ Espresso | Daily digest of your favorite topics")

with st.form(key='api_form'):
   metaphor_api_key = st.text_input(label='Enter metaphor API key:')
   openai_api_key = st.text_input(label='Enter OpenAI API key:')
   submit_button = st.form_submit_button(label='Update')

with st.form(key='topics'):
    topics = st.text_input(label='Enter topics (comma separated):')
    submit_button = st.form_submit_button(label='Create digest')

if submit_button:
    topics = topics.split(',')
    topics = [topic.strip() for topic in topics]

    tabs = st.tabs(topics)

    for tab in tabs:
        tab.write("This is the " + tab.label + " tab.")