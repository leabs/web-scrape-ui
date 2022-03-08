from flask import Flask, render_template, request
import json

from scraper import Webpage


# Initialize the flask app
app = Flask(__name__, static_folder='static')

# serve the page with a GET request
@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')

# this "/get_results" url will return the results
# like an API, with POST method
@app.route('/get_results', methods=['POST'])
def get_results():
    """
    Returns the scraped results for a set of inputs.

    Inputs:

    The URL, the type of content to scrap and class/id name.
    This comes from the get_results() function in script.js

    Output:

    Returns a JSON list of the results
    """

    # Decode the json data and turn it into a python dict
    post_data = json.loads(request.data.decode())

    # Extract the inputs from the JSON data
    req_url = post_data.get('url')
    req_type = post_data.get('type')
    req_selector = post_data.get('selector')

    results = []

    # Each of the types of extraction is handled here
    if req_type == 'head':
        results = Webpage(req_url).get_head_tag()
    elif req_type == 'content':
        results = Webpage(req_url).get_all_contents()
    elif req_type == 'class':
        results = Webpage(req_url).get_content_by_class(req_selector)
    elif req_type == 'id':
        results = Webpage(req_url).get_content_by_id(req_selector)
    elif req_type == 'images':
        results = Webpage(req_url).get_all_images()

    # The scraped results are turned into JSON format 
    # and sent to the frontend
    serialized = json.dumps(results)

    return serialized



if __name__ == '__main__':
    app.run()