from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class Song(DB.Model):
    """Songs and their features"""
    
    artist_name = DB.Column(DB.String(30))
    track_id = DB.Column(DB.String(30), primary_key=True)
    track_name = DB.Column(DB.String(30), nullable=False)
    
    acousticness = DB.Column(DB.Float)
    danceability = DB.Column(DB.Float)
    duration_ms = DB.Column(DB.BigInteger)
    energy = DB.Column(DB.Float)
    instrumentalness = DB.Column(DB.Float)
    key = DB.Column(DB.INT)
    liveness = DB.Column(DB.Float)
    loudness = DB.Column(DB.Float)
    mode = DB.Column(DB.INT)
    speechiness = DB.Column(DB.Float)
    tempo = DB.Column(DB.Float)
    time_signature = DB.Column(DB.INT)
    valence = DB.Column(DB.Float)
    
    popularity = DB.Column(DB.INT)
    
    def __repr__(self):
        return '<Track Id: {}>'.format(self.track_id)