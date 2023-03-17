import unittest
from collections import Counter
from temp_output import extract_movie_titles, count_movie_mentions, display_top_movies

class TestMovieMentions(unittest.TestCase):

    def test_extract_movie_titles(self):
        test_content = 'I love watching "Movie1" and "Movie2".'
        expected = ['Movie1', 'Movie2']
        result = extract_movie_titles(test_content)
        self.assertEqual(result, expected)

    def test_count_movie_mentions(self):
        movie_titles = ['Movie1', 'Movie2', 'Movie1', 'Movie3', 'Movie2']
        expected = Counter({'Movie1': 2, 'Movie2': 2, 'Movie3': 1})
        result = count_movie_mentions(movie_titles)
        self.assertEqual(result, expected)

    def test_display_top_movies(self):
        movie_counts = Counter({'Movie1': 4, 'Movie2': 3, 'Movie3': 2, 'Movie4': 1, 'Movie5': 1})
        expected = "Movie1: 4\nMovie2: 3\nMovie3: 2\nMovie4: 1\nMovie5: 1\n"
        with unittest.mock.patch('builtins.print') as mocked_print:
            display_top_movies(movie_counts)
            output = "".join([call[0][0] for call in mocked_print.call_args_list])
            self.assertEqual(output, expected)

if __name__ == "__main__":
    unittest.main()