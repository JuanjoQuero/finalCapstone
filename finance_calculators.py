import math #just imported math to able our code to do more complex calculations.

#Create a welcoming message to our users.
text = '''WELCOME TO YOUR HOME FINANCE CALCULATOR.
You have 2 options:
Investment - to calculate the amount of interest you'll earn on your investment.
Bond - to calculate the amount you'll have to pay on a home loan.'''
print (text)

#Ask our user to enter the type of finance they want to calculate and pass it into lower case to avoid any miswriting error.
finance = input ("Please enter what type of finance would you like to calculate today: (investment/bond) \n")

new_finance = finance.lower ()

#I'm going to use a conditional if first option it's been selected. 
if new_finance == "investment":
    
    #We need to require from our user all information needed for our formulas. 
    p = float (input ("Enter amount of money depositing:"))
    interest_rate = float (input ("Enter interest rate:"))
    r = interest_rate / 100
    t = float (input ("Enter number of years planning to invest:"))
    #Cast into float just in case interest rate is coming with decimals. 
    interest = input ("Enter type of interest (simple/compound):\n")
    new_interest = interest.lower ()

    #Create a nest conditional for the 2 different types of interest and mathematical formulas applied
    if new_interest == "simple":
        total_amount = p * (1 + r * t)
        print (f"Total amount at the end of the invesment: {total_amount:.2f}")
    #noticed that it was returning a long list of decimals, so I've add {.2f} to get only 2 decimals in our result 
    #That was explained by Chris on last Saturday's live lecture (March 28th)
    elif new_interest == "compound":
        total_amount = p * math.pow ((1 + r), t)
        print (f"Total amount at the end of the invesment: {total_amount:.2f}")

    else:
        print ("You need to enter a valid interest type")

#create another conditional for "bond" option with the different inputs required from user
elif new_finance == "bond":

    p = float (input ("Enter present value of the house:"))
    interest_rate = float (input ("Enter interest rate:"))
    i = (interest_rate /100) / 12
    n = float (input ("Enter number of months you are planning to take to repay:"))

    repayment = (i * p) / (1 - (1 + i) ** (-n))

    print (f"Amount you will have to repay each month: {repayment:.2f}")

else:
    print ("You have to enter a valid option.")