# Edit
a = "How many miles per gallon does your car get? "
b = "What is the current price of gas, per gallon? (Please use a decimal, like this: 2.85) "
c = "What is the length of your trip, in miles? "

def cost_of_gas (mpg, price_of_gas, distance):
    cost = (distance / mpg) * price_of_gas
    print "The cost of gas is $%d" % cost

mpg = float (raw_input(a))
price_of_gas = float(raw_input(b))
distance = float(raw_input(c))

cost_of_gas (mpg, price_of_gas, distance)