import requests
from bs4 import BeautifulSoup
from class_html_parsing import ParsedItem

page = requests.get('https://books.toscrape.com/')  # Scrapping a website
soup = BeautifulSoup(page.content, "html.parser")  # Parses a html-script

# Get all the books tags
books_tags = soup.select(
    'body div.container-fluid.page div.page_inner div.row div.col-sm-8.col-md-9 section div ol.row li.col-xs-6.col-sm-4.col-md-3.col-lg-3')
books_soups = [ParsedItem(book) for book in books_tags]  # Creating a new parsing for each book

names = [book.name for book in books_soups]  # Getting the name of each book

# Displaying the names in the console
print("These are the books names:")
for name in names:
    print(f"\t- {name}")
