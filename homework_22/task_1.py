"""
1)შექმენით კლასი Inset, რომელსაც ექნება კონსტრუქტორი +
2) კონსტრუქტორში უნდა შეიქმნას ცარიელი სია +
3)შექმენით მეთოდი insert, რომელიც +
სიაში ჩაამატებს გადაცემულ ელემენტს. 
4) insert მეთოდით უნდა დაემატოს მხოლოდ უნიკალური ელემენტები. +
5)შექმენით მეთოდი member რომელიც იღებს ერთ არგუმენტს ამოწმებს არის თუ არა მსგავსი 
ელემენტი ლისტში თუ არის აბრუნებს True თუ არ არის აბრუნებს False. +
6)მას აქვს მეთოდი remove რომელიც იღებს ერთ არგუმენტს და ცდილობს მის წაშლას სიიდან,
თუ ასეთი ელემენტი არ აღმოჩნდება სიაში უნდა გამოიტყორცნოს ValueError შეტყობინებით 
"ვერ ვიპოვნე" 
7) კლასს უნდა ჰქონდეს __str__ რომელიც ჯერ დაალაგებს სიას ზრდადობით 
და მერე დააბრუნებს მის ელემენტებს სტრიქონად.
"""
class Inset:
    def __init__(self):
        self.data = []
    def __str__(self):
        sorted_list = sorted(self.data)
        return ' '.join(map(str,sorted_list))
    
    def insert(self,element):
        if element not in self.data:
           self.data.append(element)
    
    def member(self,element):
        if element in self.data:
            return True
        else:
            return False
    def remove (self,element):
        if element in self.data:
            self.data.remove(element)
        else:
            raise ValueError ("Can't find element")
    
            
output = Inset()
output.insert(1)     
output.insert(2)
output.insert(1)
output.insert(3)
print(output)

print(output.member(2))
print(output.member(6))

output.remove(2)
print(output)