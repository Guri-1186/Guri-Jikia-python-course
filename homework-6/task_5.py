"""
დაწერეთ პროგრამა რომელიც მიიღებს მთელ რიცხვს - n, სადაც 0 < n < 10.  
Პროგრამამ უნდა დაბეჭდოს სურათზე მოცემული სტრუქტურა.


"""
num = int(input("Please enter  integer less than 10 :"))

if num < 0 or num > 10:
    print("Invalid input")
    exit(1)
       
i = 0
while i <= num:
    space = num - i
    while space > 0:
        print(" ", end = " ") 
        space -= 1
        
    j=i
    while j >= 0:
        print(j, end = " ")
        j -= 1
        
    k=1
    while k <= i:
        print(k, end=" ")
        k += 1
    print()
    i += 1
    