sciezka = r"C:\Users\Mateusz\Desktop\Python_projects\Project 1\lekcja_5-czytanie_plików\zadanie_4\dane.txt"



with open(sciezka) as plik:
    linia = plik.readline()
    lista = plik.readlines()

print(lista)
print(linia)
print("Hello\nworld")

linia = "    \n     " + linia + "    \n"
print(linia)
print("-----")
linia = linia.strip()
print(linia)
print(linia.split())
print("------")