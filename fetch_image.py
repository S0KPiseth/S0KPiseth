import requests
import os

image_extension=""
while(image_extension!="png"):
    response = requests.get("https://meme-api.com/gimme")
    data = response.json()
    image_url = data['url']
    image_extension = image_url.split('.')[-1]

title = "meme_of_the_day"    
image_response = requests.get(image_url)
os.makedirs('memes', exist_ok=True)
image_path = f"memes/{title}.{image_extension}"

with open(image_path, 'wb') as f:
    f.write(image_response.content)

