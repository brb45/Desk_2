

test = dict([("rate",'cck'),("tech",'wifi'),('channel','5810')])
key = list(test.keys())
val = test.values()

print(type(key))
new_test = dict(zip(key,val))

for key, value in new_test.items():
    print(key,value)
    print ("###")