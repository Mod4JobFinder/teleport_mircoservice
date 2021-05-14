from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route('/api/<location>')
def index(location):
  data = get_urban_salary_data(location)
  return data

def get_urban_salary_data(location):
  params = {"slug:": location}
  req = requests.get("https://api.teleport.org/api/urban_areas/slug:%s/salaries" % location)
  data = json.loads(req.content)
  salaries = {"salaries": data["salaries"]}
  return salaries

# if __name__ == '__main__':
#   app.run(debug=True)