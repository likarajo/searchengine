# Search Engine
A Search engine built using Elasticsearch and Python

MacOS 11.0.1

Python 3.7.0

ElasticSearch 7.10 

Flask 1.0 or higher if using a container (docker, kubernetes, etc.)

Dataset used for indexing is included inside searchapp/sinhala_songs_corpus.json

# Instructions for the setup
0. Install ElasticSearch https://www.elastic.co/guide/en/elasticsearch/reference/7.10/brew.html
1. Clone the repository
2. Create and activate a virtual environment to run the project.
	```
	python3 -m venv venv
	source venv/bin/activate
	```
3. Install necessary python requirements
	```
	pip3 install -r requirements.txt
	```
	(If there is trouble with getting the "Sinling" dependancy from the git repository, add it manually from https://github.com/ysenarath/sinling)
4. setup searchapp
	```
	pip3 install -e .
	```
5. Start ElasticSearch
	```
	elasticsearch
	```
	It runs on http://localhost:9200/
5. While elasticsearch node/nodes are running, create indices in nodes.
	```
	python3 searchapp/index_songs.py
	```
6. Run the flask app.
	```
	python3 searchapp/run.py
	```
7. Goto http://localhost:5000 to view the flask app and do searches.

