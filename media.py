import webbrowser

class Video():

    """A video class that tracks common Video attributes"""
    
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        
class Movie(Video):

    """A movie class that tracks a movie's details and allows a trailer to be played"""
    
    def __init__(self, movie_title, movie_duration, movie_storyline, poster_image_url, trailer_youtube_url):
        Video.__init__(self, movie_title, movie_duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

class TvShow(Video):

    """A TV show class that tracks a TV show's details and allows a local listing to be displayed"""

    def __init__(self, tvshow_title, tvshow_duration, tvshow_season, tvshow_episode, tvshow_tv_station):
        Video.__init__(self, tvshow_title, tvshow_duration)
        self.season = tvshow_season
        self.episode = tvshow_episode
        self.tv_station = tvshow_tv_station

    def get_local_listing(self):
        print("TODO Get local listing")
