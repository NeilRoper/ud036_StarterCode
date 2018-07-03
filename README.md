# Fresh tomatoes Introduction
Fresh tomatoes is a Python project that displays a list of movies on a website. Users can click on Movie trailer images to play a movie trailer on YouTube.

##Installation
1. Clone or download the [Github repository](https://github.com/NeilRoper/ud036_StarterCode.git).
2. Create a Python file that imports the media and fresh_tomatoes libraries - for an example take a look at the entertainment_center.py file.
3. Create instances of your favourite films making sure to pass the following parameters:
-movie_title
-movie_duration
-movie_storyline
-poster_image_url
-trailer_youtube_url
e.g.
```
toy_story = media.Movie("Toy Story",
                        103,
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
```
4. Load all of the Movie instances into a list `movies = (toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games)`
5. Call the open_movies_üpage passing the list to open the web browser and display the movies `fresh_tomatoes.open_movies_page(movies)`

##Dependencies
This program requires [Pyth)on 2.7](https://www.python.org/download/releases/2.7/).

##Known Issues
-Some of the YouTube movie trailers may not open in your region due to copyright issues.
