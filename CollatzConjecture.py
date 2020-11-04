######################################################################################################################################
#  1.Enter a natural number.                                                                                                         #
# 2. Please note that I establish a limit of cycles, in case you just think that you have solved                                     #
# a mathematical ancient problem..In other words, do you think that there is a number that will break this sequence...I don't know   #
# I am just a mother trying to learn Phyton. Please give me a like!                                                                  #
######################################################################################################################################

def doCollatz(number ):
    count=0
    while (number!=1):
        count +=1
        if (number % 2 == 0):
            number = number/2
        else:
            number = number*3+1
        print("iteration n°:{}".format(count))
        print(number)
        

        if (count ==2000):  #Enter the number of cycles that you want to give to this testing
        #The following block can be deleted unless you think there is a solution for this problem. 
            print("""You find a positive number                    
            who doesn\'t comply with the Collatz conjeture which 
            is unexplicable or you have just reach the maximun number of cycles in this program""")
            break    

try:
    userInput=int(input("Please enter a natural number:"))
    doCollatz(userInput)
except (ValueError, TypeError):
    print("You have entered a not natural number;therefore, the program will stop")






