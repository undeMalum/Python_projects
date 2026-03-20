sciezka = " dane.txt"

lista2d = []

with open(sciezka) as plik:
    for _ in range(200):
        wiersz = plik.read_line()
        
        # 0 1 2 0 1 2
        print(wiersz)
        
        int()
        # ['0', '1', '2']
        wiersz_lista = list(map(int, wiersz.strip().split()))
                       #[int(element) for element in wiersz.strip().split()]
        
        lista2d.append(wiesz_lista)
        
    
    
"""
lista2d = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

szesc = lista2d[1][1]
dwojka = lista2d[0][1]
piatka = lista2d[1][0]
siodemka = lista2d[1][2]
dziesiatka = lista2d[2][1]


for i in range(wiersze):
    for j in range(kolumny):
        print(lista2d[i][j])
        print("Sąsiad po prawej", lista2d[i][j+1]) 3 + 1 = 4
        print("Sąsiad po lewej", lista2d[i][j-1])  0 - 1 = -1
"""
    
"""
0 0 0 0\n
23 32 1 2\n
...
"""
