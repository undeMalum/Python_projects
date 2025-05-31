if __name__ == "__main__":
    numbers = [1, 13, 0, 10, 5]
    print(type(numbers))
    
    # adding to the list
    
    # append
    print(numbers)
    numbers.append(5)
    print(numbers)
    
    # extend
    strings = ["a", "b"]
    numbers.extend(strings)
    print(numbers)
    
    # removing stuff
    
    # pop
    top = numbers.pop()
    print(top, numbers)
    
    # remove
    numbers.remove("a")
    print(numbers)
    
    # Other stuff
    
    # sorting
    # a)
    numbers.sort()
    print(numbers)
    # b)
    numbers = [1, 13, 0, 10, 5]
    numbers_sorted = sorted(numbers)
    print(numbers_sorted)
    