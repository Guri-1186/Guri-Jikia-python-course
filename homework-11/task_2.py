"""
დაწერეთ პროგრამა რომელიც მიიღებს ორ ნატურალურ რიცხვს a და b,
სადაც 0 < a,b < 10000 და ეკრანზე გამოიტანს ამ ორი რიცხვის უდიდეს საერთო გამყოფს.
გადაჭერით ეს პრობლემა როგორც იტერაციული ისე რეკურსიული მეთოდით. Მაგალითი 1:
Enter a: 1000 Enter b: 400 GCD of 1000 and 400 is 200.
"""
  
def GCD(a,b):
    if a <= 0 or a > 10000 or b <= 0 or b > 10000:
        print("Invalid Input")
        exit(1)
    while b != 0:
        result = a % b
        a,b = b,result
    return a
 
def GCD_rec(a,b):
    if b == 0:
        return a
    else:
       return  GCD_rec(b, a%b)
            
def main():
    a = int(input("Enter first number : "))
    b = int(input("Enter second number :"))
    output = (GCD(a,b))
    print(f"GCD of {a} and {b} is {output}")
   
    output = (GCD_rec(a,b))
    print(f"GCD_rec of {a} and {b} is {output}")
    
if __name__ == '__main__':
    main()