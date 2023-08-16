import requests
from bs4 import BeautifulSoup
import json

indexed_titles = {}

with open("found_links.txt", 'r') as indexed_links_f:
    for link in indexed_links_f.readlines():
        link = link.strip()
        content = requests.get(link).content
        bs = BeautifulSoup(content, "html.parser")
        title = bs.title.string
        indexed_titles[link] = title

with open("indexed_titles.json", "w") as indexed_titles_f:
    json.dump(indexed_titles, indexed_titles_f)
