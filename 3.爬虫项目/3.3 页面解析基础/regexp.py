import re

m = re.match(r'\d{3}\-\d{3,8}', '010-12345')
print(dir(m))
print(m.string)  # 010-12345
print(m.pos, m.endpos)  # 0 9

# 分组
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.groups())  # ('010', '12345')
print(m.group(0))  # 010-12345
print(m.group(1))  # 010
print(m.group(2))  # 12345

# 分割
p = re.compile(r'\d+')
print(type(p))  # <class '_sre.SRE_Pattern'>
print(p.split('one1two3three3four4'))  # ['one', 'two', 'three', 'four', '']
print(m.group(2))  # 12345

t = '20:15:45'
s = re.match(
    r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$',
    t)
print(s.groups())  # ('20', '15', '45')
