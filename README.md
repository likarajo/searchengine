# Search Engine

A Search engine built using ElasticSearch and Python

## Development Environment

* MacOS 11.0.1
* ElasticSearch 7.10.1
* JVM 15.0.1
* Python 3.9.0
* pip 20.3.3

## Requirements

* ElasticSearch Python client: https://elasticsearch-py.readthedocs.io/en/master
* pandas 1.1.5

## Set up

1. Install Elastic Search: https://www.elastic.co/guide/en/elasticsearch/reference/7.10/brew.html
2. Create and activate a virtual environment to run the project.
	```
	python -m venv venv
	source venv/bin/activate
	```
3. Install necessary python requirements
	```
	pip3 install -r requirements.txt
	```
4. Start ElasticSearch
	```
	elasticsearch
	```
	It runs on http://localhost:9200/
5. Run the search app
	```
	python main.py
	```