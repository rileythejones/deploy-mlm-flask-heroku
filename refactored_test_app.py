import pandas as pd
import pdb
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from spider import spider_plot
from functions import preprocess, create_model, suggest_songs
from model import Song

app = Flask(__name__)

engine = create_engine('sqlite:///db.sqlite3', echo=False)

# DB = SQLAlchemy(app)
# DB.drop_all()
# DB.create_all()

# df = pd.read_csv('SpotifyAudioFeaturesApril2019.csv')
# df.to_sql('songs', index=False, con=engine)
songs_df =  pd.read_sql_table('songs', 'sqlite:///db.sqlite3')

X = songs_df[songs_df.columns[3:]]
y = songs_df[songs_df.columns[:3]]


test_song2 = {"artist_name": "Rick Astley", "track_id": "7GhIk7Il098yCjg4BQjzvb", "track_name": "Never Gonna Give You Up", "acousticness": 0.135, "danceability": 0.727, "duration_ms": 212827, "energy": 0.939, "instrumentalness": 4.35e-05, "key": 8, "liveness": 0.151, "loudness": -11.855, "mode": 1, "speechiness": 0.0369, "tempo": 113.33, "time_signature": 4, "valence": 0.916, "popularity": 66}
my_model = create_model(preprocess(X))

@app.route('/')
def root():
    return "hello"

@app.route('/pred', methods=['GET'])
def returnAll():
    
    song_dict = test_song2
    song_dict.update((x, [y]) for x, y in song_dict.items())
    song_df = pd.DataFrame.from_dict(song_dict)
    song_df = song_df[song_df.columns[3:]]

    result = suggest_songs(song_df, my_model)

    return jsonify(result)

@app.route('/pred', methods=['POST'])
def runPred():
    
    input_song = request.get_json(force=True)
    input_song.update((x, [y]) for x, y in input_song.items())

    song_df = pd.DataFrame.from_dict(input_song)
    song_df = song_df[song_df.columns[3:]]
    
    results = suggest_songs(song_df, my_model)

    return jsonify(results)

@app.route("/reset")
def reset():
    engine = create_engine('sqlite:///db.sqlite3', echo=False)

    # DB = SQLAlchemy(app)
    # DB.drop_all()
    # DB.create_all()

    # df = pd.read_csv('SpotifyAudioFeaturesApril2019.csv')
    # df.to_sql('songs', index=False, con=engine)
    songs_df =  pd.read_sql_table('songs', 'sqlite:///db.sqlite3')

    X = songs_df[songs_df.columns[3:]]
    y = songs_df[songs_df.columns[:3]]


    test_song2 = {"artist_name": "Rick Astley", "track_id": "7GhIk7Il098yCjg4BQjzvb", "track_name": "Never Gonna Give You Up", "acousticness": 0.135, "danceability": 0.727, "duration_ms": 212827, "energy": 0.939, "instrumentalness": 4.35e-05, "key": 8, "liveness": 0.151, "loudness": -11.855, "mode": 1, "speechiness": 0.0369, "tempo": 113.33, "time_signature": 4, "valence": 0.916, "popularity": 66}
    my_model = create_model(preprocess(X))

    return "DB reset"

if __name__ == '__main__':
    app.run(debug=True, port=8000)

