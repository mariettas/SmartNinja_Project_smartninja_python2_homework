print("Hello, welcome to the fizzbuzz game!")

choice = int(input("Please, enter a number between 1 and 100: "))


for x in range(1, choice + 1):

    if x % 3 == 0 and x % 5 == 0:
        print("fizzbuzz")
    elif x % 3 == 0:
        print("fizz")
    elif x % 5 == 0:
        print("buzz")
    else:
        print(x)
