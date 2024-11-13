"""
1. Დაწერეთ პროგრამა რომელიც მოცემული 
ტემპერატურების [22, 25, 19, 23, 25, 26, 23] მიხედვით 
გამოითვლის საშუალო ტემპერატურას და დაბეჭდავს ეკრანზე.
"""

def average(temperature:list):
    result = 0
    for temp in temperature:
        result+=round(temp/len(temperature))
    return result

def main():
    print(average([22, 25, 19, 23, 25, 26, 23]))
if __name__ == "__main__":
    main()  