di = {'k1': 'v1', 'k2': 'v2'}

di['k3'] = 'v3'

di['k4'] = 'v4'

for k in di:
    print(di[k])
'''
    v1
    v2
    v3
    v4
'''

for k, v in di.items():
    print(k, v)
'''
    k1 v1
    k2 v2
    k3 v3
    k4 v4
'''
