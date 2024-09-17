from math import pow

"""
task.1 დაწერეთ პროგრამა რომელიც მიიღებს ორ რიცხვს (x,y) და დაბეჭდავს რიცხვს რომელიც მიიღება x-ის y ხარისხში აყვანით. 
იხ module math
"""
num_base = int(input("Please enter base (x) : "))
num_exponent = int(input("Please enter exponent (y): "))

result = round(pow(num_base,num_exponent ))
print(f" The {num_base} to the power of {num_exponent} is {result}")