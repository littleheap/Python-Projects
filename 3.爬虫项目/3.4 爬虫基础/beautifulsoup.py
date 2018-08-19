from bs4 import BeautifulSoup

soup = BeautifulSoup(open('./example/test.html'))
# print(soup.prettify())
'''
    <html>
     <head>
      <title>
       The Dormouse's story
      </title>
     </head>
     <body>
      <p class="title" name="dromouse">
       <b>
        The Dormouse's story
       </b>
      </p>
      <p class="story">
       Once upon a time there were three little sisters; and their names were
       <a class="sister" href="http://example.com/elsie" id="link1">
        <!-- Elsie -->
       </a>
       ,
       <a class="sister" href="http://example.com/lacie" id="link2">
        Lacie
       </a>
       and
       <a class="sister" href="http://example.com/tillie" id="link3">
        Tillie
       </a>
       ;
    and they lived at the bottom of a well.
      </p>
      <p class="story">
       ...
      </p>
     </body>
    </html>
'''

# Tag

print(type(soup.title))  # <class 'bs4.element.Tag'>
print(soup.title.name)  # title
print(soup.title)  # <title>The Dormouse's story</title>

# String
print(type(soup.title.string))  # <class 'bs4.element.NavigableString'>
print(soup.title.string)  # The Dormouse's story

# Comment
print(type(soup.a.string))  # <class 'bs4.element.Comment'>
print(soup.a.string)  # Elsie

for item in soup.body.contents:
    print(item.name)
'''
None
p
None
p
None
p
'''

# CSS查询
print(soup.select('.sister'))
'''
    [<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, 
    <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, 
    <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
'''
print(soup.select('#link1'))
# [<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]
print(soup.select('head > title'))
# [<title>The Dormouse's story</title>]

a_s = soup.select('a')
for a in a_s:
    print(a)
'''
    <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
    <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
    <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
'''
