import requests
from pathlib import Path

# Make a GET request to fetch the raw HTML content
url ="https://interactivecares.com/"

for i in range(1000):
    requests.get(url)
    print(i)