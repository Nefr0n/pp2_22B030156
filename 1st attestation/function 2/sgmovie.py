from movies import movies

def is_movie_good(movies ,movie_name):
    curr_movie = dict(())
    for movie in movies:
        if movie["name"] == movie_name:
            curr_movie = movie
    return curr_movie["imdb"] > 5.5


print(is_movie_good(movies, "Hitman"))