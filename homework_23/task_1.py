"""
1. შექმენით კლასი Person, რომელსაც ექნება შემდეგი protected ველები:
• _name (სახელი)
• _age (ასაკი)
კლასს უნდა ჰქონდეს მეთოდები:
1. კონსტრუქტორი, რომელიც იღებს სახელს და ასაკს და ინახავს მათ protected ველებში.
2. მეთოდი get_info(), რომელიც აბრუნებს სახელს და ასაკს როგორც სტრინგს.
დავალება:
შექმენით რამდენიმე ობიექტი კლასიდან Person, და დაბეჭდეთ მათი ინფორმაცი
"""
class Person:
    def __init__ (self,name,age):
        self.name = name
        self.age = age
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name (self,value):
        self._name = value
        
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        self._age = value
        
    def get_info(self):
        return f"{self._name} is {self._age} years old"
    
def main():
    p1 = Person("Luk", 30)
    p2 = Person("Zuzu",20)
    print(p1.get_info())
    print(p2.get_info())
    
if __name__ == "__main__":
    main()
    