import json
import os
import textwrap
_all_songs = None


class SongData():
   
    def __init__(self, id_, track_id, track_name_en, track_name_si, track_rating, album_name_en, album_name_si, artist_name_en, artist_name_si, artist_rating, lyrics):
        self.title = track_name_si
        self.title_singlish = track_name_en
        self.track_rating = track_rating
        self.album_name = album_name_si
        self.album_name_singlish = album_name_en
        self.artist_name = artist_name_si
        self.artist_name_singlish = artist_name_en
        self.artist_rating = artist_rating
        self.lyrics = lyrics
        self.id = id_

    def __str__(self):
        return textwrap.dedent("""\
            
            Title: {}
            TrackRating: {}
            Album: {}
            Artist: {}
            ArtistRating: {}
            Lyrics: 

            {}
        """).format(self.title, self.track_rating, self.album_name,
                    self.artist_name, self.artist_rating, self.lyrics)


def all_songs():
    """
    Returns a list of All SongData objects, loaded from
    searchapp/<data_set>.json
    """

    global _all_songs

    if _all_songs is None:
        _all_songs = []

        # Load the songs corpus json from the same directory as this file.
        dir_path = os.path.dirname(os.path.realpath(__file__))
        print(dir_path)
        songs_path = os.path.join(dir_path, 'sinhala_songs_corpus.json')
        with open(songs_path, encoding="utf-8") as songs_file:
            for idx, song in enumerate(json.load(songs_file, strict=False)):
                id_ = idx + 1  # ES indexes must be positive integers, so add 1
                song_data = SongData(id_, **song)
                _all_songs.append(song_data)

    return _all_songs
