import requests
import string
import matplotlib.pyplot as plt

# Retrieve the text of the Wikipedia page for the International Space Station
url = 'https://en.wikipedia.org/wiki/International_Space_Station'
response = requests.get(url)
text = response.text

# Create an empty dictionary to store the letter counts
counts = {}

# Loop through each character in the text and update the count in the dictionary if the character is a letter
for char in text:
    if char.isalpha():
        char = char.lower()
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

# Create a histogram of the letter counts
plt.bar(counts.keys(), counts.values())

# Save the histogram to a local file using the savefig function
plt.savefig('letter_histogram.png')