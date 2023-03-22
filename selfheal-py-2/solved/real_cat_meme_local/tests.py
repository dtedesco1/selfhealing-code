import os
import requests

def test_download_cat_meme():
    cat_meme_url = 'https://i.imgur.com/3pGZm7v.jpeg'
    response = requests.get(cat_meme_url)
    assert response.status_code == 200
    with open("cat_meme.jpg", "wb") as f:
        f.write(response.content)
    assert os.path.isfile("cat_meme.jpg") is True