"""
1.	დაწერეთ პროგრამა რომელიც მიიღებს ნატურალურ რიცხვს n. n > 1. 
პროგრამამ უნდა დაითვალის რიცხვი x და დაბეჭდოს ეკრანზე. Რიცხვი x ის დათვლის პრინციპი ასეთია.
x = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - ... (+/-)1 / (2n-1) )
"""
number = int(input("Please enter integer (n > 1) :"))
if number <=1:
     print("Invalid input")
     exit(1)
x = 0
for i in range (number):
    output = (-1) ** i / (2*i+1)
    x+=output
x = 4 * x
print(x)