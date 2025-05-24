    # FOUND = FALSE
    # loop I from 0 to NUMS.Length()-3
    #   if NUMS[I] = 1 and NUMS[I+1] = 2 and NUMS[I+2] = 3 then
    #     FOUND = TRUE
    #   end if
    # end loop
    # output FOUND
    

# strings = ["a", "b", "c"]
# alternated = [1, 2, "a", "b", [1, 2, 3]]


if __name__ == "__main__":
    numbers = [4, 5, 1, 2, 3, 7]
    
    # for i in range(1, 6, 2):
    #     ...
    # length = len(numbers)
    found = False

    for i in range(len(numbers) - 3):
        if numbers[i] == 1 and numbers[i+1] == 2 and numbers[i+2] == 3:
            found = True
            
    print(found)
