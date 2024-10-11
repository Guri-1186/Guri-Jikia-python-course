"""
1.	დაწერეთ პროგრამა რომელიც დაბეჭდავს გამრავლების ტაბულას 1 და 9 ის ჩათვლით. 
ტაბულა უნდა იყოს სვეტებად შედგენილი. ყოველ მომდევნო სვეტში არ უნდა იყოს გამეორებული
ნამრავლი წინა სვეტიდან.

"""
num = 1
while num <= 9:
    multiplier =1
    while multiplier <= 9:
        if num >= multiplier:
           value = num * multiplier
           print(f"{num} * {multiplier} = {value}", end = "\t")
        multiplier += 1
    num += 1    
    print()

    
    