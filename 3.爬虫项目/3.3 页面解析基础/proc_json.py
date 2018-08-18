import json

obj = {'one': '一', 'two': '二'}

encoded = json.dumps(obj)
print(type(encoded))  # <class 'str'>
print(encoded)  # {"one": "\u4e00", "two": "\u4e8c"}

decoded = json.loads(encoded)
print(type(decoded))  # <class 'dict'>
print(decoded)  # {'one': '一', 'two': '二'}
