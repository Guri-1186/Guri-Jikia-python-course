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
    print(GCD(48, 18)) #6
    print(GCD_rec(48, 18)) #6
    
if __name__ == '__main__':
    main()