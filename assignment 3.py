x= {"a":6, "b": 2, "c": 3,"d": 4}
# print(type(x))
max_value = max(x,key=x.get)
print(max_value)