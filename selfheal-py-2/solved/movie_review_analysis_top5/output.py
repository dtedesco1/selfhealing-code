import collections
import re
import sys

def extract_movie_titles(file_content):
    pattern = r'"(.*?)"'
    movie_titles = re.findall(pattern, file_content)
    return movie_titles

def count_movie_mentions(movie_titles):
    movie_counter = collections.Counter()
    for title in movie_titles:
        movie_counter[title] += 1
    return movie_counter

def display_top_movies(movie_counter):
    top_movies = movie_counter.most_common(5)
    for movie, count in top_movies:
        print(f'{movie}: {count}')

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as file:
            content = file.read()
        movies = extract_movie_titles(content)
        movie_counts = count_movie_mentions(movies)
        display_top_movies(movie_counts)
    else:
        print("Please provide a text file as a command line argument.")