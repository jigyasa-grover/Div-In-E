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
    if category == "culture":
        r = requests.get("https://api.meetup.com/find/groups?photo-host=public&page=16&text=women&sig_id=256722888&category=10%2C16&sig=a0ca77ee1dce3986f1613939f0841f9daca3317e")
    elif category == "wellbeing":
        r = requests.get("https://api.meetup.com/find/groups?photo-host=public&page=16&text=women&sig_id=256722888&category=9%2C14&sig=1d0890ae2bdab37ba97e1932ee8329e7ee783caa")
    elif category == "pride":
        r = requests.get("https://api.meetup.com/find/groups?photo-host=public&page=16&text=women&sig_id=256722888&category=12&sig=5df30d07e1de83ea0a44696c74bfc420ac76f396")
    
    if r.status_code != 200:
        print("Error with meetup api, expected: %d, got: %d\n" % (200, r.status_code))
        sys.exit("Error with meetup api, expected: %d, got: %d\n" % (200, r.status_code))
    
    result = r.json()
    return "%s(%s)" % (params["callback"][0], result)
