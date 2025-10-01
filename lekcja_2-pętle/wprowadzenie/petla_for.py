# range(od, do, krok)
# range(2, 5) -> 2, 3, 4
# range(5) -> 0, 1, 2, 3, 4
# range(1, 6, 2) -> 1, 3, 5

# * range(5, 1, -1) -> 5, 4, 3, 2
# for i in range(5, 1, -2):
#     print(i)

for i in range(1, 21):
    print(i)

# * iteratory - przydatne pózniej do pracy na plikach
warzywa = ["pomidor", "sałata" "ogórek"]

for warzywo in warzywa:
    print(warzywo)

linie_pliku = ["Cześć", "jestem Matek"]
for linia in linie_pliku:
    print(linia)

for _ in range(10):
    print("Dzień Dobry")
