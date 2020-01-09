from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import NearestNeighbors
import pandas as pd 
from spider import spider_plot

songs_df =  pd.read_sql_table('songs', 'sqlite:///db.sqlite3')
y = songs_df[songs_df.columns[:3]]
X = songs_df[songs_df.columns[3:]]


test_song = {"artist_name":"YG","track_id":"2RM4jf1Xa9zPgMGRDiht8O","track_name":"Big Bank feat. 2 Chainz, Big Sean, Nicki Minaj","acousticness":0.00582,"danceability":0.743,"duration_ms":238373,"energy":0.339,"instrumentalness":0.0,"key":1,"liveness":0.0812,"loudness":-7.678,"mode":1,"speechiness":0.409,"tempo":203.927,"time_signature":4,"valence":0.118,"popularity":15}
test_song2 = {"artist_name": "Rick Astley", "track_id": "7GhIk7Il098yCjg4BQjzvb", "track_name": "Never Gonna Give You Up", "acousticness": 0.135, "danceability": 0.727, "duration_ms": 212827, "energy": 0.939, "instrumentalness": 4.35e-05, "key": 8, "liveness": 0.151, "loudness": -11.855, "mode": 1, "speechiness": 0.0369, "tempo": 113.33, "time_signature": 4, "valence": 0.916, "popularity": 66}



def preprocess(df):
    """ normalizes pandas df.
    Removes unecessary columns """
    drop_cols = ['duration_ms', 'key', 'mode', 'time_signature', 'popularity','tempo']
    df = df.drop(columns=drop_cols)
    scaler = MinMaxScaler()
    scaler.fit_transform(df)
    
    return df

def create_model(X, n_neighbors=10):
    """ Insantiate nearest neighbor model """
    model = NearestNeighbors(n_neighbors=n_neighbors, algorithm='kd_tree')
    model.fit(X)
    return model

def suggest_songs(source_song, model):
    """ Preprecesses source song, use it to make suggestions from the database """
    source_song = preprocess(source_song)
    recommendations = model.kneighbors(source_song)[1][0]
    recommendations_dict = y.iloc[recommendations].T.to_dict()
    # pic_hash = spider_plot(songs_df)
    return recommendations_dict

