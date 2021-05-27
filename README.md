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
  $ git clone git@github.com:Mod4JobFinder/teleport_mircoservice.git
  ```

2. Install requirements
  ```
  $ pip install -r requirements.txt
  ```
  ```
## Endpoint
| HTTP verbs | Paths  | Used for |
| ---------- | ------ | --------:|
| GET | /api/denver,co | Finds different salaries for specified city |

## Running the tests
- To run the full test suite run the below in your terminal:
```
$ coverage run


## Authors
  - **Joseph Budina**
