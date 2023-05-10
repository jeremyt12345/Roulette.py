#Jeremy Thomas

##   Input: Name of Inventory file
#          Item record field data - Description, Quantiy & Price
#
#   Processing: 1. Display menu & prompt user for choice
#               2. Drive menu options
#                   1 - Create new Inventory file
#                       Open file in writing mode
#                       Close file
#                   2 - Add item Inventory
#                       Prompt user for item record field data
#                       Open file for appending
#                       Write item record to file
#                       Close file
#                   3 - Display items in Inventory
#                       Open file for reading
#                       While there are records in the file:
#                           Read description, quantity, price
#                           Display item record data
#                       Close file
#                   4 - Generate Inventory Price Summary
#                       Open file for reading
#                       Initialize item counter, price accumulator, lowest & highest
#                       While there are records in the file:
#                           Read description, quantity, price
#                           Increment item counter
#                           Update price accumulator
#                           Determine if item price is new lowest / highest
#                       Calculate average price
#                           average price = price accumulator / item counte
#                       Display Inventory price summary
#                   5 - Quit
#
#   Output: List of items in the Inventory
#           Inventory Price Summary

def main():
    # Our Intro
    print("Invenotry Control App ...")

    # Show constants and variables
    QUIT = 5 # if user puts 5 program ends
    choice = 0 # menu control variable

    while choice != QUIT:
        # Display menu & prompt user for choice
        print("\nChoose one of the following options")
        print("\t1. Create new Inventory file.")
        print("\t2. Add Item Inventory.")
        print("\t3. Display Items in Invenotry.")
        print("\t4. Generate Inventory Price Summary")
        print("\t5. Quit")

        # First menu option
        if choice == 1:#New file
            print("\nCreating new Inventory File ...", end=" ")
            createFile("inventory.txt")
            print("\"inventory.txt\" successfully created")

        elif choice == 2: #add item
            print("\nAdding item to Inventory ...")

            #Prompt user for item information
            description, quantity, price = getItem()

            # Append item to inventory.txt
            addItem(description, quantity, price, "inventory.txt")

        elif choice == 3: #Display file
            print("\nDisplaying items in Inventory ...")
            displayFile("inventory.txt")

        elif choice == 4: #Process File Data
            print("\nGenerating Inventory Price Summary")

        elif choice == 5: #quit program
            print("\nGood Bye ...")
            print()
            
        else: # Invalid input
            print("\Please enter valid number, 1-5, Try again")


            #
            #createFile(filename)
            #
            # Creates an empty file named filename
            #
            #Return Value: None
            def createFile(filename):
                #Open file for writing - create a new one if it already exists
                outFile = open(filename, "w")
                #close file
                outFile.close()

            #
            # getItem()
            #
            # Prompts user for inventory record fields
            # - item description <string>
            # - item quantity (>=0) <int>
            # - item price (>=0) <float>
            # and returns them back to the caller
            #
            # return values : <item description> <item quatity> <item price>
            def getItem():
                print("\nPlease enter the following data ...")

                # prompt user for the item description, quanitiy and price
                description = input("\t" + format("Item description: ", "<20s"))

                # quantity (>=0)
                                    
                quantity = -1
                while quantity < 0:
                    try:
                        quantity = int(input("\t" + format("item price: ", "<20s")))

                        if quantity < 0:
                            print("\tError ... Invalid price. Try again .")
                    except ValueError:
                        print("\tError ... Price must be a number. Try again")

            return description, quantity, price

                #
                # addItem(desc, qty, price, filename)
                #
                # Appends and Inventory record with fields:
                # item description <desc>
                # item quantity <qty>
                # item price <price>
                # to the file named filename, one field per line
                #
                # return value: None
                #
            def addItem(desc,qty, price, filename):
                    try:
                        #Open file for appending
                        outfile = open(filename, 'a')

                        #Write item data to file - one field per line
                        outFile.write(desc + '\n')
                        outFile.write(str(qty) + '\n')
                        outFile.write(str(price) + '\n')

                        # close file
                        outFile.close()
                    except:
                        print("Fatal Error ... Could not open file", filename)


                 #
                 # displayFile(filename)
                 #
                 # Displays a table containing Inventory records stored in file named Filename
                 #
                 # Return Vale: None
                 #
            def displayFile(filename):
                     try:
                         # Open File
                         inFile = open(filename, "r")

                         #Display Table Header
                         print()
                         print("{0:<20s} {1:^10s} {2:^15s}".format("Description", "quantity", "price"))
                         print("-"*47)

                         #read file one record at a time & display it

                         #read first item description
                         itemDesc = inFile.readline()

                         while itemDesc != "":
                             #Read item quatity & price
                             itemQty = inFile.readline()
                             itemPrice = inFile.readline()

                             #strip \n from fields
                             itemDesc = itemDesc.rstrip('\n')
                             itemQty = itemQty.rstrip('\n')
                             itemPrice = eval(itemPrice)

                             #Convert numerix values
                             itemQty = eval(itemQty)
                             itemPrice = eval(itemPrice)

                             # Display Record
                             print("{0:<20s} {1:^10d} {2:>12,.2f}" .format(itemDesc, itemQty, itemPrice))

                             # Read next item description
                             itemDesc = inFile.readline()

                             # Close file
                         inFile.close()
                     except FileNotFoundError:
                         print("Fatal Error ...", filename, "not found.")
                     except IOError:
                         print("Fatal Error ... could not read", filename)

                   #
                   #Pricesummary(filename)
                   #
                   # read item records from inventory file named file name, determines
                   # and displays:
                   # -number of items in inventory
                   # -lowest price in inventory
                   # -Average price of items in Inventory
                   #
                   # return value:none

            def priceSummary(filename):
                       #Import library
                       import sys

                       #intialize variables
                       itemCount = 0 # number of items in inventory
                       lowPrice = sys.float_info.max # lowest price in inventory
                       highPrice = sys.float_info.min #Highest price in inventory
                       priceSum = 0.0 #Sum of Prices in inventory
                       priceAvg = 0.0

                       try:
                           #Open file
                           inFile = open(filename, "r")

                           # read file one record at the time to determine
                       
                             

            

                                    


            
            

        

        
            
                  
        
        
    
