from bs4 import BeautifulSoup
import logging

SIMPLE_HTML = '''<html>
     <head>
     </head>
     <body>
        <h1>This is a title</h1>
        <p class="subtitle">Lorem impsum dolor sit amet. Consectetur edipiscim elit.</p>
        <p>Here's another p without a class</p>
        <ul>
            <li>Rolf</li>
            <li>Charlie</li>
            <li>Jen</li>
            <li>Jose</li>
        </ul>
     </body>
 </html>'''


logging.basicConfig(
    format='%(asctime)-s %(name)-8s %(levelname)-8s [%(filename)s:%(lineno)d]: %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S',
    level=logging.DEBUG
)
logger = logging.getLogger(__name__)

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')
# print(simple_soup)


def find_title():
    h1_tag = simple_soup.find('h1')
    print(h1_tag.string)


def find_list_items():
    list_items = simple_soup.find_all('li')
    list_contents = [elem.string for elem in list_items]
    print(list_contents)


def find_subtitle():
    paragraph = simple_soup.find('p', {'class': 'subtitle'})
    print(paragraph.string)


def find_other_paragraph():
    paragraphs = simple_soup.find_all('p')
    other_paragraph = [p for p in paragraphs if 'subtitle' not in p.attrs.get('class', [])]
    print(other_paragraph[0].string)


find_title()
find_list_items()
find_subtitle()
find_other_paragraph()
