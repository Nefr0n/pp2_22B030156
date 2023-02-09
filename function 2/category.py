def get_movies_by_category( movies, category):
    movies_list = []
    for movie in movies:
        if movie['category'] == category:
            movies_list.append(movie)
    return movies_list

print(get_movies_by_category(movies, "Drama"))
print(get_movies_by_category(movies, "Suspense"))