import random

#print("Hello, whats your favorite number?")
#number = input()

#print("Your favorite number is " + str(number))


minNumber = 1
maxNumber = 1000
magicNumber = random.randint(minNumber,maxNumber)

message = "The magic number is between {0} and {1}"
print(message.format(minNumber,maxNumber))

found = False

while not found:
    print("Guess what it is?")
    guess = int(input())

    if guess == magicNumber:
        found = True
    if guess < magicNumber:
        print("Too low")
    if guess > magicNumber:
        print("Too high")

print("You got it!")

