import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Data_science"

# Download the page
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extracts the page title
page_title = soup.find("title").text.strip()
print("Page title:" + page_title)

# Finds the main article content
content_div = soup.find("div", id="mw-content-text")

# Extracts the first paragraph with at least 50 characters
paragraphs = content_div.find_all("p")
for p in paragraphs:
    text = p.text.strip()
    if len(text) >= 50:
        print("First paragraph with 50+ characters:")
        print(text)
        break