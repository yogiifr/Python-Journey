from hmtl.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):

    def __init__(self,base_url,page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def error(self, massage):
        pass

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute,value) in attrs:


    