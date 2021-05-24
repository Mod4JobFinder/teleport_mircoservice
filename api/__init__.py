import os
from flask import Flask, jsonify
import requests
import json


def create_app(test_config=None):
  app = Flask(__name__)
  if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
  else:
        app.config.from_mapping(test_config)

  try:
        os.makedirs(app.instance_path)
  except OSError:
      pass
  
  @app.route('/api/<location>')
  def index(location):
    data = jsonify(get_urban_salary_data(location))
    return data
    

  def get_urban_salary_data(location):
    params = {"slug:": location}
    req = requests.get("https://api.teleport.org/api/urban_areas/slug:%s/salaries" % location)
    data = json.loads(req.content)
    salaries = {"salaries": data["salaries"]}
    jobs = ['Data Analyst', 'Data Scientist', 'Mobile Developer', 'QA Engineer', 'Sofware Engineer', 'Systems Administrator', 'Web Developer']
    final_jobs = []
    for job in jobs:
      for salary in salaries['salaries']:
          if job == salary['job']['title']:
            final_jobs.append({
              'title': salary['job']['title'],
              'min': salary['salary_percentiles']['percentile_25'],
              'max': salary['salary_percentiles']['percentile_75']
            })
    return final_jobs
  return app