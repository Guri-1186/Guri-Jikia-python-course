"""
4.	*დაწერეთ პროგრამა რომელიც მომხმარებლის შემოყვანილ ტექსტს 
დაშიფრავს ან განშიფრავს და დაბეჭდავს ეკრანზე. 

1)Ნებისმიერი სიმბოლო რომელიც არ მიეკუთვნება a-z დატოვეთ უცვლელი.

2)დაშიფვრის ლოგიკა ასეთია, ყოველი სიმბოლო(a-z) უნდა შეიცვალოს 
კლავიატურაზე მის მარჯვნივ მდგომი სიმბოლოთი. 

3)Თუ სიმბოლოს მარჯვნივ კლავიატურაზე ინგლისური სიმბოლო არ არის, 
მაშინ უნდა გადავიდეს პირველ სიმბოლოში ამ სტრიქონიდან.
Მაგალითად: p -> q, l -> a და ა.შ.

4) პროგრამამ უნდა გარდაქმნას მხოლოდ დაბალი რეგისტრის ინგლისური სიმბოლოები a-z. 
"""
direction = input("Type 'encode' or 'decode' : ").lower()
text = input("Type your message: ").lower()
keyboard_layout = 'qwertyuiopasdfghjklzxcvbnm'

output_text = " "
for letter in text:
    if letter not in keyboard_layout:
        output_text+=letter
    else:
        if direction == "encode":
          shifted_postion = keyboard_layout.index(letter)+1
          shifted_postion%=len(keyboard_layout)
          output_text+=keyboard_layout[shifted_postion]
        else:
          shifted_postion = keyboard_layout.index(letter)-1
          shifted_postion%=len(keyboard_layout)
          output_text+=keyboard_layout[shifted_postion]
            
print(output_text)
        
    
    

















# output_text =""
# for letter in text:
#     if letter not in keyboard_layout:
#        output_text+=letter
#     else:
#         shifted_position = keyboard_layout.index(letter) +1
#         shifted_position %=len(keyboard_layout)
#         print(shifted_position)
#         output_text+=keyboard_layout[shifted_position]
   
# print(output_text)















