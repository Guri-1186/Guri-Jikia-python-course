"""
2. Შექმენით კლასი Queue. Ეს უნდა იყოს მონაცემთა სტრუქტურა Stack ის მსგავსი.
Პირველი ჩამატებული ელემენტი უნდა დაბრუნდეს პირველი. 
Ამ პრინციპის სახელწოდებაა FIFO(First in First Out) q = Queue() q.insert(1) 
q.insert(2) q.insert(3) print(q.pop()) # must return 1
"""

class Queue:
    def __init__(self):
        self.data = []
    def insert(self,element):
        self.data.append(element)
    def pop(self):
        return self.data.pop(0)
        
    

q = Queue() 
q.insert(1) 
q.insert(2) 
q.insert(3) 
print(q.pop())