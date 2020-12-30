# Search Engine

A Search engine built using ElasticSearch and Python

![](app_screenshot.png)

## Environment

* MacOS 11.0.1
* ElasticSearch 7.10.1
* JVM 15.0.1
* Python 3.9.0
* pip 20.3.3
* node 15.5.0
* npm 7.3.0
* yarn 1.22.10

## Requirements

* [ElasticSearch Python client](https://elasticsearch-py.readthedocs.io/en/master)
* pandas
* flask

## Steps

0. Clone the repository

1. [Install Elastic Search](https://www.elastic.co/guide/en/elasticsearch/reference/7.10/brew.html)

2. Start ElasticSearch

  ```sh
  elasticsearch
  ```
  
  It runs on <http://localhost:9200/>

3. Create and activate Virtual environment `/api/venv`
  
  ```sh
  cd api
  python -m venv venv
  source venv/bin/activate
  ```

4. Install necessary python requirements

  ```sh
  pip3 install -r requirements.txt
  ```

5. Install packages

  ```sh
  cd ..
  npm install
  ```

6. Run the React Front End

  ```sh
  yarn start
  ```
  
  React front end runs on <http://localhost:3000/>

7. Run the Flask Back End
  
  ```sh
  yarn start-api
  ```

  Flask back end runs on <http://localhost:5000/>

8. Search in the app <http://localhost:3000/>

