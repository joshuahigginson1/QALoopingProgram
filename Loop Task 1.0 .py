#Python Excercise Loop Task V1.0
#Joshua Higginson


#Variables

loop_total = 100
square_limit = 200


#Loop Function


#Code to loop between numbers

for i in range(loop_total):
    print('The square of', i, 'is', i**2)
    if i**2 >= square_limit:
        break
    else:
        continue

print("The program has reached the squared limit of " + str(square_limit) + "!")
