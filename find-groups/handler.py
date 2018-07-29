import os
import json
import requests
def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    gateway_hostname = os.getenv("gateway_hostname", "gateway")
    r = requests.get("https://api.meetup.com/find/groups?photo-host=public&page=20&text=india&sig_id=259945822&lon=-122.19738189999998&lat=37.4715136&sig=e6b59f26bc83740c9888e15bedaa57e3b36ee7ba")
    if r.status_code != 200:
        print("Error with meetup api, expected: %d, got: %d\n" % (200, r.status_code))
        sys.exit("Error with meetup api, expected: %d, got: %d\n" % (200, r.status_code))
    result = r.json()
    print(result)
    return result
