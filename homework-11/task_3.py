from task_2 import GCD

"""
დაწერეთ პროგრამა რომელიც მიიღებს ორ ნატურალურ რიცხვს a და b, 
სადაც 0 < a,b < 10000 და ეკრანზე გამოიტანს ამ ორი რიცხვის უმცირეს საერთო ჯერადს. 
Მინიშნება lcm(a, b) = (a * b) / gcd(a, b).
დააიმპორტეთ და გამოიყენეთ უდიდესი საერთო გამყოფის დათვლის ფუნქციონალი 
პირველი დავალების ფაილიდან
"""

def lcm(a, b):
    if a <=0 or a > 10000 or b <= 0 or b > 10000:
        print("Invalid Input")
        exit(1)
    result = (a * b) / GCD(a, b)
    return round(result)
        
        
def main():
    a = int(input("Enter first number : "))
    b = int(input("Enter second number :"))
    output = (lcm(a, b))
    print(f"LCM of {a} and {b} is {output}")
    
if __name__ == "__main__":
    main()