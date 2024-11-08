
"""
1. Მოცემულია ტემპერატურების მონაცემები კვირის განმავლობაში. 
Თითოეული დღისთვის ჩაინიშნეს დილის, შუადღს და საღამოს ტემპერატურები. 
((33, 34, 28), (24, 31, 27), (24, 23, 27), (28, 32, 34), (33, 21, 28), (20, 25, 31), 
(21, 31, 28)) . 
Თქვენი ამოცანაა: 
1) იპოვოთ თითოეული დღის საშუალო, მაქსიმალური და მინიმალური ტემპერატურა. 
2) Ასევე გამოთვალეთ კვირის საშუალო ტემპერატურა. 
Კვირის საშუალო გამოითვალეთ დღიური საშუალოების გამოყენებით. 
3)Ყველა ნაპოვნი მონაცემი დაბეჭდეთ ეკრანზე. 
Ბეჭდვისას გამოიყენეთ ისეთი ტექსტები რომ გასაგები იყოს პროგრამის შედეგი.
"""
def get_temperature_data(datas):
    results = []
    daily_average = []
    for data in datas:
        max_temp = max(data) 
        min_temp = min(data)
        avg_temp = sum(data) / len(data)
        daily_average.append(avg_temp)
        results.append([max_temp, min_temp, round(avg_temp,1)])
    week_avg_temp =sum(daily_average) / len(daily_average)
    print(f"Week avarage tmeperature is : {round(week_avg_temp)} C")
    return tuple(results)
      
def main():
    data = ((33, 34, 28), (24, 31, 27), (24, 23, 27), (28, 32, 34), (33, 21, 28), (20, 25, 31), 
(21, 31, 28))
    results = get_temperature_data(data)
    for index, result in enumerate(results, start=1):
        print(f"Day {index} - Max Temperature : {result[0]} - Min Temperature: {result[1]}- Average Temperature: {result[2]}")
        
main()