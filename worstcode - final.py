import random
import time

def print_picture():
    # Define your ASCII art or Unicode pictures
    picture = [
        "   _\\/_,",
        "  //o o\\",
        " ('_'= )",
        " /'--'\\",
        "and you had no shame typing that 🤨?"
    ]

    # Print the picture
    for line in picture:
        print(line)

def multiply_numbers():
    print("Welcome to the Doofenshmirtz Number Multiplier Incorporated!")
    print("Input two numbers and I will multiply them for you when I feel like it.")

    # Taking user inputs
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("I said a number. Use your overworked stressed braincells.")

    # Multiplying the numbers
    result = num1 * num2

    # Printing a random picture in the top-left corner
    print("\n")
    print_picture()

    # Pause for 20 seconds before showing the quote
    time.sleep(20)

    # Printing a random quote
    print("\nAnd now, for a little quote:")
    print(random.choice([
        "loading it in 3..2..1... I didn't feel like it",
        "qhhbnisfooajnfnasjfbubewibnjsd. - who knows",
        "tell your cat I said pspspspsps. - Fellow Cat Lover",
        "An apple a day keeps everyone away. if you just throw it hard enough. - A S.",
        "Error404"
    ]))

    # Pause for another 20 seconds before showing the riddle
    time.sleep(20)

    # Printing a joke
    print("\nAnd now, for a little joke:")
    print(random.choice([
        "imagine i crash",
        "the job scope for your field",
        "Wisdom has always been chasing you but you've always been faster",
        "Think about it while I calculate the result...",
    ]))
    # Simulating a longer processing time
    print("Calculating result...")
    for i in range(60):  # This loop will run for approximately 10 minutes
        if i == 1:
            print("Just one minute...")
        elif i == 5:
            print("Oh no! crashed...")
        elif i == 8:
            print("No! I didn't!")
        elif i == 11:
            print("5 minutes...")
        elif i == 12:
            print("45 minutes...")
        elif i == 54:
            print("keep waiting'")
        elif i == 55:
            print("You asked a very dumb question. Keep waiting...")
        else:
            time.sleep(45)  # Sleep for some seconds per iteration

    # Printing the result
    print("\n")
    print("The result of multiplying", num1, "and", num2, "is:", result)

if __name__ == "__main__":
    multiply_numbers()
