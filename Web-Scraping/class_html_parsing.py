import re
from bs4 import BeautifulSoup, Tag

ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
                <p class="star-rating Three">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
        <p class="price_color">£51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>

        In stock

</p>
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>
            </div>
    </article>
</li>

</body></html>
'''


class ParsedItemLocators:
    """
    Locators for an item in the HTML page.

    This allows us to easily see what our code will be looking at
    as well as change it quickly if we notice it is now different.
    """
    NAME_LOCATOR = 'article.product_pod h3 a'
    LINK_LOCATOR = 'article.product_pod h3 a'
    PRICE_LOCATOR = 'article.product_pod p.price_color'
    RATING_LOCATOR = 'article.product_pod p.star-rating'


class ParsedItem:
    """
    A class to take in an HTML page (or part of it), and find properties of an
    item in it.
    """

    def __init__(self, page):
        if isinstance(page, Tag):
            self.soup = page
        else:
            self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def name(self):
        locator = ParsedItemLocators.NAME_LOCATOR
        item_link = self.soup.select_one(locator)
        item_name = item_link.attrs['title']
        return item_name

    @property
    def link(self):
        locator = ParsedItemLocators.LINK_LOCATOR
        item_link = self.soup.select_one(locator)
        item_href = item_link.attrs['href']
        return item_href

    @property
    def price(self):
        locator = ParsedItemLocators.PRICE_LOCATOR
        item_price = self.soup.select_one(locator).string  # £51.77

        expression = r'(\$|£|€)([0-9,]+\.[0-9]+)'
        matcher = re.search(expression, item_price)  # [£51.77, £, 51.77]

        price_float = float(matcher[2].replace(",", ""))
        return price_float

    @property
    def rating(self):
        locator = ParsedItemLocators.RATING_LOCATOR
        star_rating_tag = self.soup.select_one(locator)
        classes = star_rating_tag.attrs['class']
        rating_classes = filter(lambda cls: cls != 'star-rating', classes)
        return next(rating_classes)


if __name__ == '__main__':
    item = ParsedItem(ITEM_HTML)
    print(item.name)
    print(item.link)
    print(item.price)
    print(item.rating)
