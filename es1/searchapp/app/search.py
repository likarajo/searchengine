from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from sinling import SinhalaTokenizer
from typing import List

from searchapp.constants import INDEX_NAME

HEADERS = {'content-type': 'application/json'}


class SearchResult():
    """Represents a song returned from elasticsearch."""
    def __init__(self, id_, title, track_rating, album_name, artist_name, artist_rating, lyrics):
        self.id = id_
        self.title = title
        self.track_rating = track_rating
        self.album_name = album_name
        self.artist_name = artist_name
        self.artist_rating = artist_rating
        self.lyrics = lyrics

    def from_doc(doc) -> 'SearchResult':
        return SearchResult(
                id_ = doc.meta.id,
                title = doc.title,
                track_rating = doc.track_rating,
                album_name = doc.album_name,
                artist_name = doc.artist_name,
                artist_rating = doc.artist_rating,
                lyrics = doc.lyrics
            )


def search(term: str, count: int) -> List[SearchResult]:
    client = Elasticsearch()

    # Elasticsearch 6 requires the content-type header to be set, and this is
    # not included by default in the current version of elasticsearch-py
    client.transport.connection_pool.connection.headers.update(HEADERS)

    tokenizer = SinhalaTokenizer()

    terms = tokenizer.tokenize(term)

    print(terms)

    if (term == "songs" or terms == []):
        s = Search(using=client, index=INDEX_NAME)
        docs = s.query({"bool": {"must": [{"match_all":{}}]}})[:count].execute()
        return [SearchResult.from_doc(d) for d in docs]

    if ('top' in term and ('songs' in term or 'artist' in term)):
        if ('songs' in term):
            bool_query = {
                    'bool': {
                        'must': {
                            'range': {
                                'track_rating.sort': {
                                    'gte': 0
                                }
                            }
                        },
                    }
                }
            s = Search(using=client, index="tokenized")
            docs = s.query(bool_query)[:count].sort('-track_rating.sort').execute()
            return [SearchResult.from_doc(d) for d in docs]

        if ('artis' in term):
            bool_query = {
                    'bool': {
                        'must': {
                            'range': {
                                'artist_rating': {
                                    'gte': 0
                                }
                            }
                        },
                    }
                }
            s = Search(using=client, index="tokenized")
            docs = s.query(bool_query)[:count].sort('-artist_rating.sort').execute()
            return [SearchResult.from_doc(d) for d in docs]


    elif ('artist' in terms and ':' in terms):
        terms.remove('artist')
        terms.remove(':')
        term = " ".join(terms)
        print('artist got here '+ term)
        bool_query = {
                    'bool': {
                        'must': {
                            'match': {
                                'artist_name': {
                                    'query': term,
                                    'operator': 'and',
                                    'fuzziness': 'AUTO'
                                }
                            }
                        },
                        'should': {
                            'multi_match': {
                                'query': term,
                                'fields': ['title^2','lyrics'],
                                'type': 'best_fields',
                                'operator': 'or'
                            }
                        }
                    }
                }
        s = Search(using=client, index="tokenized")
        docs = s.query(bool_query)[:count].execute()
        return [SearchResult.from_doc(d) for d in docs]
            
    elif ('lyrics' in terms and ':' in terms):
        terms.remove('lyrics')
        terms.remove(':')
        term = " ".join(terms)
        print('lyrics got here '+ term)
        bool_query = {
                    'bool': {
                        'must': {
                            'match': {
                                'lyrics': {
                                    'query': term,
                                    'operator': 'and',
                                    'fuzziness': '2'
                                }
                            }
                        },
                        'should': {
                            'multi_match': {
                                    'query': term,
                                    'fields': ['title^3','artist_name'],
                                    'type': 'best_fields',
                                    'operator': 'and'
                            }
                        }
                    }
                }
        s = Search(using=client, index=INDEX_NAME)
        docs = s.query(bool_query)[:count].execute()
        return [SearchResult.from_doc(d) for d in docs]

    elif ('album' in terms and ':' in terms):
        terms.remove('album')
        terms.remove(':')
        term = " ".join(terms)
        print('albuns got here '+ term)
        bool_query = {
                    'bool': {
                        'must': {
                            'match': {
                                'album_name': {
                                    'query': term,
                                    'operator': 'and',
                                    'fuzziness': 'AUTO'
                                }
                            }
                        },
                        'should': {
                            'multi_match': {
                                    'query': term,
                                    'fields': ['title^3','artist_name'],
                                    'type': 'best_fields',
                                    'operator': 'and'
                            }
                        }
                    }
                }
        s = Search(using=client, index=INDEX_NAME)
        docs = s.query(bool_query)[:count].execute()
        return [SearchResult.from_doc(d) for d in docs]

    else:
        term = " ".join(terms)
        print('else got here '+ term)
        s = Search(using=client, index=INDEX_NAME)
        title_query = {'match': {'title': {'query': term, 'operator': 'and', 'fuzziness': 'AUTO'}}}
        lyrics_query = {'match': {'lyrics': {'query': term, 'operator': 'and', 'fuzziness':'AUTO'}}}
        artist_query = {'match': {'artist_name': {'query': term, 'operator': 'and', 'fuzziness': 'AUTO'}}}
        dis_max_query = {'dis_max': {'queries': [title_query, artist_query]}, "tie-breaker":0.5}

        docs = s.query(dis_max_query)[:count].execute()

    #print(docs[0].title)

        return [SearchResult.from_doc(d) for d in docs]
