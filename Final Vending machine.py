VMItems = { 
	"1A" : {
		"Code" : "1A",
		"Item": "Soda", 
		"Category": "Drink",
		"Price" : 4, 
		"Stock" : 3,
		"Related item" : '1B'
	},
	"2A" : {
		"Code" : "2B",
		"Item" : "Milk",
		"Category" : "Drink",
		"Price" : 4,
		"Stock" : 5,
		"Related item" : '2B'
	},

	"3A" : {
		"Code" : "3A",
		"Item" : "Chocolate Brownie",
		"Category": "Snack",
		"Price" : 1,
		"Stock": 2,
		"Related item" : '3B'
	},
	"2B" : {
		"Code" : "2B",
		"Item" : "Cookie",
		"Category" : "Snack",
		"Price" : 2,
		"Stock" : 1,
		"Related item" : '2A'
	},
	"1B" : {
		"Code" : "1B",
		"Item" : "Nachos",
		"Category" : "Snack",
		"Price" : 2,
		"Stock" : 2,
		"Related item" : '1A'
	},
	"3B" : {
		"Code" : "3B",
		"Item" : "Hot espresso",
		"Category" : "Drink",
		"Price" : 4,
		"Stock" : 5,
		"Related item" : '3A'
	}
}
while True:
	additional_item = None
	options = input("What do you want to do?\n1-Full list of options\n2-List snacks\n3-List drinks\n(1/2/3): ")#user input that always will 
	if options in ["1","2", "3"]:#Error handeling if user inputs anything else than options available
		for key,value in VMItems.items():#for loop
			if options == '1':#if user inputs 1
				print(f"Code : {value['Code']} || Item : {value['Item']:<18} || Category : {value['Category']} || Price : {value['Price']} || Stock : {value['Stock']} || Related item : {value['Related item']}")#it will print out full list

			elif options  == "2" and value["Category"].lower() == "snack":
				print(f"Code : {value['Code']} || Item : {value['Item']:<17} || Category : {value['Category']} || Price : {value['Price']} || Stock : {value['Stock']} || Related item : {value['Related item']}")#will print out snacks only

			elif options == '3' and value["Category"].lower() == 'drink':
				print(f"Code : {value['Code']} || Item : {value['Item']:<13} || Category : {value['Category']} || Price : {value['Price']} || Stock : {value['Stock']} || Related item : {value['Related item']}")#will print out drinks only
	else:#dont touch
		print("wrong! try again")#dont touch
	fisrt_item = input("Enter the code of desired item: ").upper()
	if fisrt_item in VMItems:
		if VMItems[fisrt_item]['Stock'] != 0:
			additional_item  = VMItems[fisrt_item]["Related item"]
			if VMItems[additional_item]['Stock'] != 0:
				y_n= input(F"Would you like to add {VMItems[additional_item]['Item']}?\n(y/n): ").lower()
				if y_n == 'y':
					print(f"{VMItems[fisrt_item]['Item']} & {VMItems[additional_item]['Item']} is added, total price is $",VMItems[additional_item]['Price'] + VMItems[fisrt_item]['Price'])
				else:
					additional_item = None
					print(f"{VMItems[fisrt_item]['Item']} is added, total cost is ${VMItems[fisrt_item]['Price']}")
			else:
				additional_item = None
				print(f"{VMItems[fisrt_item]['Item']} is added, total cost is ${VMItems[fisrt_item]['Price']}")			
		else:
			print(f"{VMItems[fisrt_item]['Item']} is out of stock")
			continue
	else:
		print("item is not listed")
		continue
	try:
		wallet = int(input("Enter the required amount to pay:"))
	except ValueError:
		print("use numbers")
		continue
	if additional_item == None:
		if VMItems[fisrt_item]['Price'] < wallet:
			print(f"You got {VMItems[fisrt_item]['Item']} & your change is $", wallet - VMItems[fisrt_item]['Price'])
			VMItems[fisrt_item]['Stock'] -= 1
		else:
			print("Not enough money")
			continue 
	else:
		if wallet >= VMItems[fisrt_item]['Price'] + VMItems[additional_item]['Price']:
			print(f"You got {VMItems[fisrt_item]['Item']} with {VMItems[additional_item]["Item"]} & your change is $", wallet - (VMItems[fisrt_item]['Price'] + VMItems[additional_item]['Price']))
			VMItems[fisrt_item]['Stock'], VMItems[additional_item]['Stock'] = VMItems[fisrt_item]['Stock'] - 1, VMItems[additional_item]['Stock'] - 1
	repeat = input("wanna repeat?(y/n): ").lower()
	if repeat == 'y':
		continue
	else:
		break
