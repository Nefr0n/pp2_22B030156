def get_avg_rating_by_category(movies, category):
    sum = 0
    num_movies = 0
    for movie in movies:
        if movie['category'] == category:
            sum += movie['imdb']
            num_movies += 1
    return sum / num_movies

print(get_avg_rating_by_category(movies, 'Suspense'))