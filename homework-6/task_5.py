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
    j = 0
    while j <= i:
        print(j, end = " ")
        j+=1
    i+=1
    print()
    
    
    