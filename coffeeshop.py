print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("+                               +")
print("+         The Coffee Shop       +")
print("+              Welcome          +")
print("+                               +")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("")
print("We serve the following coffees:")
print(" > Espresso") 
print(" > Americano") 
print(" > Latte") 
print(" > Cappuccino") 
print(" > Macchiato")
print(" > Mocha")
print(" > Flat White")
print(" > Breakfast Tea")
print("----------------------------")

price = 0
coffee = input("What type of coffee would you like? ").title()

if coffee == "Espresso":
    price = 2.50
elif coffee == "Americano":
    price = 3.00
elif coffee == "Latte":
    price = 2.50
elif coffee == "Cappuccino":
    price = 3.50
elif coffee == "Macchiato":
    price = 4.00
elif coffee == "Mocha":
    price = 6.00
elif coffee == "Flat White":
    price = 5.00
elif coffee == "Breakfast Tea":
    price = 3.00
else:
    print("Sorry, we don’t serve that drink.")
    exit()

print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("+         The sizes we have     +")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("")
print("We have the following sizes:")
print(" > Medium") 
print(" > Large") 
print(" > Extra Large") 
print("----------------------------")

size = input("What size would you like? ").title()
if size == "Medium":
    price += 0
elif size == "Large":
    price += 1.00
elif size == "Extra Large":
    price += 1.50
else:
    print("Sorry we don’t have that size.")
    exit()

print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("+    Drink here or take out?    +")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print(" > Drink Here") 
print(" > Take Out") 
print("----------------------------")

option = input("Would you like to drink here or take out? ").title()
if option == "Drink Here":
    price += 0
elif option == "Take Out":
    price += 1.00
else:
    print("Invalid option.")
    exit()

# Ask for quantity
quantity = int(input("How many cups? "))
total_price = price * quantity

print("----------------------------")
print("Total Cost: €" + str(round(total_price, 2)))
print("Thank you for visiting The Coffee Shop!")
