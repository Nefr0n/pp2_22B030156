def get_average_rating(movies):
    sum = 0
    num_movies = len(movies)
    for movie in movies:
        sum += movie["imdb"]
    return sum/num_movies

print(get_average_rating(movies))