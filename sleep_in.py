#   if NOT WEEKDAY OR VACATION then
#     output TRUE
#   else
#     output FALSE
#   end if


# type()
type_of_employment = "engineer"
print(type(type_of_employment))

type_of_employment = 6
print(type(type_of_employment))

type_of_employment = 6.5
print(type(type_of_employment))

# WEEKDAY = 6

# age, gender, hair = 24, "male", "blue"


"""
if (weekdat==0) or (vacation==1) {print(True);}

"""

if __name__ == "__main__":
    weekday = True
    vacation = False

    if not weekday or vacation: 
        print(True)
    elif vacation:
        print("Gotcha")
    else:
        print(False)
    