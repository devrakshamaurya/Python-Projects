#lambda function
#return cube

def cube(num):
    return num **3
cube = lambda x: x ** 3

print(cube(3))


#function with *args
#write a function that takes variable number of arguments and returns their sum

def sum_all(*args):
    print(args)
    for i in args:
        print(i * 2)
    return sum (args)
print (sum_all(1, 2, 3))    


#Recursive function
#creaate a recursive function to calculate the factorial of a number.


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)