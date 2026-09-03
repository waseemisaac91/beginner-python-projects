#Project 1: Favorite Movie List

print("Welcome to the Favorite Movie List!")

movies = []
for i in range(3):
    movie = input(f"Enter the name of your favorite movie # {i+1}: ")
    movies.append(movie)

print("Your favorite movies are:", movies)
print("First movie:", movies[0] )
print("Last movie:", movies[-1])
print("Total number of movies:", len(movies))
