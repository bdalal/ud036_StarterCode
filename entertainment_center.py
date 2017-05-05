import sys
import csv
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
# no. of movies to be fetched
no_of_movies = 9
# increments for the progress bar
progress_increments = float(100 / no_of_movies)
# precached movie ids from file to speed up execution
movie_cache = dict()
# current cache to be maintained so that no movie is duplicated
current_cache = set()

try:
    with open('movie_id_cache', 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            movie_cache[row[0]] = row[1:]
except IOError:
    pass

f = open('movie_id_cache', 'a')
writer = csv.writer(f)

while m_ctr < no_of_movies:
    try:
        # Generate a random integer to be used as ID for the movie
        movie_id = randint(0, 2000)
        # Check if id exists in cache
        if movie_id in movie_cache and movie_id not in current_cache:
            title = movie_cache[movie_id][0]
            tagline = movie_cache[movie_id][1]
            poster = movie_cache[movie_id][2]
            trailer = movie_cache[movie_id][3]
            current_cache.add(movie_id)
        elif movie_id not in current_cache:
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
            current_cache.add(movie_id)
            # Write new movie to and cache file
            writer.writerow([movie_id, title, tagline, poster, trailer])
        movie_list.append(media.Movie(title, tagline, poster, trailer))
        m_ctr += 1
        # Display progress bar as movies are being fetched
        sys.stdout.write("Fetching movies: %d%%   \r" %
                         (progress_increments * m_ctr))
        sys.stdout.flush()
    except:
        pass

f.close()

# Calling the open_movies_page module for rendering the static page
fresh_tomatoes.open_movies_page(movie_list)
