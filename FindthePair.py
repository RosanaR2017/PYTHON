#  Instruction: Enter a pair of integer numbers and expect the result. If there exist a pair of numbers which sum is contained in the array the
#  the code will print that you have found the pair.
#  My comments: I do not know if this reach the goal, I used simple logic since the numbers follows this sequence  
#  i=0,0,0,1,1,1,2,2,3 j=1,2,3,2,3,3 for an array size of 4.
#  Maybe there is a better solution with Binary Search. Tomorrow, I will figure out. 
#  Last modification: 5-31-2019   Please like and comment any improvement. 



def getMyOtherHalf(a,b,items):

    sum=a+b 
    j=1
    i=0

    while i!=len(items)-1:

        while j<= len(items)-1:
       
            if items[i] + items[j] ==sum:
                print("The pair is number {} and number {}".format(items[i],items[j]))
                return
            else:
                j += 1

        j =i+1
        i+=1

    print("There is no pair")
    return


items = [-10,-1,-1, 0, 0, 0, 1, 2, 4, 4, 90]
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

getMyOtherHalf(a,b,items)


