from random import uniform

"""
task.2 დაწერეთ პროგრამა რომელიც დააგენერირებს არამთელ შემთხვევით რიცხვს და დაამრგვალებს მეათედებამდე სიზუსტით. 
Შედეგი დაბეჭდეთ ეკრანზე.
Დამრგვალების ფუნქცია შეარჩიეთ თქვენი სურვილისამებრ. იხ module math
"""
random_num = round(uniform(1,100), 2)
print(f"Random floating-point number is {random_num}")