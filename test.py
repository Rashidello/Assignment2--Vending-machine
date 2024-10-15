
def dic():
	item = { 
		933 : {
			"Code" : 933,
			"Item": "Soda", 
			"Category": "drink",
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
			"Price" : 1.5,
			"Stock": 2
		}
	}
	
	print("Welcome hren")
	for keys,values in item[311].items():
		print(f"Code: {values['Code']}, Item: {values['Item']}, Category: {values['Category']},Price: {values['Price']}, Stock: {values['Stock']}")

	userchoice = int(input("please enter the code of an item"))
	if userchoice in dic():
		print(f"yo 3433e3e{dic[userchoice]}")




dic()
