""" 5. Დაწერეთ ფუნქცია რომელსაც გადაეცემა ტექტი და აბრუნებს ამ ტექსტს შებრუნებული მიმდევრობით. Გამოიძახეთ ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტისთვის რომ აჩვენოთ მისი მუშაობა """

def reverse(text):
    result = text[::-1]
    return result

print(reverse("guri"))
print(reverse("this was very simple task:)"))
print(reverse("coding is actualy rocket science :)"))