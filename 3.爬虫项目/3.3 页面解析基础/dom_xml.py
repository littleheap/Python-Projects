from xml.dom import minidom

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

doc = minidom.parse('book.xml')

root = doc.documentElement
print(dir(root))
# ['ATTRIBUTE_NODE', 'CDATA_SECTION_NODE', 'COMMENT_NODE', 'DOCUMENT_FRAGMENT_NODE', 'DOCUMENT_NODE', 'DOCUMENT_TYPE_NODE', 'ELEMENT_NODE', 'ENTITY_NODE', 'ENTITY_REFERENCE_NODE', 'NOTATION_NODE', 'PROCESSING_INSTRUCTION_NODE', 'TEXT_NODE', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '__weakref__', '_attrs', '_attrsNS', '_call_user_data_handler', '_child_node_types', '_ensure_attributes', '_get_attributes', '_get_childNodes', '_get_firstChild', '_get_lastChild', '_get_localName', '_get_tagName', '_localName', '_magic_id_nodes', 'appendChild', 'attributes', 'childNodes', 'cloneNode', 'firstChild', 'getAttribute', 'getAttributeNS', 'getAttributeNode', 'getAttributeNodeNS', 'getElementsByTagName', 'getElementsByTagNameNS', 'getInterface', 'getUserData', 'hasAttribute', 'hasAttributeNS', 'hasAttributes', 'hasChildNodes', 'insertBefore', 'isSameNode', 'isSupported', 'lastChild', 'localName', 'namespaceURI', 'nextSibling', 'nodeName', 'nodeType', 'nodeValue', 'normalize', 'ownerDocument', 'parentNode', 'prefix', 'previousSibling', 'removeAttribute', 'removeAttributeNS', 'removeAttributeNode', 'removeAttributeNodeNS', 'removeChild', 'replaceChild', 'schemaType', 'setAttribute', 'setAttributeNS', 'setAttributeNode', 'setAttributeNodeNS', 'setIdAttribute', 'setIdAttributeNS', 'setIdAttributeNode', 'setUserData', 'tagName', 'toprettyxml', 'toxml', 'unlink', 'writexml']

print(root.nodeName)  # bookstore

books = root.getElementsByTagName('book')
print(type(books))  # <class 'xml.dom.minicompat.NodeList'>

for book in books:
    titles = book.getElementsByTagName('title')
    print(titles[0].childNodes[0].nodeValue)
    # Harry Potter
    # Learning XML
