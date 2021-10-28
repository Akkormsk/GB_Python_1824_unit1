src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

mylist = [*enumerate(src)]
res = [n for (i, n) in mylist[1:] if n > src[i-1]]
print(res)
