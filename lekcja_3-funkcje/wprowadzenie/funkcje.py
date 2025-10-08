def przedstaw_sie(imie, nazwisko, drugie_imie="", *, wiek=""):
    print(f"Jestem {imie} {drugie_imie} {nazwisko}. Miło was poznać.")

przedstaw_sie("Konat", "Mateusz")

przedstaw_sie("Wiktor", "Piechowiak", "Marcin")


def przedstaw_sie_2(imie, nazwisko):
    return f"Jestem {imie} {nazwisko}. Miło was poznać."

print(przedstaw_sie_2("Konat", "Mateusz"))

