import webbrowser


class Movie():
    """Class to store Movie details"""
    def __init__(self, movie_title,
                 movie_poster_url,
                 movie_storyline,
                 movie_trailer):
        self.title = movie_title
        self.poster_image_url = movie_poster_url
        self.movie_storyline = movie_storyline
        self.trailer_youtube_url = movie_trailer

    def show_trailer(self):
        """Plays the trailer video of the movie"""
        # Play the youtube video.
        webbrowser.open(self.trailer_youtube_url)
