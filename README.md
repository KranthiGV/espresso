# ☕️ Espresso - Daily Digest App
[Live Demo](https://digest.streamlit.app/)

Espresso is an application made to provide a daily digest of your favorite topics. This app uses the power of OpenAI and Metaphor APIs to fetch, process, and summarize the latest information on a list of topics provided by the user.

## Features

- Custom topic selection: Enter a list of topics you're interested in and Espresso will fetch related information for you.
- Digests: For each topic, Espresso generates a summarized digest.
- Security: User API keys are entered and handled privately.
- Streamlit UI: A sleek, interactive, and user-friendly interface provided through Streamlit.

## Files overview

- `app.py`: Main UI entry point. Handles the user inputs for API keys and topic of interest.
- `data_handlers.py`: Functions to get recent URLs through the Metaphor API, fetch the raw contents of the URLs and uses OpenAI's GPT-4 for summarizing.

## Demo

https://github.com/KranthiGV/espresso/assets/7046771/b516431d-02cf-44ec-8450-e90f9b7f0373

You can view and interact with a live demo of Espresso at: 

[Espresso - Daily Digest App](https://digest.streamlit.app/)

Simply enter your OpenAI and Metaphor API keys, and then provide your list of desired topics to start receiving your personalized digest. Enjoy Espresso shots of brief, recent news, and information tailor-made for you.


## Installation

1. Clone the repository: `git clone https://github.com/KranthiGV/espresso`
2. Navigate into the project directory: `cd espresso`
3. Install the required dependencies: `pip install -r requirements.txt`

## Usage

- Run the app: `streamlit run app.py`

The application will ask for two API keys:

- Metaphor API Key:
- OpenAI API Key:

After entering the keys, provide a list of topics you're interested to get digests for. These topics need to be comma-separated.
  
The application will then collate digests and display them tab-wise for each topic.
