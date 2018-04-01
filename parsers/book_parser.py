from bs4 import  BeautifulSoup
import re
from locators.book_locators import BookLocators


class BookParser:
    """
    A class to take in an HTML page (or part of), and find properties of an item in it.
    """

    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5,

    }

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Book {self.name}, ${self.price}, ({self.rating} stars)'

    @property
    def name(self):
        locator = BookLocators.NAME_LOCATOR
        item_link = self.parent.select_one(locator)
        item_name = item_link.attrs['title']
        # can do item_name = soup.select_one(locator).['title']
        return (item_name)

    @property
    def link(self):
        locator = BookLocators.LINK_LOCATOR
        item_link = self.parent.select_one(locator).attrs['href']
        return (item_link)

    @property
    def price(self):
        locator = BookLocators.PRICE_LOCATOR
        item_price = self.parent.select_one(locator).string
        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        return (float(matcher.group(1)))

    @property
    def rating(self):
        locator = BookLocators.RATING_LOCATOR
        star_rating_tag = self.parent.select_one(locator)
        """
        star_rating_tag =
        <p class="star-rating Three">
            <i class="icon-star"></i>
            <i class="icon-star"></i>
            <i class="icon-star"></i>
            <i class="icon-star"></i>
            <i class="icon-star"></i>
            </p>
        """
        classes = star_rating_tag.attrs['class'] # returns ['star rating', 'Three']
        rating = [r for r in classes if r != 'star-rating']
        return BookParser.RATINGS[rating[0]]
