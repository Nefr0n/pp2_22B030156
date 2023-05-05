def get_high(movies):
    g_rate = []
    for movie in movies:
        if movie["imdb"] > 5.5:
            g_rate.append(movie["name"])
    return g_rate

print(get_high(movies))