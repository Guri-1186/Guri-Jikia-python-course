
"""
3.	დაწერეთ პროგრამა რომელიც მიიღებს ნატურალურ რიცხვს - n, სადაც 0 < n < 50.
Პროგრამამ უნდა დახატოს n სიმაღლის ნაძვის ხე სიმბოლოებით *,  /, | და \ .
Მაგალითად n = 4
"""
height = int(input("Please enter positive integer: "))


if height < 0 or height >= 50:
    print("Invalid Number")
    exit(1)

i = 0
while i < height:
    if i == 0:
        print(" " * (height - 1) + "*")
    elif i ==1:
        print(" " * (height -2) + "/|\\")
    else:
        slashes = "/" * i
        back_slashes = "\\" * i
        v_bar = "|"
        print(" " * (height - i - 1) + slashes + v_bar + back_slashes)


    i+=1
print( " " * (height - 1) + v_bar)
   
    
