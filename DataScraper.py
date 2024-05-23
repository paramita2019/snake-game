import requests
from bs4 import BeautifulSoup

# Make a request to the website
r = requests.get("http://www.google.com")
r.content

# Use the 'html.parser' to parse the page
soup = BeautifulSoup(r.content, 'html.parser')

# Use the BeautifulSoup object `soup` and the `find_all` method to extract all HTML elements with the tag "a" (links)
links = soup.find_all('a')

# Loop through the links and print each one
for link in links:
    print(link.get('href'))