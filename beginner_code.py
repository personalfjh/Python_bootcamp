# This code might be complex for beginner level so, you can double check all these codes on my replit
# "https://replit.com/@FranciscoHern11"

# First-day code, learning to use print, input, len and variables.


# -------------------------------------------------------------------------------------------------------
# Please ignore this section is just an easy way to select which code you want to run just read the comments
import time



class Beginner:
    """Needs two string inputs, one for day and the second for the option"""

    def __init__(self):
        self.functions = {1: self.day_1, 2: self.day_2, 3: self.day_3}
        self.option = 0

    def call_function(self, days, numbers):
        self.functions[days](numbers)
# -------------------------------------------------------------------------------------------------------

# -----------------------------------------------DAY 1--------------------------------------------------------
    def day_1(self, option):
        self.option = option
        if self.option == 1:
            # Use of Print
            # print is use to show data on the information that you want in the console of python
            # "\n" is a newline
            print("Hello World! \nWelcome to my path \nprint('This is a Test')")
            print("Hello" + " " + "Angela")
            # first exercise day_1
            time.sleep(1)
            print("Day 1 - Python Print Function")
            print("The function is declared like this:")
            print('print("what to print")')
            time.sleep(1)
            # Second exercise day_1
            # You can use " double " or ' quotes
            print("Day 1 - String Manipulation")
            print('String Concatenation is done with the "+" sign.')
            print('e.g. print("Hello " + "world")')
            print("New lines can be created with a backslash and n.")

        elif self.option == 2:
            # Use of Input
            # Input is used to get information from the python console.
            # Python interpreter checks the most intern command this means Input will be executed first
            print("Hello " + input("Whats your name? "))

            # Use of Len
            # Len is use to count the number of characters in a variable
            print(f' The total of letters of your name is {len(input("What is your name?"))}')

        elif self.option == 3:
            # Write a program that switches the values stored in the variables a and b.
            # Third exercise day_1
            # 🚨 Don't change the code below 👇 (code given in the exercise)
            print('Type two numbers "a" and "b"')
            a = input("a: ")
            b = input("b: ")
            # 🚨 Don't change the code above 👆 (code given in the exercise)

            ####################################
            # Write your code below this line 👇
            c = a
            a = b
            b = c

            # Write your code above this line 👆
            ####################################

            # 🚨 Don't change the code below 👇 (code given in the exercise)
            print("a: " + a)
            print("b: " + b)

        elif self.option == 4:
            # Final exercise Name Band Generator
            print("Welcome to the band name generator")
            city_name = input("What's the name of the city you grew up?\n")
            pet_name = input("What's your pet's name?\n")
            print("Your name band could be " + city_name + " " + pet_name)

    # -----------------------------------------------DAY 2--------------------------------------------------------
    def day_2(self, option):
        self.option = option
        # Understanding Data Type: String, Integer, Float, Boolean
        if self.option == 1:
            # Data Types
            # String
            print("Hello"[-1])
            # Integer
            print(1 + 5)
            # float
            print(3.14159)
            # Boolean
            print(True)
            print(False)

        elif self.option == 2:
            # First exercise day_2

            # Write a program that adds the digits in a 2 digit number. e.g. if the input was 35,
            # then the output should be 3 + 5 = 8

            # 🚨 Don't change the code below 👇 (code given in the exercise)
            two_digit_number = input("Type a two digit number: ")
            # 🚨 Don't change the code above 👆 (code given in the exercise)

            ####################################
            # Write your code below this line 👇
            digit_one = int(two_digit_number[0])
            digit_two = int(two_digit_number[1])
            result = digit_one + digit_two
            print(f'The result of add {digit_one} and {digit_two} is{result}')

        elif self.option == 3:
            # Second exercise day_2

            # Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
            # The BMI is a measure of some weight taking into account their height. e.g.
            # If a tall person and a short person both weigh the same amount,
            # the short person is usually more overweight.
            # The BMI is calculated by dividing a person's weight (in kg example 55)
            # by the square of their height (in m example 1.73)

            # 🚨 Don't change the code below 👇 (code given in the exercise)
            height = input("Enter your height in m: ")
            weight = input("Enter your weight in kg: ")
            # 🚨 Don't change the code above 👆 (code given in the exercise)

            # Write your code below this line 👇
            height = float(height)
            weight = float(weight)
            result = weight / height ** 2
            print(f' Your BMI is: {result}')

        elif self.option == 4:
            # Third exercise day_2

            # Create a program using maths and f-Strings that tells us how many days, weeks,
            # months we have left if we live until 90 years old.

            # 🚨 Don't change the code below 👇 (code given in the exercise)
            age = input("What is your current age?")
            # 🚨 Don't change the code above 👆 (code given in the exercise)

            # Write your code below this line 👇
            input_age = 90 - int(age)
            days = input_age * 365
            weeks = input_age * 52
            months = input_age * 12
            print(f"\nYou have {days} days, {weeks} weeks, and {months} months left")

        if self.option == 5:
            # Final exercise Tip Calculator

            # If the bill was $150.00, split between 5 people, with 12% tip.
            # Each person should pay (150.00 / 5) * 1.12 =
            # 33.6 Format the result to 2 decimal places = 33.60 Tip: There are 2 ways to round a number. You might have
            # to do some Googling to solve this.💪

            print("Welcome to the tip calculator!!")
            bill = input("Type the total bill? $")
            tip = input("What percentage of tip would you like to give? 10, 12, or 15? ")
            people = input("How many people to split the bill? ")
            split_bill = round((float(bill) * (1 + int(tip) / 100)) / int(people), 2)
            print(f"Each person should pay: ${split_bill}")

    # -----------------------------------------------DAY 3--------------------------------------------------------
    def day_3(self, option):
        self.option = option
        # Use of if, elif, else

        # Make a simple Roller coaster program.
        # if…elif…else are conditional statements that provide you with the decision making
        # that is required when you want to execute code based on a particular condition.

        if self.option == 1:
            print("Welcome to the Roller-coaster!")
            height = int(input("What is your height in cm? "))
            if height >= 120:
                print("You can ride the Roller-coaster")
                age = int(input("What is your age? "))
                if age < 12:
                    print("Child tickets are $5.")
                    bill = 5
                elif age <= 18:
                    print("Youth tickets are $7.")
                    bill = 7
                elif 45 <= age <= 55:
                    print("You get a free admission ticket.")
                    bill = 0
                else:
                    print("Adult ticket are $12.")
                    bill = 12
                want_photo = input("Do you want a photo taken? Y or N. ").upper()
                if want_photo == "Y":
                    bill += 3
                print(f"Your total is ${bill}.")
            else:
                print("Sorry, you need to be taller to be able to use the Roller-coaster.")

        if self.option == 2:
            # First exercise day_3
            # Write a program that works out whether if a given number is an odd or even number.
            # 🚨 Don't change the code below 👇 (code given in the exercise)
            number = int(input("Which number do you want to check? "))
            # 🚨 Don't change the code above 👆 (code given in the exercise)

            # Modulus - remainder of the division of left operand by the right
            # Write your code below this line 👇
            number = number % 2
            # print(number)
            if number == 0:
                print("This is an even number")
            else:
                print("This is an odd number")

        if self.option == 3:
            # Second exercise day_3
            # Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

            # 🚨 Don't change the code below 👇
            height = float(input("Enter your height in m: "))
            weight = float(input("Enter your weight in kg: "))
            # 🚨 Don't change the code above 👆

            # Write your code below this line 👇
            bmi = round(weight / height ** 2)
            if bmi < 18.5:
                print(f"Your BMI is {bmi}, you are underweight.")
            elif bmi < 25:
                print(f"Your BMI is {bmi}, you have a normal weight.")
            elif bmi < 30:
                print(f"Your BMI is {bmi}, you are slightly overweight.")
            elif bmi < 35:
                print(f"Your BMI is {bmi}, you are obese.")
            elif bmi >= 35:
                print(f"Your BMI is {bmi}, you are clinically obese.")

        if self.option == 4:
            # Third exercise day_3
            # Write a program that works out whether if a given year is a leap year.
            # A normal year has 365 days, leap years have 366, with an extra day in February.

            # 🚨 Don't change the code below 👇
            year = int(input("Which year do you want to check? "))
            # 🚨 Don't change the code above 👆

            # Write your code below this line 👇
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        print("Leap Year")
                    else:
                        print("Not leap year")
                else:
                    print("Leap year")
            else:
                print("Not leap year")

        if self.option == 5:
            # Fourth exercise day_3
            # Build an automatic pizza order program.

            # In this exercise I assumed that the user won't enter an incorrect value.
            # 🚨 Don't change the code below 👇
            print("Welcome to Python Pizza Deliveries!")
            size = input("What size pizza do you want? S, M, or L ").upper()
            add_pepperoni = input("Do you want pepperoni? Y or N ").upper()
            extra_cheese = input("Do you want extra cheese? Y or N ").upper()
            # 🚨 Don't change the code above 👆

            # Write your code below this line 👇
            bill = 0
            if size == "S":
                bill = 15
                if add_pepperoni == "Y":
                    bill += 1
            if size == "M":
                bill = 20
                if add_pepperoni == "Y":
                    bill += 3

            if size == "L":
                bill = 25
                if add_pepperoni == "Y":
                    bill += 3
            if extra_cheese == "Y":
                bill += 1

            print(f"Your final bill is: ${bill}.")

        if self.option == 6:
            # Final exercise Love Calculator day_3
            # You are going to write a program that tests the compatibility between two people.
            #
            # To work out the love score between two people:
            #
            # Take both people's names and check for the number of times the letters in the word TRUE occurs.
            # Then check for the number of times the letters in the word LOVE occurs.
            # Then combine these numbers to make a 2 digit number.

            # 🚨 Don't change the code below 👇(code given in the exercise)
            print("Welcome to the Love Calculator!")
            name1 = input("What is your name? \n").lower()
            name2 = input("What is their name? \n").lower()
            # 🚨 Don't change the code above 👆(code given in the exercise)

            # Write your code below this line 👇
            names = name1 + name2
            # TRUE
            occurs_true = 0
            occurs_true = names.count("t")
            occurs_true = occurs_true + names.count("r")
            occurs_true = occurs_true + names.count("u")
            occurs_true = occurs_true + names.count("e")
            data1 = str(occurs_true)
            # LOVE
            occurs_love = 0
            occurs_love = names.count("l")
            occurs_love = occurs_love + names.count("o")
            occurs_love = occurs_love + names.count("v")
            occurs_love = occurs_love + names.count("e")

            data2 = str(occurs_love)
            # Operation
            score = int(data1 + data2)
            if score < 10 or score > 90:
                print(f"Your score is {score}, you go together like coke and mentos.")
            elif 40 <= score <= 50:
                print(f"Your score is {score}, you are alright together.")
            else:
                print(f"Your score is {score}.")

