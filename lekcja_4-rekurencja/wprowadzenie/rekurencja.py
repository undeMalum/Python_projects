

def say_hello_for(ilosc):
    for i in range(ilosc):
        print("Hello!")


print("Say hello wersja a pętlą for")

say_hello_for(3)


def say_hello_recursion(ilosc):
    if ilosc == 0:
        return
    print("Hello!")
    say_hello_recursion(ilosc - 1)


print("Say hello wersja rekurencyjna")
say_hello_recursion(3)


def open_box(level):
    print("Opening box", level)
    if level == 1:
        print("Found the toy!")
        return
    open_box(level - 1)
    print("Closing box", level)

print("--------")
open_box(3)
