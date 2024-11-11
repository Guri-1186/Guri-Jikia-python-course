"""
დაწერეთ ფუნქცია რომელსაც შეეძლება ცელსიუსის ფარენჰეიტებში გადაყვანა და პირიქით.
C = (F - 32) * 5/9 , F = C * 9/5 + 32. 
Main ფუნქციაში დაუწერეთ რამდენიმე მაგალითი თქვენს მიერ შექმნილი 
ფუნქციის გამართულად მუშაობის სადემონსტარაციოდ
"""
# ## SOLUTION - 1
def temperature_converter(temp, unit):
    if unit == "C":
        return temp * 9/5 + 32
    elif unit == "F":
        return (temp - 32) * 5/9
    else:
        print("Invalid input")

def main():
    print(temperature_converter(12, "C"))
    print(temperature_converter(50, "F"))
if __name__ == "__main__":
    main()

## SOLUTION - 2
user_input_unit = input("Which unit would you like get/ type 'C' or 'F':").lower()
user_input_temp = float(input("What is the temperature value? "))
def temperature_converter(temp, unit):
    if unit == "c":
        return temp * 9/5 + 32
    elif unit == "f":
        return (temp - 32) * 5/9
    else:
        print("Invalid input")
   

def main():
    print(temperature_converter(user_input_temp,user_input_unit))
    
if __name__ == "__main__":
    main()