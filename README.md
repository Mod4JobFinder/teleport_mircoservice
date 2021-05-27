# teleport_mircoservice
This flask microservice consumes urban city data from the teleport api. It then exposes a new end point showing tech job's maximum and minimum salary data for a specified city.
## Summary

  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installing](#installing)
  - [Endpoints](#endpoints)  
  - [How to test](#running-the-tests)
  - [Authors](#authors)

## Getting Started

These instructions will get you a copy of the project up and running on
your local machine for development and testing purposes. See deployment
for notes on how to deploy the project on a live system.

### Prerequisites

* __Python__

  - The project is built with Python 3.9.5

* __Flask__
  ```
  pip install flask
  ```

### Installing

1. Clone the repo
  ```
  $ git clone git@github.com:josephbudina/sweater_weather.git
  ```

2. Install gems
  ```
  $ bundle install
  ```

3. Create, migrate and seed rails database
  ```
  $ rails db:{create,migrate}
  ```

4. Set up Environment Variables:
  - run `bundle exec figaro install`
  - add the below variable to the `config/application.yml` if you wish to use the existing email microservice. Otherwise you replace it the value with service if desired.
  ```
    mapquest_key: <your mapquest api>
    open_weather_map_key: <your open weather api>
    flickr_key: <your flickr api>
  ```
## Endpoints
| HTTP verbs | Paths  | Used for |
| ---------- | ------ | --------:|
| GET | /api/v1/forecasts?location=denver,co | Finds different variants of weather in the specified city |
| GET | /api/v1/backgrounds?location=denver,co | Finds background image for given city |
| POST | /api/v1/users | Creates a new user |
| POST | /api/v1/sessions | Creates a new session for logged in user |
| POST | /api/v1/road_trips | Allows a user to set up a road trip |

## Running the tests
- To run the full test suite run the below in your terminal:
```
$ bundle exec rspec
```
- To run an individual test file run the below in tour terminal:
```
$ bundle exec rspec <file path>
```
for example: `bundle exec rspec spec/requests/api/v1/forecast/index_spec.rb`

## Authors
  - **Joseph Budina**

### Creating/registering user

> ```
> {
>   "data": {
>     "id": "null",
>     "type": "urban_area",
>     "attributes": [
>       {
>         "id": "integer",
>         "title": "string",
>         "min_salary": "float",
>         "max_salary": "float"
>       }
>     ]
>   }
> }

### Bad request or invalid credential per user post

> ```
> {
>   error: 'Bad Request for your parameter',
>   errors: "parameter is bad: #{reason}"
> }


### Response for Salary Page

>```
>{
>    'data': { 
>        'id': null,
>        'type': 'urban area'
>        'attributes': [
>            {  
>                'id': integer,
>                'title': string,
>                'min_salary': float,
>                'max_salary': float
>             }
>        ]
>     }
>}

### StackOverflow Microservice to Backend

> ```
> {
>  "data": [{
>    "id": "integer",
>    "type": "job_post",
>    "attributes":{
>      "title": "string",
>      "company": "string",
>      "category": "array(strings)",
>      "description": "string",
>      "location": "string",
>      "publish_date": "datetime",
>      "link": "string"
>      },
>      {...}
>   }]
> }
 

### session authentication

>```
>{ 
>    'email': string,
>    'password': string
>}
> 
> status: :ok

### Profile page

>```
>request
>
>{
>     'email': string,
>}
>
>response
>
>{
>    'data': { 
>        'id': null,
>        'type': 'user'
>        'attributes': {
>            'first_name': string,
>            'last_name': string,
>            'email': string,
>            'city': string,
>            'state': string (initial),
>            'zipcode': string,
>            'saved_jobs': [
>                {
>                    'job_title': string,
>                    'location': string,
>                    'company': string,
>                    'url': string
>                }
>            ]
>        }
>     }
>}

