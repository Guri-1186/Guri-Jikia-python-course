"""
3. Შექმენით სია და შეავსეთ სიტყვებით. 
Პროგრამამ უნდა გაფილტროს სია, გადაყაროს
ყველა ელემენტი რომელიც შეიცავს 3 ზე მეტ სიმბოლოს და
ეკრანზე უნდა დაბეჭდოს დარჩენნილი 
სიტყვები მაღალ რეგისტრში.
"""
list_of_words = ["flower", "forest", "you", "heh"]
filter_list = [word.upper() for word in list_of_words if len(word) <=3]


def main ():
    print(filter_list)
if __name__ == "__main__":
    main()