######################################################################################################################################
#  1. Just enter a natural number.                                                                                                         #
# I am just a mother trying to learn Phyton. Please give me a like!                                                                  #
######################################################################################################################################

def doCollatz(number ):
        if(number==1):
            return
        else:
            if(number % 2 == 0):
                number = number/2
                print(number)
                
                doCollatz(number)
            else:
                number = number*3+1
                print(number)
                doCollatz(number)

           

try:
    userInput=int(input("Please enter a natural number:"))
    doCollatz(userInput)
except (ValueError, TypeError):
    print("You have entered a not natural number;therefore, the program will stop")






