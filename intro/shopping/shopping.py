"""Examples
Example 1:

Enter price: 12.50
Enter quantity: 3
37.50
Example 2:

Enter price: 8.99
Enter quantity: 2
17.98
Example 3:

Enter price: 15.00
Enter quantity: 4
60.00"""

price = float(input("Enter price: "))
quantity = float(input("Quantity:"))

result = price * quantity
print(f"{result:.2f}")