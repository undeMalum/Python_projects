path = ""

with open(path, "r") as file:
    counter = 0
    lines = file.readlines() # ["line 1", "line 2", "line 3", ...]
                             # index 0,  index 1,    index 2, ....
    
    for line in lines:
        ...
    
