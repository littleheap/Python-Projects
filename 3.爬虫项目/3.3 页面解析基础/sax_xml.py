import string
from xml.parsers.expat import ParserCreate

'''
    <?xml version="1.0" encoding="ISO-8859-1"?>
    
    <bookstore>
    
        <book>
    
            <title lang="eng">Harry Potter</title>
    
            <price>29.99</price>
    
        </book>
    
        <book>
    
            <title lang="eng">Learning XML</title>
    
            <price>39.95</price>
    
        </book>
    
    </bookstore>
'''

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        self.element = name
        print('element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('end element: %s' % name)

    def char_data(self, text):
        if text.strip():
            print("%s's text is %s" % (self.element, text))


handler = DefaultSaxHandler()

parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data

with open('book.xml', 'r') as f:
    parser.Parse(f.read())

'''
    element: bookstore, attrs: {}
    element: book, attrs: {}
    element: title, attrs: {'lang': 'eng'}
    title's text is Harry Potter
    end element: title
    element: price, attrs: {}
    price's text is 29.99
    end element: price
    end element: book
    element: book, attrs: {}
    element: title, attrs: {'lang': 'eng'}
    title's text is Learning XML
    end element: title
    element: price, attrs: {}
    price's text is 39.95
    end element: price
    end element: book
    end element: bookstore
'''
