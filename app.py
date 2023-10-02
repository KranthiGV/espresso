import streamlit as st
from data_handlers import createDigest

st.title("☕️ Espresso | Daily digest of your favorite topics")

with st.form(key='api_form'):
   metaphor_api_key = st.text_input(label='Enter metaphor API key:', type='password')
   openai_api_key = st.text_input(label='Enter OpenAI API key:', type='password')
   submit_button = st.form_submit_button(label='Update')

with st.form(key='topics'):
    topics = st.text_input(label='Enter topics (comma separated):')
    submit_button = st.form_submit_button(label='Create digest')

if submit_button:
    topics = topics.split(',')
    topics = [topic.strip() for topic in topics]

    digests = []
    with st.status('🪄Searching the magicland...', expanded=True) as status:
        for topic in topics:
            st.write(f"Summarize {topic}...")
            digests.append(createDigest(topic, metaphor_api_key, openai_api_key))
        status.update(label="💫Digest created!", state="complete", expanded=False)



    tabs = st.tabs(topics)

    
    for idx, tab in enumerate(tabs):
        with tab:
            for idx, item in enumerate(digests[idx]):
                if idx != 0:
                    st.divider()
                st.markdown(item)