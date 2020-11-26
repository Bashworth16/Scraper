import requests
from bs4 import BeautifulSoup
import urllib.request

# Tell tell the program where we are going to scrape.
url = "http://www.reddit.com/r/BabyYoda"

# Create Response Object:
# Get request with our URL as its parameter to get the contents from the BabyYoda reddit page.
response = requests.get(url)

# Instantiate Web Scraper. Parse over html content taken from the response variable.
soup = BeautifulSoup(response.content, "html.parser")

# Finds and stores all 'img' files from post images in a dictionary.
images = soup.find_all("img", attrs={"alt": "Post image"})

# Variable for numbering collected images
number = 0

# Iterate over images collected and stores in our images dictionary.
for image in images:
    image_src = image["src"]  # Extract Source attribute for download.
    print(image_src)  # Print image source
    urllib.request.urlretrieve(image_src, str(number))  # urllib to download and number (image_src, str(number)
    number += 1
