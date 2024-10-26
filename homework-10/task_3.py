"""
3. Დაწერეთ ფუნქცია რომელიც დაითვლის რიცხვის ფაქტორიალს. 
"""

def factorial(num):
    output = 1
    i = 1
    while i <= num:
        output*=i
        i+=1
    return output

print(factorial(5))
print(factorial(10))      