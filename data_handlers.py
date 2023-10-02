from datetime import datetime, timedelta
from metaphor_python import Metaphor

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
    response = metaphor.get_content(ids)

    # TODO(krgv): Add error handling for response

    return response

def processRecentURLsForTopic(topic, metaphor_api_key):
    response = fetchRecentURLs(topic, metaphor_api_key)
    ids = [item['id'] for item in response['results']]
    contents = fetchRawContentsForIds(ids, metaphor_api_key)
    return contents

def createDigest(topic, metaphor_api_key):
    contents = processRecentURLsForTopic(topic, metaphor_api_key)

    contents = [content['content'] for content in contents]


    return contents