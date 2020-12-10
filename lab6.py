


"""
To start, we will generate a random integer between 1 and 20, and based on
the result of the random number, we check to see if it fall under certain range
if the number is greater than 15 , then the results will be "cherries"
otherwise if the number is > 10, the result will be "Orange"
otherwise if the number is > 5, the result will be "Plum"
otherwise if the number is > 2, the result will be "Melon"
otherwise if the number is > 1, the result will be "Bell"
if the result is not any of the above, the result will be "bar"

we iterate over using a loop three times and print the results to the user. As an example
"Plum, cherries, Melon'


"""
"""
import random
num = generate random number

if num is greater than 15 , 
    then the results will be "cherries"
otherwise if num is > 10, 
    then result will be "Orange"
otherwise if num is > 5,
     then result will be "Plum"
otherwise if num is > 2, 
    then result will be "Melon"
other wise if num is > 1,
    then the result will be "Bell"
otherwise
    the result will be "Bar"

loop three times
    print the outout (fruit) to the user


"""
import random

def main():
    for i in range(0, 3):
      spin()

def spin():
    rand_num = random.randint(1, 20)
    output = ""
    if (rand_num > 15):
        output = "Cherries"
    elif(rand_num > 10):
        output = "Orange"
    elif (rand_num > 5):
        output = "Plum"
    elif(rand_num > 2):
        output = "Melon"
    elif(rand_num > 1):
        output = "Bell"
    else:
        output = "Bar"

    print(output, end=" ")

main()


