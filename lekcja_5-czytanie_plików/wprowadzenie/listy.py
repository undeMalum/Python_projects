a = ["a", "b", "c", "d", "e", "f", "g", "h"]

print(a[3])

print(a[-3])

print(a[1:3]) # <1,3),  range(1,3) -> 1, 2

print("----")
print(a[1:-1])
print(a[1:])

print(a[3:5])

print(a[:3])

print(a[1:6:2])

print(a[:7:3])

print(a[-1:3:-1])

print(a[::-1])

b = ["i", "j", "k", "l", "m", "n", "o", "p"]

print(a + b)
# myinvers(["b", "c", "d"]) + ["a"]
# myinvers(---------------)  + [lista[0]]

# mvinvers(["c", "d"]) + [lista[0]]       + ["a"]
# myinvers(["c", "d"]) + ["b"] + ["a"]


# myinvers(lista[1:]) + [lista[0]]


"""
1. list = ["a", "b", "c", "d"]
a. myinvers(lista[1:]) + [lista[0]]
   myinvers(["b", "c", "d"]) + ["a"]
   +----------------------------------> 2. lista = ["b", "c", "d"]
                                        a. myinvers(lista[1:]) + [lista[0]]
                                           myinvers(["c", "d"]) + ["b"]
                                           +-----------------------------------> 3. lista = ["c", "d"]
"""

