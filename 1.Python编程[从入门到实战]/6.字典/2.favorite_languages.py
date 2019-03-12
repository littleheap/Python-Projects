# 遍历字典
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
'''
    Jen's favorite language is Python.
    Sarah's favorite language is C.
    Edward's favorite language is Ruby.
    Phil's favorite language is Python.
'''

# 遍历键
for key in favorite_languages.keys():
    print(key)
    '''
        jen
        sarah
        edward
        phil
    '''

# 遍历值
for value in favorite_languages.values():
    print(value)
    '''
        python
        c
        ruby
        python
    '''