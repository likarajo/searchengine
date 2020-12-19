# IR_Search_Engine
A Search engine built using Elasticsearch and python with a basic UI using Flask

python version - 3.7.7

Elasticsearch version used - 7.7.1 (Warning:- If using an elasticsearch version < 7.0 might have to change indexing and mappings 
to include doc_types and type declerations)

Flask version - Upgrade to 1.0 or higher if using a container(docker, kubernetes, etc.)

Dataset used for indexing is included inside searchapp/sinhala_songs_corpus.json

# Instructions for the setup
1. Clone or download the repository (Linux/Unix OS is preferred)
2. Create a virtual environment to run the project. Activate the environment (using virtualenv)
	```
	python3 -m venv venv
	source venv/bin/activate
	```
3. Install necessary python requirements
	```
	pip install -r requirements.txt
	```
	(If you had trouble with getting the "Sinling" dependancy from the git repository, Add it manually from https://github.com/ysenarath/sinling)
4. setup searchapp
	```
	pip install -e .
	```
5. While elasticsearch node/nodes are running, create indices in nodes.
	```
	python searchapp/index_songs.py
	```
6. Run the flask app.
	```
	python searchapp/run.py
	```
7. Goto http://localhost:5000 to view the flask app and do searches.

