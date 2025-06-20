numbers = [1, 13, 2, 10, 5]
temp1 = numbers[0]

temp2 = numbers[0]

for i in range(1, len(numbers)):
    if temp2 < numbers[i]:
        temp2 = numbers[1]
        
        
print(temp2)


for element in numbers:
    if temp1 < element:
        temp1 = element
        
        
print(temp1)
