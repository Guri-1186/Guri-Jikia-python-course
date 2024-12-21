"""
3. შექმენით კლასი Student, რომელიც ინახავს სტუდენტის ქულებს და უზრუნველყოფს 
ენკაფსულაციის პრინციპს:
• protected ველები:
• _name (სტუდენტის სახელი)
• _scores (ქულების სია)
კლასს უნდა ჰქონდეს შემდეგი მეთოდები:
1. კონსტრუქტორი, რომელიც იღებს სტუდენტის სახელს და ინიციალიზაციას უკეთებს
ცარიელ ქულების სიას.
2. მეთოდი add_score(score), რომელიც ამატებს ქულას სიის ბოლოში.
თუ ქულა არ არის [0-დან 100-მდე] ინტერვალში, უნდა დაბეჭდოს შეტყობინება: 
“არასწორი ქულა”.
3. მეთოდი get_average(), რომელიც აბრუნებს ქულების საშუალო მნიშვნელობას.
4. მეთოდი get_scores(), რომელიც აბრუნებს ქულების სიას.

დავალება:
1. შექმენით სტუდენტების სია, დაამატეთ მათ ქულები და გამოთვალეთ თითოეული 
სტუდენტის ქულების საშუალო.
2. დაამატეთ ახალი სტუდენტი და დარწმუნდით, რომ ენკაფსულაციის პრინციპი დაცულია.
"""

class Student:
    def __init__ (self, name):
        self.name = name
        self.scores = []
        
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
        
    @property
    def scores (self):
        return self._scores
    @scores.setter
    def scores(self,value):
        self._scores = value
    
    def add_score(self,score):
        if 0 < score <= 100:
            self._scores.append(score)
        else:
            print("wrong score")
    
    def get_average(self):
        if self._scores:
          return sum(self._scores)/len(self._scores)
        else:
            return 0
    
    def get_scores(self):
        return self._scores
            
    
def main():
    student1 = Student("zuzu")
    student1.add_score(85)
    student1.add_score(90)
    student1.add_score(101)
    
    student2 = Student("erekle")
    student2.add_score(80)
    student2.add_score(100)
    
    student3 = Student("kravai")
    student3.add_score(50)
    student3.add_score(90)
    
    students = [student1,student2,student3]
    for student in students:
      print(f"Student: {student.name}")
      print(f"Scores: {student.get_scores()}")
      print(f"Average Score: {round(student.get_average())}")
      print("-" * 30)
      
if __name__ == "__main__":
    main()