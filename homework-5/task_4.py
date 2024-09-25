
"""
3.	დაწერეთ პროგრამა რომელიც მიიღებს ნატურალურ რიცხვს - n, სადაც 0 < n < 50.
Პროგრამამ უნდა დახატოს n სიმაღლის ნაძვის ხე სიმბოლოებით *,  /, | და \ .
Მაგალითად n = 4
"""
height = int(input("Please enter positive integer: "))

if height < 0 or height >= 50:
    print("Invalid Number")

