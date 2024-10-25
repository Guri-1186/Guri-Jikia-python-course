
"""
4. Დაწერეთ ფუნქცია, რომელიც დაადგენს გადაცემული რიცხვი მარტივია თუ არა. Გამოიძახეთ ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტისთვის რომ აჩვენოთ მისი მუშაობა
"""

def is_prime(num):
    if num <=1:
        return False
    for i in range(2, num - 1):
        if num % i == 0:
            return False     
        else:
            return True
    
print(is_prime(7))
print(is_prime(8))
print(is_prime(4))
print(is_prime(11))

    
    
    