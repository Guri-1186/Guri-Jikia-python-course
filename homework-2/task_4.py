"""
Დაწერეთ პროგრამა რომელიც არგუმენტად მიიღებს მანქანის სიჩქარეს,
განსაზღვრავს მისი სიჩქარის კატეგორიას და დაბეჭდავს ეკრანზე. 
Სიჩქარისკატეგორიები განისაზღვრება შემდეგნაირად. 
Თუ ავტომობილის სიჩქარე 30 კმ/სთ-ზე ნაკლებია; 
მისი კატეგორიაა - SLOW. 
Როცა ავტომობილის სიჩქარე 120 კმ/სთ-ზემეტია;
მისი კატეგორიაა - VERY FAST.
Თუ ავტომობილის სიჩქარე მეტია 60 კმ/სთ-ზე,მისი კატეგორიაა - FAST.
Ხოლო თუ ავტომობილის სიჩქარე მეტია 30 კმ/სთ-ზე, მისიკატეგორიაა - MODERATE.
(თუ ავტომობლი ხვდება ორ კატეგორაიში, უნდა შეირჩეს უფრო სწრაფი კატეგორია)
"""
#Solution 1
car_speed = int(input("Please enter the car speed (in km/h) :"))

if car_speed > 120:
  print("Your car is VERY FAST")
elif car_speed > 60 and car_speed <= 120:
  print("Your car is FAST")
elif car_speed > 30 and car_speed <= 60:
    print("Your car is MODERATE")
else:
  print("Your car is SLOW ")

#Solution 1
if car_speed > 120:
  print("Your car is VERY FAST")
elif car_speed > 60:
   print("Your car is FAST")
elif car_speed > 30:
  print("Your car is MODERATE")
else:
  print("Your car is SLOW ")
  
  
