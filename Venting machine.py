#dictionary for venting machine 
def dic():
	global item,additem
	additem = 0
	item = { 
		933 : {
			"Code" : 933,
			"Item": "Soda", 
			"Category": "Drink",
			"Price" : 4, 
			"Stock" : 3 
		},
		209 : {
			"Code" : 209,
			"Item" : "Milk",
			"Category" : "Drink",
			"Price" : 4,
			"Stock" : 5
		},

		311 : {
			"Code" : 311,
			"Item" : "Mentos",
			"Category": "Snack",
			"Price" : 1,
			"Stock": 2
		},
		878 : {
			"Code" : 878,
			"Item" : "Cookie",
			"Category" : "Snack",
			"Price" : 2,
			"Stock" : 1,
		},
		767 : {
			"Code" : 767,
			"Item" : "Chips",
			"Category" : "Snack",
			"Price" : 2,
			"Stock" : 0,
		},
		343 : {
			"Code" : 343,
			"Item" : "Ice tea",
			"Category" : "Drink",
			"Price" : 4,
			"Stock" : 5
		}
	}
	start()


def userinput():
	global userchoice
	userchoice = int(input("Choose an item using their code "))

	#checks if item in the vending machine is present
	if userchoice in item:
		#checks stock of userchoice
		if item[userchoice]["Stock"] == 0:
			print("sorry, we're out of chips, please try again\n")
			userinput()
			#343 doesn't have any additional snacks 
		elif userchoice == 343:
			print(f"You have chosen {item[userchoice]['Item']}, it will cost {item[userchoice]['Price'] } AED")
			payment()		
		else:
			print(f"You have chosen {item[userchoice]['Item']}, it will cost {item[userchoice]['Price'] } AED")
			recommendations()
	else:
		print("It's not there:<")
		start()



def recommendations():
	#classic
	if userchoice == 933:
		additem = input("Would you like to have some Mentos?(y/n): ")
		if additem == 'y':
			additem = 311
			#cancels additional item if it's stock equals to 0
			if item[additem]["Stock"] == 0:
				print(f"Sorry we're out of {item[additem]['Item']}")
				additem = 0
			payment()
		else:
			additem = 0 	
			payment()
	#classic v2
	elif userchoice == 311:
		additem = input("Would you like to have some Soda?(y/n): ")
		if additem == 'y':
			additem = 933
			if item[additem]["Stock"] == 0:
				print(f"Sorry we're out of {item[additem]['Item']}")
				additem = 0
			payment()
		else:
			additem = 0
			payment()
	elif userchoice == 209:
		additem = input("Would you like to have some Cookie?(y/n): ")
		if additem == 'y':
			additem = 878
			if item[additem]["Stock"] == 0:
				print(f"Sorry we're out of {item[additem]['Item']}")
				additem = 0
			payment()
		else:
			additem = 0
			payment()
	elif userchoice == 878:
		additem = input("Would you like to have some Milk?(y/n): ")
		if additem == 'y':
			additem = 209
			if item[additem]["Stock"] == 0:
				print(f"Sorry we're out of {item[additem]['Item']}")
				additem = 0
			payment()
		else:
			additem = 0
			payment()
			
	else:
		#2:52am
		print("You broke the system!")


#fucntion where payment is going
def payment():
	#global variable
	global additem
	#to check whether we have two items for total amount to pay
	if additem > 0:
		totalamount = item[userchoice]["Price"] + item[additem]['Price']

	else:
		totalamount = item[userchoice]["Price"] 

	userwallet = int(input(f"pay {totalamount}AED "))
	#checks if user gave correct amount of money
	if userwallet < totalamount:
		print("Pay the required amount")
		payment()
	userwallet = userwallet - totalamount
	#shows items bought by user and user's change
	if additem > 0:
		print(f"You got {item[userchoice]['Item']} and {item[additem]['Item']}\nYour change is {userwallet}")
	else:
		print(f"You got {item[userchoice]['Item']}\nYour change is {userwallet}")

	#Stock substraction
	item[userchoice]["Stock"] -= 1
	if additem > 0:
		item[additem]["Stock"] -= 1
	#repeat if user wants
	repeat = input("Wanna buy something again?(y/n) ")
	if repeat == 'y':
		#updating value in variable "additem" because additional item would be saved even if u have chosen one item
		additem = 0

		start()
	else:
		exit()



#start of an code
def start():
	print("Welcome! here's some stuff that we have:>\n")
	#prints items using for loop
	for keys,values in item.items():
		print(f"Code: {values['Code']}, Item: {values['Item']}, Category: {values['Category']}, Price: {values['Price']}, Stock: {values['Stock']}")
	#users options with numbers
	fchoice = int(input("\nUser's options:\n1.Cancel\n2.Choose category:snack\n3.Choose category:drinks\n4.Choose an item\n(1-4)\n"))
	if fchoice == 1:
		print("Bye bye!")
		exit()
	#option 2 & 3 are using for loop to show spesicic category and have function for user's input
	elif fchoice == 2:
		print("")
		for keys, values in item[767].items():
			print(f"{keys} : {values}")
		print("")
		for keys, values in item[311].items():
			print(f"{keys} : {values}")
		print("")
		for keys, values in item[878].items():
			print(f"{keys} : {values}")
		print("")
		for keys, values in item[311].items():
			print(f"{keys} : {values}")
		userinput()
	elif fchoice == 3:
		print("")
		for keys,values in item[343].items():
			print(f"{keys} : {values}")
		print("")	
			
		for keys, values in item[933].items():
			print(f"{keys} : {values}")
		print("")
		for keys, values in item[311].items():
			print(f"{keys} : {values}")
	
		userinput()
	elif fchoice == 4:
		userinput()
	#restarts program incase user writes any other nomber except 1-4
	else:
		print("Wrong!\nTry again!!")
		start()

dic()
