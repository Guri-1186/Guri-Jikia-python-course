import random




list_1 = []
def gogo ():
   for _ in range(4):
    random_num = random.randint(1,30)
    list_1.append(random_num)
    
   return list_1


print(gogo())
