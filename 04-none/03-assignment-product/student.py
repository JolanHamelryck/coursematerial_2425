def product(a, b, c):
    #a = a if not None else a = 1

    if a is None:
        a = 1
        print(a)
    if b is None:
        b = 1
    if c is None:
        c = 1
    
    #b = b if not None else 1
    #c = c if not None else 1

    return a * b * c

print(product(None, 10, 0))
#print(product(2, 10, 0))