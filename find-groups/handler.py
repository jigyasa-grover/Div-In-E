import os
import json
import requests
import sys
from urllib.parse import parse_qs

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    meetup_categories = {
        "culture": "10,16",
        "entertainment": "20,21",
        "wellbeing" : "9,14",
        "pride": "12",
    }

    query = os.environ['Http_Query']
    params = parse_qs(query)
    category = params["category"][0]

    category_id = meetup_categories[category]

    r = requests.get("https://api.meetup.com/find/groups?desc=india%2C+women&photo-host=public&page=5&sig_id=256722888&category=10%2C16&sig=3f7d46528c7210ccc257f08ead92d0923749e912")
    if r.status_code != 200:
        print("Error with meetup api, expected: %d, got: %d\n" % (200, r.status_code))
        sys.exit("Error with meetup api, expected: %d, got: %d\n" % (200, r.status_code))
    
    result = r.json()
    return "%s(%s)" % (params["callback"][0], result)
