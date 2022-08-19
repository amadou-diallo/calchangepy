#!'/usr/bin/env python 3

# getCoin function
def getCoin(coinType) :
    c = -1
    while c < 0:
        try:
          c = int(input("How many " + coinType + " do you have? "))
          if c < 0:
              print("Coin counts cannot be negative. Please re-enter.")
        except ValueError:
            print("Illegal input. Must be non negative integer. re-enter." )
            c = -1
    return c

# display welcome message
print ("Welcome to the Change Calculator")
print()

grandtotal = 0
choice = input("Do you have change (y/n) ? ")
while choice.lower() == "yes":
    
    h = getCoin("Half- dollars")
    q = getCoin("Quarters ")
    d = getCoin("Dimes")
    n = getCoin("Nickels")
    p = getCoin("Pennies")
    print()
    
    totVal = (h*50) + (q*25) + (d*10)+ (n*5) + p
    print("You have " + str(totVal) + " cents.")

    grandtotal += totVal
    dollars  = totVal //100
    cents = totVal % 100
    print("which is " + str(dollars) + " dollars and "
          + str(cents) + " cents.")

    print()
    
    choice = input("Do you have more change (y/n) ? ")
    print()
    

print("You had a grand total of " + str(grandtotal) + " cents.\n"  +
           "Which is " + str(grandtotal//100) + " dollars and " + str(grandtotal % 100)
          + " cents.")
    
print("Thanks for Using the Change Calculator.")
    


