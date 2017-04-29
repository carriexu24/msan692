import requests
from bs4 import BeautifulSoup

def parseAmazonBestSellers():
    response = requests.get("http://www.amazon.com/gp/bestsellers/books/ref=sv_b_2",
                          params={'User-Agent': "Resistance is futile"})
    soup = BeautifulSoup(response.text, "html.parser")

    books = []
    for item in soup.find_all(class_="zg_itemWrapper"):
        link = item.find(class_="a-link-normal")
        priceitem = item.find(class_="a-size-base a-color-price")
        if priceitem is None: continue
        price = priceitem.string.strip()
        href = link['href'].strip()
        title = link.img['alt'].strip()
        auth = item.find(class_="a-size-small a-link-child")
        if auth: # some missing an author?
            author = auth.text.strip()
            books.append((price, title, author, href))

    return books

books = parseAmazonBestSellers()
for price, title, author, href in books:
    print title, author, price
    print href
    print
