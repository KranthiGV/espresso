import streamlit as st
from data_handlers import createDigest

st.title("☕️ Espresso | Daily digest of your favorite topics")

# Get API keys from user
with st.form(key='api_form'):
   metaphor_api_key = st.text_input(label='Enter metaphor API key:', type='password')
   openai_api_key = st.text_input(label='Enter OpenAI API key:', type='password')
   submit_button = st.form_submit_button(label='Update')

# Get topics from user
with st.form(key='topics'):
    topics = st.text_input(label='What topics do you want digests for? (comma separated):')
    submit_button = st.form_submit_button(label='Create digests')

if submit_button:
    topics = topics.split(',')
    topics = [topic.strip() for topic in topics]

    # Collate digests
    digests = []
    with st.status('🪄Searching the magicland...', expanded=True) as status:
        for topic in topics:
            st.write(f"Summarizing {topic}...")
            digests.append(createDigest(topic, metaphor_api_key, openai_api_key))
        status.update(label="💫Digest created!", state="complete", expanded=False)

    # Display digests
    tabs = st.tabs(topics)
    for idx, tab in enumerate(tabs):
        with tab:
            for idx, item in enumerate(digests[idx]):
                if idx != 0:
                    st.divider()
                st.markdown(item)