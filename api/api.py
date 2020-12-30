import time
from flask import Flask
from flask import request, jsonify
from flask_cors import CORS, cross_origin
from search import Search

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/search": {"origins": "*"}})

@app.route('/', methods=['GET'])
def home():
    return "Home"

@app.route('/welcome/', methods=['GET'])
def welcome():
    return {'msg': "Welcome"}

@app.route('/time/', methods=['GET'])
def get_current_time():
    return {'time': time.time()}

@app.route('/search/', methods=['GET']) 
@cross_origin(origin='localhost', headers=['Content- Type','Authorization'])
def search():
    if 'q' in request.args:
        keywords = request.args['q']
    else:
        keywords = "Avengers" 
    print("api_keywords: ", keywords)
    items = []
    s = Search(index_name='netflix')
    s.index_data()
    response = s.find(keywords)
    if response:
        results = s.process_result(response)
        for res in results:
            title = res['title']
            _type = res['type']
            release_year = res['release_year']
            director = res['director']
            rating = res['rating']
            description = res['description']
            duration = res['duration']
            cast = res['cast']
            item = {
                'title': title,
                'type': _type,
                'release_year': release_year,
                'director': director,
                'rating': rating,
                'description': description,
                'duration': duration,
                'cast': cast
            }
            if item not in items:
                items.append(item)
    else:
        item = {
            'title': None,
            'type': None,
            'release_year': None,
            'director': None,
            'rating': None,
            'description': None,
            'duration': None,
            'cast': None
        }
        items.append(item)
    print(items)
    return {'items': items}
