import requests
import bs4

result = requests.get('http://example.com')

soup = bs4.BeautifulSoup(result.text, 'lxml')

# Select HTML element
soup.select('title')[0].getText()
site_paragrapsh = soup.select('p')
first_paragraph = site_paragrapsh[0]
first_paragraph_text = first_paragraph.getText()

wikipedia_page = requests.get('https://hu.wikipedia.org/wiki/Lewis_Hamilton')
soup = bs4.BeautifulSoup(wikipedia_page.text, 'lxml')
soup.select('.toctext')

for item in soup.select('.toctext'):
    print(item.text)

# Download image from a website
res = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
soup = bs4.BeautifulSoup(res.text, 'lxml')
soup.select('.thumbimage')
computer = soup.select('.thumbimage')[0]
thumb_images = soup.select('.thumbimage')
first_thumbimage = thumb_images[0]
image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg')
# f = open('my_computer_image.jpg', 'wb')
# f.write(image_link.content)
# f.close()


# Get books with 2 star
base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
two_start_titles = []

for n in range(1, 51):
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    books = soup.select('.product_pod')

    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            book_title = book.select('a')[1]['title']
            two_start_titles.append(book_title)

