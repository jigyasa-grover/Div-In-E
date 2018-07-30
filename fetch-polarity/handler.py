import os
import requests
import sys
from urllib.parse import parse_qs
import json

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    query = os.environ['Http_Query']
    params = parse_qs(query)
    text = params["text"][0]

    gateway_hostname = os.getenv("gateway_hostname", "gateway") # uses a default of "gateway" for when "gateway_hostname" is not set

    r = requests.get("http://" + gateway_hostname + ":8080/function/sentimentanalysis", data= text)

    result = r.json()
    return "%s(%s)" % (params["callback"][0], result)
