import requests
import os

# Step 2: Get the URL of a real cat meme
cat_meme_url = 'https://i.imgur.com/3pGZm7v.jpeg'

# Step 3: Make a GET request to the cat meme URL
response = requests.get(cat_meme_url)

# Step 4: Check the response status code
if response.status_code != 200:
    raise ValueError("Failed to download cat meme")

# Step 5: Extract the content of the response
image_content = response.content

# Step 6: Create a new file with a .jpg extension
with open("cat_meme.jpg", "wb") as f:
    # Step 7: Write the image content to the file
    f.write(image_content)

# Step 8: Close the file
f.close()

# Step 9: Print a success message
print("Cat meme downloaded and stored locally!")