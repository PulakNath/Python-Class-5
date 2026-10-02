x = int(input("Enter your number: "))
if x > 0:
    print("x is a positive number.")
elif x == 0:
    print("x is 0.")
else:
    print("x is negative.")
a = float(input("Enter the cost of your item: "))
b = float(input("Enter the selling price of your item: "))
if b > a:
    Profit = b - a
    print("Profit = {0}".format(Profit))
else:
    print("No profit")
q = int(input("Enter your quantity: "))
if q > 100:
    print("I'm in the if block")
else:
    print("I'm in the else block")
print("This is outside the if-else block")
e = int(input("Enter your number: "))
if e%2 == 0:
    print("e is an even number.")
else:
    print("e is an odd number.")