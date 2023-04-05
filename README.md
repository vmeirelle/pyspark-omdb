# Movie Rating Stream

This code is a simple PySpark application that streams movie titles from a local socket and returns their ratings using the OMDb API. The ratings are printed in real-time using PySpark Streaming.

## Prerequisites

* Python 3.x
* PySpark
* requests module
* OMDb API key (imported from key.py file)

## How to Run

Clone this repository and navigate to the directory.
Open the key.py file and replace YOUR_API_KEY with your actual OMDb API key.
Open a terminal window and start the netcat utility to create a local socket:
```
nc -lk 9999
```
In a separate terminal window, start the PySpark application:
```
spark-submit movie_ratings_stream.py
```
In the first terminal window, type in movie titles and press Enter to send them to the streaming application.
The application will return the movie titles and their ratings in real-time.
Note: You can adjust the streaming interval by modifying the value of StreamingContext (in seconds).

## Streaming

In this code, PySpark's Streaming module is used to read data from a local socket in real-time and process it using the get_movie_rating function. The ratings are then filtered and printed in real-time using PySpark's pprint function.

A pipeline refers to the process of chaining together multiple data processing stages to form a workflow. In this code, a simple pipeline is used to read in data from the socket, process it with the ```get_movie_rating``` function, and then filter and print the resulting ratings. The pipeline consists of three stages:

1. Data ingestion: The ```StreamingContext``` reads data from the local socket and creates a ```DStream``` of movie titles.
2. Data processing: The ```map``` function applies the ```get_movie_rating function``` to each movie title in the ```DStream```, which retrieves the movie's rating from the OMDb API.
3. Data output: The ```filter``` function removes any ```None``` values returned by the ```get_movie_rating``` function, and the resulting ```(movie_title, rating)``` tuples are printed in real-time using the ```pprint``` function.

Overall, this code demonstrates how PySpark's Streaming module can be used to build a simple data pipeline that processes and analyzes continuous data streams in real-time.

![flow](https://user-images.githubusercontent.com/50549048/229989599-af3c6d92-9dc6-4876-9d1a-bb2080f99f6f.png)

## Code Attribution

This code was developed by @vmeirelle for educational purposes. You are free to use and modify this code for your own projects. 
