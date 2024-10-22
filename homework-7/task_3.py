"""
3.	პროგრამამ შეგვაყვანინოს სიტყვა და დაბეჭდოს ბოლო, 
პირველი და შუა ასოები 5-ჯერ while ლუპით. თუ შემოყვანილი ტექსტის ზომა არის ლუწი, 
მაშინ პროგრამამ უნდა დაბეჭდოს 
შუა ორი სიმბოლო.
"""

while True:
    word = input("Please enter word :")
    if word.replace(" ", ""). isalpha():
        break
    else:
         print("Please enter string")
   
i = 0
while i < 5: 
    length = int(len(word))
    middle_el = int(length/2)
    if length % 2 == 0:
        print(word[middle_el-1:middle_el+1])
    else:
        print(word[-1], word[middle_el], word[0])
    
    i+=1