import time
import sys


ans = True

while ans:


    menu = input ("""

    1. Beer bottles

    2. Info sheet

    3. Deposit calculator
    
    Please select and option: """)

    if menu == "1":
        bottles = 99

        while bottles != 0:
            bottlesFalling = bottles - 1
            print (str(bottles) + (" bottles of beer on the wall, ") + str(bottles) + (" bottles of beer. Take one down, pass it around, ") +  str(bottlesFalling) + (" bottles of beer on the wall... "))
            time.sleep(0.5)
            bottles = bottles - 1
            
            if bottles == 0:
                print ("No more bottles of beer on the wall, no more bottles of beer.")
                sys.exit
    
    elif menu == "2":
        gdpr = input ("Are we able to collect some information about you?: ")

        if gdpr == "yes":

            name = input ("What is your name: ")
            if len(name) < 3:
                print("Please enter more than 3 characters")

            else:
                age = input("How old are you? ")

                height = input ("How tall are you in inches? ")

                weight = input ("How much do you weigh in pounds? ")

                eye = input ("What is your eye color? ")

                Hair = input ("What color is your hair? ")


    elif menu == "3":
        portion_deposit = 0
        current_savings = 0
        r = 0.04

        annual_salary = input ("Please enter your current annual salary: ")
        portion_saved = input ("Please enter how much you would like to be saved, as a decimal: ")
        total_cost = input ("Please enter the cost of your dream home: ")

        months = 0

        annual_salary = int (annual_salary)
        portion_saved = float(portion_saved)

        current_savings = annual_salary*r/12

        monthly_salary = annual_salary/12

        portion_saved = portion_saved*100

        current_savings = monthly_salary/portion_saved

        total_cost = float(total_cost)
        months = float(months)

        months = total_cost/current_savings

        print (months)


        #Ive done something severely/simply wrong
