"""
დაწერეთ პროგრამა რომელიც მიიღებს მთელ რიცხვს - n, სადაც 0 < n < 10.  
Პროგრამამ უნდა დაბეჭდოს სურათზე მოცემული სტრუქტურა.
"""
num = int(input("Please enter integer less than 10 :"))

if num < 0 or num > 10:
    print("Invalid input")
    exit(1)

  
i = 1
increasing = True

while i > 0:
    j = 1
    while j <= i:
        print(j, end='')
        j += 1
    print()
    
    if i == num:
        increasing=False
    if increasing:
        i+=1
    else:
        i-=1