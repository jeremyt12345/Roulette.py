# Jeremy Thomas
#twoNumbers.Py


# Prompt user for two values i & j (i<=j), calculate
# and display:
#     - List    of numbers from i to j (inclusive)
#     - Sum     of numbers from i to j 
#     - Product of numbers from i to j 
#     - Average of numbers from i to j


#   Input: Two values - i & j (i<=j)


# Process: 1. prompt uset to get to values
#          2. Determine & Display
#            -List
#            -Sum
#            -Product
#            -Average


#        Output^



def main():
    #intro
    print("\nPlaying with Numbers App ...")

    tryAgain = "y"

    while tryAgain == "y":
        #prompt user for two values
        i, j = getValues()

        #Determine & display list of numbers
        print("\From", i, "to", j, ":", listValues(i,j))

        #Calculate & display sum, product and average of number
        print("\n\tSum    of Values:", format(sumValues(i,j), '10d'))
        print("\tProduct of Values:", format(productValues(i,j), '10d'))
        print("\tAverage of Values:", format(averageValues(i,j),'10.3f'))

        #Prompt user whether to try again
        tryAgain = input("\nWould you like to try again (y/n)? ").lower()

        #getvalues()

        #prompt user for two values n1, n2 & return them back
        #to the caller so n1<=n2

        # return values:n1,n2

        def getValues():
            #prompt user
            n1,n2 = eval(input("\nPlease enter two numbers (separated by ,): "))

            #swap values if needed
            if n1 > n2
            temp = n1
            n1 = n2
            n2 = temp

            # return numbers to the caller
            return n1,n2

        # listValues(n1,n2)
        #  create & return, as a string, the list of numbers
        # from n1 to n2 (inclusive)
        #
        # Return Value:string containing the list of number from n1 to n2(inclusive)

        def listValues(n1,n2):
            #intialize string of values
            1stString ""

            #Build the string one number at a time
            for value in range(n1, n2+)
            1stString = 1stString + str(value) + " "

            # Return Value:
    
