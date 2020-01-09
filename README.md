
# http://spotify-flask-model.herokuapp.com/


# misc code removed
```
infile = "https://raw.githubusercontent.com/spotify-recommendation-engine-3/data_science/master/Data/SpotifyAudioFeaturesApril2019_duplicates_removed.csv"
df = pd.read_csv(infile)
df = pd.read_csv('SpotifyAudioFeaturesApril2019.csv')
df.to_sql('songs', con=engine)
```