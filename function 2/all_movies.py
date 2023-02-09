def get_good_movies(movies):
    good_movies = []
    for movie in movies:
        if movie["imdb"] > 5.5:
            good_movies.append(movie["name"])
    return good_movies

print(get_good_movies(movies))