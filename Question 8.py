import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Data_science"

response = requests.get(url)
response.raise_for_status()  # makes errors obvious if the page fails to load

soup = BeautifulSoup(response.text, "html.parser")

# Main content area
content_div = soup.find("div", id="mw-content-text")

# Get all h2 headings inside the main content
h2_tags = content_div.find_all("h2")

exclude_words = {"references", "external links", "see also", "notes"}

headings = []

for h2 in h2_tags:
    # Wikipedia headings usually store the real heading text in <span class="mw-headline">
    headline_span = h2.find("span", class_="mw-headline")

    if headline_span:
        heading_text = headline_span.get_text(strip=True)
    else:
        # fallback: get all text, then clean possible "[edit]"
        heading_text = h2.get_text(" ", strip=True).replace("[edit]", "").strip()

    # Skip empty headings
    if not heading_text:
        continue

    # Exclude unwanted headings (case-insensitive)
    if any(word in heading_text.lower() for word in exclude_words):
        continue

    headings.append(heading_text)

# Save to headings.txt, one heading per line
with open("headings.txt", "w", encoding="utf-8") as f:
    for heading in headings:
        f.write(heading + "\n")

print(f"Saved {len(headings)} headings to headings.txt")
