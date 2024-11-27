
"""
დაწერეთ პროგრამა რომელიც წაიკითხავს data.txt ფაილს. 
data.txt ფაილში მოცემულია პროდუქციის შესყიდვის მონაცემები. 
Მონაცემები ერთმანეთისგან გამოყოფილია მძიმით. 

Მონაცემების მიმდევრობა შემდეგია user_name,product_name,amount,price - 
სადაც price არის ერთეული პროდუქციის ღირებულება. 

Პროგრამამ უნდა გააკეთოს ორი ახალი ფაილი small.txt და high.txt. 
Პროგრამა small.txt ფაილში უნდა გადაწეროს ის შესყიდვები რომელთა ღირებულება 
ნაკლებია 10-ზე, ხოლო ყველა სხვა დანარჩენი high.txt ფაილში.
"""
with open ("homework_18/my_dir/data.txt", "r") as file:
    content = file.readlines()
    print(content)
      
with open("homework_18/my_dir/small.txt", "w") as small_file, \
     open("homework_18/my_dir/high.txt", "w") as high_file:
    for data in content:
        user_name, product_name, amount, price = data.strip().split(",")
        amount = int(amount)
        price = float(price)
        total_price = amount *price
        
        if total_price < 10:
            small_file.write(data)
        else:
            high_file.write(data)
            