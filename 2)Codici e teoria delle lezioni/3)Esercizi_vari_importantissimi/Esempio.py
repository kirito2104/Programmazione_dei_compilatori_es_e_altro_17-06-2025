def func(a):
    d = {}
    for x in a:
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1


    print(d[5])
    return (max(a,key=lambda x: d[x]))

print(func([1, 2, 3, 2, 5, 1, 5, 5]))  # Output: 2

d = {"1":10,"2":20,"3":30}
print(lambda x: d[x])  # Output: "2"

print()