string = "tablet"
print(string[-2])

# for i in range(0, len(numbers), 3):
#     print(numbers[i])

for i in range(len(string)):
    print(i, string[i])
 
print("\n\n")   
    
for i in range(len(string) - 1, -1, -1):
    print(i, string[i])
