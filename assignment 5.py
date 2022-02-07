def fun(n):
  return n % 3 == 0 or n % 5 ==0
li = [2, 3, 9, 4, 6, 1, 5, 7, 8,12,15,18,21,27,30]
print(list(filter(fun, li)))