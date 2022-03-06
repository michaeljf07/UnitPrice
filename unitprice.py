"""
For unit price program project.

If you use any of this code please give credit to the creator:
- Michael J. Ferreira
"""

from time import sleep


item1 = int(input("What is the price of the first the item?   $"))
quantity1 = int(input("How much of the item do you have?   "))
item2 = int(input("What is the price of the second the item?   $"))
quantity2 = int(input("How much of the item do you have?   "))
print()

unitprice1 = round(item1 / quantity1, 2)
unitprice2 = round(item2 / quantity2, 2)

print(f"The unit price of the first item is ${unitprice1} while the second item is ${unitprice2}")

# Visuals
for i in range(3):
    sleep(0.2)
    print(".")

if unitprice1 > unitprice2:
    print("The first item is the better deal")

else:
    print("The second item is the better deal")