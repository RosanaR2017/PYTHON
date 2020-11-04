def binarySearch(lower, upper, sum, items):
   
    #Get midpoint
    midPoint= (lower+upper)//2  # // is the floor divisor

    if lower != upper:   #If lower equls upper that means there is no value there.
        if items[midPoint] == sum :
            print("The value: {} is found at index: {}".format(midPoint,items[midPoint]))
            return  
        else: 
            if items[midPoint] < sum :
                lower = midPoint+1
            else:
                upper= midPoint-1
            return binarySearch(lower,upper,sum,items)
    else:
        print("Not found")
        return   


items = [1,2,4,4]

a=int(input("Enter first number:"))
#b=int(input("Enter first number:"))
#sum=a+b
binarySearch(0, len(items)-1,a,items)