""" 
დაწერეთ ფუნქცია, რომელსაც გადაეცემა ორი დალაგებული სია და დააბრუნებს ახალ სიას, 
რომელშიც იქნება ელემენტები ორივე სიიდან დალაგებული მიმდევრობით.
Main ფუნქციიდან გატესტეთ თქვენს მიერ შექმნილი ფუნქცია სხვადასხვა ინფუთისთვის. 
Არ გამოიყენოთ ფუნქციები sort და sorted. Შეეცადეთ რომ თქვენ შერწყათ
გადმოცემული ორი სია ისე, 
რომ დალაგება არ დაირღვეს.
"""
def merge_lists(list1, list2):
    merged = []
    i = 0  
    j = 0  
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    
    while i < len(list1):
        merged.append(list1[i])
        i += 1
        
    while j < len(list2):
        merged.append(list2[j])
        j += 1
    
    return merged

def main():
    list1 = [1, 3, 10]
    list2 = [0, 4, 7, 9]
    
    list3 = [3,50]
    list4 = [0, 4, 7, 9]
    print(merge_lists(list1, list2))
    print(merge_lists(list3, list4))

if __name__ == "__main__":
    main()
