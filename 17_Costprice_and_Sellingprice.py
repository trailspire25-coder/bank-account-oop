# Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit 
 
costprice = int(input("Enter Cost Price: GHc "))
sellingprice = int(input("Enter Selling Price: GHc "))

profit = sellingprice - costprice
loss = costprice - sellingprice

if costprice > sellingprice:
    print(f"You made a Loss of GHc{loss}.00")

elif sellingprice > costprice:
    print(f"You made a Profit of GHc{profit}.00")

else:
    print("There was no Profit or Loss made.")