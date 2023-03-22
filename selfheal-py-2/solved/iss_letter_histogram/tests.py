import os
import unittest
import requests
import matplotlib.pyplot as plt

class TestLetterHistogram(unittest.TestCase):
    
    def test_file_exists(self):
        self.assertTrue(os.path.exists('letter_histogram.png'))
    
    def test_file_not_empty(self):
        self.assertGreater(os.path.getsize('letter_histogram.png'), 0)
    
    def test_file_is_image(self):
        self.assertIn('image', os.popen('file -b --mime-type letter_histogram.png').read())
    
    def test_histogram_created(self):
        url = 'https://en.wikipedia.org/wiki/International_Space_Station'
        response = requests.get(url)
        text = response.text
        counts = {}
        for char in text:
            if char.isalpha():
                char = char.lower()
                if char in counts:
                    counts[char] += 1
                else:
                    counts[char] = 1
        plt.bar(counts.keys(), counts.values())
        plt.savefig('letter_histogram.png')
        self.assertTrue(os.path.exists('letter_histogram.png'))

if __name__ == '__main__':
    unittest.main()