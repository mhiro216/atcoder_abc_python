s = input()

l = ['Sunny', 'Cloudy', 'Rainy']
l_next = l[1:]+l[:1]

d = {}
for k,v in zip(l,l_next):
    d[k] = v
    
print(d[s])