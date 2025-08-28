import requests
from pathlib import Path

# Make a GET request to fetch the raw HTML content
url ="https://interactivecares.com/"
response = requests.get(url)
output = response.text

# Define the output file path
output_file = Path("web_scrapping_1.txt")
# Write the HTML content to a file
output_file.write_text(output)

# Read and print the content from the file
output_file = output_file.read_text(encoding="utf-8")
print(output_file)