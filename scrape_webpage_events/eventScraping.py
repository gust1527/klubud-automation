from bs4 import BeautifulSoup
import requests


# Define what URL to target
URL = 'https://www.klubud.dk/varer/oplevelser/'

# Make a request to the URL
response = requests.get(URL, timeout=5)

# Parse the fetched HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the paragraph tags
paragraphs = soup.find_all('div', class_='product-small')

# Loop through each paragraph and print the text
for p in paragraphs:
    print(p.get_text())
