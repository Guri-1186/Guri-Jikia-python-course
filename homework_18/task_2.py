"""
2. Დაწერეთ პროგრამა რომელიც წინა ამოცანაში აღწერილი სტრუქტურის ფაილიდან 
წაიკითხავს გაყიდვების ინფორმაციას.

a. Პროგრამამ უნდა იპოვოს მაქსმალური შესყიდვის(პროდუქტების რაოდენობით, 
ერთ შესყიდვაში) განმხორციელებელი მომხმარებელი, თუ რამდენიმენა, მაშინ 
მომხმარებლების სია.

b. Პროგრამამ უნდა იპოვოს მაქსმალური შესყიდვის
(ყველა შესყიდვის ჯამური ღირებულებით) განმხორციელებელი მომხმარებელი, 
თუ რამდენიმენა, მაშინ მომხმარებლების სია.

c. Პროგრამამ უნდა იპოვოს შესყიდვების ღირებულების საშუალო არითმეტიკული

d. Პროგრამამ უნდა იპოვოს შესყოდვების რაოდენობების საშუალო არითმეტიკული

e. Პროგრამამ უნდა იპოვოს ყველაზე დიდი რაოდენობით გაყიდული პროდუქტი, 
თუ რამდენიმეა მაშინ, პროდუქტების სია.

Ნაპოვნი მონაცემები შეაგროვეთ dict ტიპის ობიექტში და ჩაწერეთ stats.json ფაილში.
Დააფორმატეთ stats.json ფაილი ისე, რომ მონაცემები ჩაიწროს ადვილად 
წაკითხვადი ფორმით.
"""
import json
from pathlib import Path
from collections import defaultdict, Counter

base_dir = Path("homework_18/my_dir")
data_file = base_dir / "data.txt"
stats_file = base_dir / "purchase_stats.json"

with data_file.open("r") as file:
    data = [line.strip().split(",") for line in file]

user_stats = defaultdict(lambda: {"total_amount": 0, "total_value": 0})
product_stats = Counter()

for user, product, amount, price in data:
    amount, price = int(amount), float(price)
    user_stats[user]["total_amount"] += amount
    user_stats[user]["total_value"] += amount * price
    product_stats[product] += amount

max_items = max(user_stats.values(), key=lambda x: x["total_amount"])["total_amount"]
max_value = max(user_stats.values(), key=lambda x: x["total_value"])["total_value"]
most_sold = max(product_stats.values())

stats = {
    "max_items_users": [user for user, stats in user_stats.items() if stats["total_amount"] == max_items],
    "max_value_users": [user for user, stats in user_stats.items() if stats["total_value"] == max_value],
    "average_purchase_value": sum(u["total_value"] for u in user_stats.values()) / len(data),
    "average_items_per_purchase": sum(u["total_amount"] for u in user_stats.values()) / len(data),
    "most_sold_products": [product for product, count in product_stats.items() if count == most_sold]
}

with stats_file.open("w") as file:
     json.dump(stats, file, indent=4)

print(json.dumps(stats, indent=4)) 
