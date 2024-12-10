"""
გააფართოვეთ სტანდარტულ ბიბლიოთეკაში არსებული მონაცემთა სტრუქტურა list. 
დაამატეთ მას ორი მეთოდი min და max, რომლებიც დააბრუნებენ მინიმალურ და 
მაქსიმალურ მნიშნელობას შესაბამისად. 

შექმენით კლასის რამდენიმე ობიექტი და აჩვენეთ
რომ მოთხოვნილი ფუნქციონალი გამართულად მუშაობს. 
გამოიყენეთ მემკვიდრეობა.
"""

class List(list):
    def __init__(self, *args):
        super().__init__(args)
    def max_value(self):
        return max(self)
    def min_value(self):
        return min(self)
    
output = List(2,5,9,7,4)

print("Max value:", output.max_value())  
print("Min value:", output.min_value())  
