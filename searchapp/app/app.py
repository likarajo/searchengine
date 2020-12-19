from flask import Flask, render_template, request

from searchapp.data import all_songs
from searchapp.app.search import search

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    """
    Search for products across a variety of terms, and show 9 results for each.
    """
    search_terms = []

    num_results = 10
    songs_by_category = [(t, search(t, num_results)) for t in search_terms]
    return render_template(
        'index.html',
        songs_by_category=songs_by_category,
    )


@app.route('/search', methods=['GET', 'POST'])
def search_single_song():
    """
    Execute a search for a specific search term.

    Return the top 50 results.
    """
    query = request.args.get('search')
    num_results = 50
    songs_by_category = [(query, search(query, num_results))]

    for songs in songs_by_category:
        if len(songs) == 1:
            songs[1][0] = {"title": "No Results Found"}
    return render_template(
        'index.html',
        songs_by_category=songs_by_category,
        search_term=query,
    )


@app.route('/song/<int:song_id>')
def single_song(song_id):
    """
    Display information about a specific product
    """

    song = str(all_songs()[song_id - 1])

    return render_template(
        'song.html',
        song_json=song,
        search_term='',
    )
