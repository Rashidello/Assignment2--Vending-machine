

	
def dic():
	global item
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

	userchoice = int(input("choose an item using their code "))
	if userchoice in item:
		print(f"you have choose {item[userchoice]['Item'.capitalize()]}, it will cost {item[userchoice]['Price'] }AED")
		recommendations()
	else:
		print("it's not there:<")
def recommendations():
	print("works")

def start():
	print("Welcome hren")
	for keys,values in item.items():
		print(f"Code: {values['Code']}, Item: {values['Item']}, Category: {values['Category']}, Price: {values['Price']}, Stock: {values['Stock']}")
	fchoice = int(input("\nUser's options:\n1.Cancel\n2.Choose category:snack\n3.Choose category:drinks\n4.Choose an item\n(1-4)\n"))
	if fchoice == 1:
		exit()
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

dic()
