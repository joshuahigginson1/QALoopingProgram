#Python Excercise Loop Task V1.0
#Joshua Higginson


#Variables

loop_total = 100
square_limit = int(input("Please enter the program square limit: "))
power_function = int(input("Please enter your chosen power: "))


#Loop Function


#Code to loop between numbers

for i in range(1, loop_total):
    print(i, 'to the power of', power_function, 'is', i**power_function)
    
    if i**power_function >= square_limit:
        break
    
    else:
        continue

print("The program has reached the squared limit of " + str(square_limit) + "!")

# Program End
