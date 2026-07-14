import os
import json
from turtle import title

filename = "movies.json"

def get_movies():
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as file:
        movies = [line.strip() for line in file.readlines()]
    return movies

def save_movie(movie):
    with open(filename, "a") as file:
        json.dump(f"{movie}\n", file, indent=2)


def add_movies(movies):
    titles = input("Enter the title of the movie: ").lower()
    if any(movie["title"].lower() == titles for movie in movies):
        print("Movie already exists in the list.")
        return
    
    genre = input("Enter the genre of the movie: ")
    try:
        rating = float(input("Enter the rating of the movie (0-10): "))
        if not (0 <= rating <= 10):
            raise ValueError("Rating must be between 0 and 10.") 
    except ValueError as e:
        print(f"Invalid rating: {e}")
        return
    
    movies.append({"title": titles, "genre": genre, "rating": rating})
    save_movie(movies)
    print(f"Movie '{titles}' added successfully.")


def search_movies(movies):
    user = input("Enter the title and genre of the movie to search: ").strip().lower()
    found_movies = [
        movie for movie in movies
          if user in movie["title"].lower() or 
          user in movie["genre"].lower()
          ]
    
    if not found_movies:
        print("No movies found matching your search.")
        return
    print(f"Found {len(found_movies)} movie(s):")
    for movie in found_movies:
        print(f"Title: {movie['title']} -- Genre: {movie['genre']} -- Rating: {movie['rating']}")


def view_movies(movies):
    if not movies:
        print("No movies in the list.")
        return
    print("Movies in the list:")
    print("-" * 40)
    for movie in movies:
        print(f"Title: {movie['title']} -- Genre: {movie['genre']} -- Rating: {movie['rating']}")
    print("-" * 40)
    


def run_movie_db():
    movies = get_movies()
    while True:
        print("\nMovie Tracker Menu:")
        print("1. Add a movie")
        print("2. View all movies")
        print("3. Search for a movie")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            add_movies(movies)
        elif choice == "2":
            view_movies(movies)
        elif choice == "3":
            search_movies(movies)
        elif choice == "4":
            print("Exiting the Movie Tracker. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")

run_movie_db()