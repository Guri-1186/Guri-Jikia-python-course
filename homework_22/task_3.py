"""
შექმენით Stack მონაცემთა სტრუქტურა Python-ში, რომელიც მოიცავს შემდეგ მეთოდებს:
1. push(element) - ელემენტის დამატება Stack-ის თავზე. 
2. pop() - Stack-ის ზედა ელემენტის წაშლა და დაბრუნება. 
3. peek() - Stack-ის ზედა ელემენტის დაბრუნება წაშლის გარეშე. 
4. is_empty() - ამოწმებს, არის თუ არა Stack ცარიელი. 
5. size() - აბრუნებს Stack-ში არსებული ელემენტების რაოდენობას.
"""

class Stack:
    def __init__(self):
        self.data = []
    
    def push(self,element):
        self.data.append(element)
        
    def pop(self):
        return self.data.pop()
    def peek(self):
        return self.data[-1]
    def is_empty(self):
        return len(self.data) == 0 
    def size(self):
        return len(self.data)
        
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)


print(stack.size()) 
print(stack.peek())
print(stack.pop())  
print(stack.is_empty()) 
print(stack.size())  

stack.pop()
stack.pop()

print(stack.is_empty())
