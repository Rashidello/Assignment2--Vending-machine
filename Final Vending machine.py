VMItems = {  #Dictionary created (VMItems is for Vending Machine Items)
    "1A": {  #Nested dictionary 
        "Code": "1A",  #Key: 'Code' & Value: '1A'
        "Item": "Soda",  #Key: 'Item' & Value: 'Soda'
        "Category": "Drink",  #Key: 'Category' & Value: 'Drink'
        "Price": 4,  #Key: 'Price' & Value: 4
        "Stock": 3,  #Key: 'Stock' & Value: 3
        "Related item": "1B"  #Key: 'Related item' & Value: '1B'
    },
    "2A": {  #Another nested dictionary
        "Code": "2A",  #Key: 'Code' & Value: '2A'
        "Item": "Milk",  #Key: 'Item' & Value: 'Milk'
        "Category": "Drink",  #Key: 'Category' & Value: 'Drink'
        "Price": 4,  #Key: 'Price' & Value: 4
        "Stock": 5,  #Key: 'Stock' & Value: 5
        "Related item": "2B"  #Key: 'Related item' & Value: '2B'
    },
    "3A": {  #Another nested dictionary
        "Code": "3A",  #Key: 'Code' & Value: '3A'
        "Item": "Chocolate Brownie",  #Key: 'Item' & Value: 'Chocolate Brownie'
        "Category": "Snack",  #Key: 'Category' & Value: 'Snack'
        "Price": 1,  #Key: 'Price' & Value: 1
        "Stock": 2,  #Key: 'Stock' & Value: 2
        "Related item": "3B"  #Key: 'Related item' & Value: '3B'
    },
    "4A" : {  #Another nested dictionary
        "Code": "4A",  #Key: 'Code' & Value: '4A'
        "Item": "Ice tea",  #Key: 'Item' & Value: 'Ice tea'
        "Category": "Drink",  #Key: 'Category' & Value: 'Drink'
        "Price": 2,  #Key: 'Price' & Value: 1
        "Stock": 3,  #Key: 'Stock' & Value: 2
        "Related item": "4B"  #Key: 'Related item' & Value: '4B'
    },
    "2B": {  #Another nested dictionary
        "Code": "2B",  #Key: 'Code' & Value: '2B'
        "Item": "Cookie",  #Key: 'Item' & Value: 'Cookie'
        "Category": "Snack",  #Key: 'Category' & Value: 'Snack'
        "Price": 2,  #Key: 'Price' & Value: 2
        "Stock": 1,  #Key: 'Stock' & Value: 1
        "Related item": "2A"  #Key: 'Related item' & Value: '2A'
    },
    "1B": {  #Another nested dictionary
        "Code": "1B",  #Key: 'Code' & Value: '1B'
        "Item": "Nachos",  #Key: 'Item' & Value: 'Nachos'
        "Category": "Snack",  #Key: 'Category' & Value: 'Snack'
        "Price": 2,  #Key: 'Price' & Value: 2
        "Stock": 2,  #Key: 'Stock' & Value: 2
        "Related item": "1A"  #Key: 'Related item' & Value: '1A'
    },
    "3B": {  #Another nested dictionary
        "Code": "3B",  #Key: 'Code' & Value: '3B'
        "Item": "Hot Espresso",  #Key: 'Item' & Value: 'Hot Espresso'
        "Category": "Drink",  #Key: 'Category' & Value: 'Drink'
        "Price": 4,  #Key: 'Price' & Value: 4
        "Stock": 5,  #Key: 'Stock' & Value: 5
        "Related item": "3A"  #Key: 'Related item' & Value: '3A'
    },
    "4B": {  #Another nested dictionary
        "Code": "4B",  #Key: 'Code' & Value: '3B'
        "Item": "Popcorn",  #Key: 'Item' & Value: 'Popcorn'
        "Category": "Snack",  #Key: 'Category' & Value: 'Snack'
        "Price": 1,  #Key: 'Price' & Value: 4
        "Stock": 5,  #Key: 'Stock' & Value: 5
        "Related item": "4A"  #Key: 'Related item' & Value: '3A'
    }
}
while True:  #Infinite loop until user decides to break
    additional_item = None  #To store an additional item if chosen
    options = input("What do you want to do?\n1-Full list of options\n2-List snacks\n3-List drinks\n(1/2/3): ")  #User input
    if options in ["1", "2", "3"]:  #Error handling if user inputs anything else
        for key, value in VMItems.items():  #Iterate over dictionary items
            if options == '1':  #If user chooses full list
                print(f"Code : {value['Code']} || Item : {value['Item']:<18} || Category : {value['Category']} || Price : {value['Price']} || Stock : {value['Stock']} || Related item : {value['Related item']}")  #Print full list
            elif options == "2" and value["Category"].lower() == "snack":  #If user chooses snacks
                print(f"Code : {value['Code']} || Item : {value['Item']:<17} || Category : {value['Category']} || Price : {value['Price']} || Stock : {value['Stock']} || Related item : {value['Related item']}")  #Print snacks only
            elif options == '3' and value["Category"].lower() == 'drink':  #If user chooses drinks
                print(f"Code : {value['Code']} || Item : {value['Item']:<13} || Category : {value['Category']} || Price : {value['Price']} || Stock : {value['Stock']} || Related item : {value['Related item']}")  #Print drinks only
    else:  #If input is invalid
        print("Wrong! Try again") #prints out error message
        continue #repeats the program
    first_item = input("Enter the code of the desired item: ").upper()  #User enters item code
    if first_item in VMItems:  #Check if item exists in dictionary
        if VMItems[first_item]['Stock'] != 0:  #Check stock availability
            additional_item = VMItems[first_item]["Related item"]  #Get related item
            if VMItems[additional_item]['Stock'] != 0:  #Check stock for related item
                y_n = input(f"Would you like to add {VMItems[additional_item]['Item']}?\n(y/n): ").lower()  #Ask user
                if y_n == 'y':  #If user agrees
                    print(f"{VMItems[first_item]['Item']} & {VMItems[additional_item]['Item']} are added. Total price is $", VMItems[additional_item]['Price'] + VMItems[first_item]['Price'])  #Print total price
                else:  #If user declines
                    additional_item = None  #Reset additional item
                    print(f"{VMItems[first_item]['Item']} is added. Total cost is ${VMItems[first_item]['Price']}")  #Print single item price
            else:  #If related item is out of stock
                additional_item = None  #Reset additional item
                print(f"{VMItems[first_item]['Item']} is added. Total cost is ${VMItems[first_item]['Price']}")  #Print single item price
        else:  #If selected item is out of stock
            print(f"{VMItems[first_item]['Item']} is out of stock") #prints out the message if item is out of stock
            continue
    else:  #If item does not exist
        print("Item is not listed") #prints out the message if item isn't in the list 
        continue
    try:  #Handle user input for payment
        wallet = int(input("Enter the required amount to pay: ")) #input that asks user to pay using numbers
    except ValueError:  #If user enters invalid input
        print("Please use numbers") #prints out the message incase the user uses anything else rather than integers or float
        continue # repeats the program
    if additional_item is None:  #If no additional item
        if VMItems[first_item]['Price'] <= wallet:  #Check if payment is sufficient
            print(f"You got {VMItems[first_item]['Item']} & your change is $", wallet - VMItems[first_item]['Price'])  #Print change
            VMItems[first_item]['Stock'] -= 1  #Reduce stock for the item
        else:  #If payment is insufficient
            print("Not enough money")
            continue #repeats  the program
    else:  #If additional item is selected
        if wallet >= VMItems[first_item]['Price'] + VMItems[additional_item]['Price']:  #Check if payment covers both items
            print(f"You got {VMItems[first_item]['Item']} with {VMItems[additional_item]['Item']} & your change is $", wallet - (VMItems[first_item]['Price'] + VMItems[additional_item]['Price']))  #Print change
            VMItems[first_item]['Stock'], VMItems[additional_item]['Stock'] = VMItems[first_item]['Stock'] - 1, VMItems[additional_item]['Stock'] - 1  #Reduce stock for both items
        else:  #If payment is insufficient
            print("Not enough money")#prints out the message
            continue #repeat
    repeat = input("Wanna repeat? (y/n): ").lower()  #Ask user if they want to repeat
    if repeat == 'y':  #If user chooses to repeat
        continue #repeats the program
    else:  #If user chooses to exit
        print("Thank you and good bye!!") #prints out bye message
        break #exit the loop
