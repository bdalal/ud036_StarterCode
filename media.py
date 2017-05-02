import webbrowser


class Movie():

    ''' The class holds movie related information like name, storyline, poster
    and trailer links

    Attributes:
        title (str): Title of the movie
        storyline (str): one-liner about the film
        poster_image_url: URL for the movie poster image
        trailer_youtube_url: URL for the movie trailer on YouTube

    Method:
        show_trailer(): Opens the trailer url in a web browser
    '''

    # Initialize Movie object
    def __init__(self, movie_title, movie_storyline, poster_image,trailer_youtube): # NOQA
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Open browser and redirect to trailer URL
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
