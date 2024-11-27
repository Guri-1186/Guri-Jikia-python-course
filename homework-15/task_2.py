"""
2. Დაწერეთ პროგრამა რომელიც მიიღებს სტრიქონს. 
Პროგრამამ უნდა დაითვალოს ამ სტრიქონში არსებული 
სიმბოლოები რომელი რამდენჯერ გვხვდება და დაბეჭდოს ეკრანზე. 
მაგალითად Input: 
Python P – 1 y – 1 t – 1 h – 1 o – 1 n – 1
"""
def count_string_chars(word):
    dict_of_count_char = {}
    for char in word:
        if char in dict_of_count_char:
            dict_of_count_char[char] += 1
        else:
            dict_of_count_char[char] = 1
    return dict_of_count_char

# souliton with dict comperhension
def count_string_chars_using_comperhension(word):
    dict_of_count_char = {char: word.count(char) for char in (word)}
    return dict_of_count_char
   
def main():
    user_input = input("Please enter word : ").lower()
    result_loop = count_string_chars_using_comperhension(user_input)
    for key, value in result_loop.items():  #დავალებაში ნაჩვენები აუთფუთი როგორც არის, ისე რომ დამებეჭდა
        print(f"{key} - {value}")
    
if __name__ == "__main__":
    main()