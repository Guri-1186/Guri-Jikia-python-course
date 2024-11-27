"""
3. Დაწერეთ გენერატორი რომელიც აბრუნებს n ცალ წევრს ფიბონაჩის მმიმდევრობიდან. 
Აჩვენეთ გენერატორის მუშაობა რამდენიმე მაგალითზე
"""

def fibonnacci(num):
    a, b = 0, 1
    for _ in range(num):
        yield a
        a, b = b, a + b

def main ():
   value = fibonnacci(6)
   print(next(value))
   print(next(value))
   print(next(value))
   print(next(value))
   print(next(value))
   print(next(value))
   
   
if __name__ == '__main__':
    main()
    