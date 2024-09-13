"""
task.3 Დაწერეთ პროგრამა რომელიც მიიღებს მთელ რიცხვს. 
Პროგრამამ უნდა დაბეჭდოს ყველა მარტივი გამყოფი ერთ ხაზზე. 
Შემოსული რიცხვის მაქსიმალური მნიშვნელობა უნდა იყოს 10. 

Მაგალითი: თუ პროგრამას გადავეცით 6, გამოსავალზე უნდა დაიბეჭდოს 2, 3. 
ახსნა: 6 იყოფა 2-ზეც და 3-ზეც. 2 და 3 არის მარტივი რიცხვები.

Დაიცავით პროგრამა ისეთი არგუმენტებისგან, რომლებიც არ არის დასაშვები.
"""
input_number = int(input("please enter number with max value 10 :"))
if input_number > 10 or input_number < 0:
  print("invalid value")
  exit(1)
# prime_divisor = 2,3,5,7

if input_number % 2 == 0:
  print(2, end = ', ')
if input_number % 3 == 0:
  print(3, end = ', ')
if input_number % 5 == 0:
  print(5, end = ', ')
if input_number % 7 == 0:
  print(7, end = ', ')

  


  
  
