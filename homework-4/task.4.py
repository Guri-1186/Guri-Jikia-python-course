

positive_integer = int(input("Please enter positive integer: "))
if positive_integer < 0 or positive_integer >= 20:
    print("Invalid input, please enter a non negative integer less than 20.")
    exit(1)
 
num_1, num_2 = 0, 1
for _ in range(positive_integer):
    num_1, num_2 = num_2, num_1 + num_2

print("The Fibonacci number of input is:",num_1)


    
    



