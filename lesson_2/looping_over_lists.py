if __name__ == "__main__":
    numbers = [1, 13, 0, 10, 5]
    
    # for loop
    for i in range(len(numbers)):
        numbers[i] = numbers[i] * 2 # numbers[i] *= 2
        print(numbers[i])
        
    # while
    i = 0
    while i < 5:
        print(numbers[i])
        i += 1
        
    # *For loop on the list itself
    for number in numbers:
        print(number)
    