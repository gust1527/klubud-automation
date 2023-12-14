from beautifulsoup4 import BeautifulSoup
import requests

# Step 1: Send HTTP request to the URL
url = 'https://klubub.dk/'
response = requests.get(url)

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Use BeautifulSoup to find elements
# For example, find all paragraph 'p' tags
paragraphs = soup.find_all('p')

# Print the text from each paragraph
for p in paragraphs:
    print(p.get_text())