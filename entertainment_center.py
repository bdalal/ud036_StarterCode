import media
import fresh_tomatoes
from tmdb3 import set_key, Movie
from random import randint

# API key for The Movie Database
set_key('bf277b2f54255cc09463930d16f832b0')

# Counter to count for n movies on the site
m_ctr = 0
# list containing movie objects
movie_list = []

while m_ctr < 5:
    try:
        # Generate a random integer to be used as ID for the movie
        movie_id = randint(0, 2000)
        movie = Movie(movie_id)
        # If the returned movie lacks any required info., skip it
        if hasattr(movie, 'title'):
            title = movie.title
        else:
            continue
        if hasattr(movie, 'tagline'):
            tagline = movie.tagline
        else:
            tagline = ''
        if hasattr(movie, 'poster'):
            try:
                poster = movie.poster.geturl()
            except:
                continue
        else:
            continue
        if hasattr(movie, 'youtube_trailers'):
            try:
                trailer = movie.youtube_trailers[0].geturl()
            except:
                continue
        else:
            continue
        movie_list.append(media.Movie(title, tagline, poster, trailer))
        m_ctr += 1
    except:
        pass

# Calling the open_movies_page module for rendering the static page
fresh_tomatoes.open_movies_page(movie_list)
