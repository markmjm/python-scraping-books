import re
import logging
from bs4 import BeautifulSoup
from locators.all_books_page import AllBooksPageLocators
from parsers.book_parser import  BookParser

logger = logging.getLogger('scraping.AllBooksPage')   # This is a child logger of scraping which was created in ap.py

class AllBooksPage:
    def __init__(self, page_content):
        logger.debug('Parsing page content with BeautifulSoup HTML Parser')
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def books(self):
        logger.debug(f'finding all book in page {AllBooksPageLocators.BOOKS}')
        return [BookParser(e) for e in self.soup.select(AllBooksPageLocators.BOOKS)]

    @property
    def page_count(self):
        content = self.soup.select_one(AllBooksPageLocators.PAGER).string
        pattern = 'Page [0-9]+ of ([0-9]+)'
        matcher = re.search(pattern, content)
        logger.info(f'Matcher is {matcher}')
        return matcher[1]


