from flask import Flask, request
import requests
import json

app = Flask(__name__)


@app.route('/<location>')
def index(location):
  data = get_urban_salary_data(location)
  return data

def get_city_id(location):
    # location = request.args['location']
    # breakpoint()
    params = {"search": location}
    req = requests.get('https://api.teleport.org/api/cities', params=params)
    data = json.loads(req.content)
    return data['_embedded']['city:search-results'][0]['_links']['city:item']['href']

def get_city_info(location):
    # location = request.args['location']
    req = requests.get(get_city_id(location))
    data = json.loads(req.content)
    return data

def get_urban_data(location):
    req = requests.get(get_city_info(location)['_links'][ "city:urban_area"]["href"])
    data = json.loads(req.content)
    return data

def get_urban_salary_data(location):
    req = requests.get(get_urban_data(location)['_links'][ "ua:salaries"]["href"])
    data = json.loads(req.content)
    return data

if __name__ == '__main__':
    app.run(debug=True)