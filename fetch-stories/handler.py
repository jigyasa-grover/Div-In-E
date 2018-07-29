import json
import os

# filters stories to include person category and 
# exclude person tags
def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    category = "cuisines"
    person_tags = ["India"]

    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, 'json/story.json')

    with open(path) as f:
        data = json.load(f)
    
    result_story = []
    for story in data["story"]:
        keep_story = True

        if category == story["category"]:
            for tags in story["tag"]:

                if tags in person_tags:
                    keep_story = False
                    break
        else:
            keep_story = False

        if keep_story:
            result_story.append(story)


    #print(result_story)

    return json.dumps(result_story)
            
