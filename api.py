from flask import Flask
import requests
import json

app = Flask(__name__)


@app.route('/<string:location>')
def index(location):
  data = new_func(location)
  return data

def new_func(location):
    req = requests.get('https://api.teleport.org/api/cities/?search=denver')
    data = json.loads(req.content)
    return data['_embedded']['city:search-results'][0]['_links']['city:item']['href']

if __name__ == '__main__':
    app.run(debug=True)