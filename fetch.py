
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
import requests
from key import key

sc = SparkContext("local[2]", "MovieStream")
ssc = StreamingContext(sc, 10)
endpoint = "http://www.omdbapi.com/"
params = {"apikey": key, "t": ""}
lines = ssc.socketTextStream("localhost", 9999)

def get_movie_rating(title):
    params["t"] = title
    response = requests.get(endpoint, params=params)
    if response.status_code == 200:
        movie = response.json()
        return (movie["Title"], movie["imdbRating"])
    else:
        return None

ratings = lines.map(get_movie_rating).filter(lambda x: x is not None)

ratings.pprint()

ssc.start()
ssc.awaitTermination()
