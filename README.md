# Espresso - Daily Digest App

Espresso is an application made to provide a daily digest of your favorite topics. This app uses the power of OpenAI and Metaphor APIs to fetch, process, and summarize the latest information on a list of topics provided by the user.

## Features

- Custom topic selection: Enter a list of topics you're interested in and Espresso will fetch related information for you.
- Digests: For each topic, Espresso generates a summarized digest.
- Security: User API keys are entered and handled privately.
- Streamlit UI: A sleek, interactive, and user-friendly interface provided through Streamlit.

## Files overview

- `app.py`: Main UI entry point. Handles the user inputs for API keys and topic of interest.
- `data_handlers.py`: Functions to get recent URLs through the Metaphor API, fetch the raw contents of the URLs and uses OpenAI's GPT-4 for summarizing.

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