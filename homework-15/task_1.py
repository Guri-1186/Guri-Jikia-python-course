from random import randint
"""
1. Დააგენერირეთ 100 ცალი შემთხვევითი რიცხვი. 
გააკეთეთ ლექსიკონი ორი გასაღებით even და odd, 

მათი მნიშნველობა უნდა იყოს ლუწი და კენტი რიცხვების რაოდენობები 
დაგენერირებული 100 რიცხვიდან.
"""
#generate 100 random num using loop: 
def generate_random_num_using_loop():
    list_of_random_num = []
    for _ in range (100):
        random_num = randint(0,1000)
        list_of_random_num.append(random_num)
    return list_of_random_num

#implement task using comperhension
def generate_random_num_using_comperhension():
    random_num = [randint(0,1000) for _ in range(100)]
    return random_num      

def create_dict_of_even_and_odd_nums(numbers):
    dict_of_count_even_and_odd_num = {"even":0, "odd":0}
    for num in numbers:
        if num % 2 == 0:
            dict_of_count_even_and_odd_num["even"] += 1
        else:
            dict_of_count_even_and_odd_num["odd"] += 1
    return dict_of_count_even_and_odd_num
    
 
def main():
    generate_random_num = generate_random_num_using_comperhension()
    print(create_dict_of_even_and_odd_nums(generate_random_num))   

if __name__ == "__main__":
    main()