import requests
import bs4

# Get HTML markup from http://quotes.toscrape.com
base_url = 'http://quotes.toscrape.com/page/{}'
result = requests.get('http://quotes.toscrape.com')
text = result.text

# Get the names of all the authors on the first page.
soup = bs4.BeautifulSoup(text, 'lxml')
authors = soup.select('.author')
name_of_authors = []
for author in authors:
    name_of_authors.append(author.text)

texts = soup.select('.text')
all_text = []
for text in texts:
    all_text.append(text.text)

tags = soup.select('.tag-item>.tag')
top_ten_tags = []

for tag in tags:
    top_ten_tags.append(tag.text)

next_page_exists = True
page_number = 1
unique_authors = set()
while next_page_exists:
    result = requests.get(base_url.format(page_number))
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    if len(soup.select('.pager>.next')) == 0:
        next_page_exists = False
    page_number += 1
    authors = soup.select('.author')
    for author in authors:
        unique_authors.add(author.text)

print(unique_authors)