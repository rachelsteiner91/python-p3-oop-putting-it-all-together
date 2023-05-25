#!/usr/bin/env python3

class Book:
#Book in book.py has the title and page_count passed into __init__, and values can be set to new instance.
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

#Book in book.py prints "page_count must be an integer" if page_count is not an integer.
    def get_page_count(self):
        return self._page_count 
    def set_page_count(self, page_count):
        if (isinstance(page_count, int)):
            self._page_count = page_count
        else:
            print("page_count must be an integer")
    page_count = property(get_page_count, set_page_count)
        
#Book in book.py outputs "Flipping the page...wow, you read fast!" when method turn_page() is called 
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")