from datetime import datetime, timedelta
from metaphor_python import Metaphor
import openai

def lastWeekDate():
    today = datetime.now()
    seven_days_earlier = today - timedelta(days=7)
    formatted_date = seven_days_earlier.strftime('%Y-%m-%d')
    return formatted_date

def fetchRecentURLs(topic, metaphor_api_key):
    metaphor = Metaphor(metaphor_api_key)
    response = metaphor.search(topic,
                               num_results=2,
                               use_autoprompt=True,
                               start_published_date=lastWeekDate())
    
    # TODO(krgv): Add error handling for response

    return response

def fetchRawContentsForIds(ids, metaphor_api_key):
    metaphor = Metaphor(metaphor_api_key)
    response = metaphor.get_contents(ids)

    # TODO(krgv): Add error handling for response

    return response

def processRecentURLsForTopic(topic, metaphor_api_key):
    response = fetchRecentURLs(topic, metaphor_api_key)
    ids = [item.id for item in response.results]
    contents = fetchRawContentsForIds(ids, metaphor_api_key)
    return contents

def createPromptForSummary(contents):
    base = f"""
         Here's HTML extracts of a few webpages. Summarize all the content into a single piece of clear text. Do not talk about summarizing. Do not refer to first, second, third webpages, etc.
         
         """
    for doc in contents:
        base += f"""
        Page title: {doc.title}
        Page content: 
        {doc.extract}
        """

    return base

def listSources(contents):
    base = "### Here are the sources:"
    for doc in contents:
        base += f"[{doc.title}]({doc.url})"
        base += f"""  
        """


    return base


def createDigest(topic, metaphor_api_key, openai_api_key):
    openai.api_key = openai_api_key
    response = processRecentURLsForTopic(topic, metaphor_api_key)
    
    final_prompt = createPromptForSummary(response.contents)

    completion = openai.ChatCompletion.create(model="gpt-4", messages=[{"role": "user", "content": final_prompt}])
    
    summary = completion.choices[0].message.content
    sources = listSources(response.contents)

    return [summary, sources]

