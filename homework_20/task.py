"""
#TODO
1)Დაწერეთ პროგრამა რომელიც json ფაილიდან წაიკითხავს რეცეპტებს. 
Რეცეპტი შეიცავს ინგრედიენტების სიას. 

2) Პროგრამამ ასევე უნდა წაიკითხოს მეორე json ფაილი,
რომელშიც მოცემულია მაღაზიებში ხელმისაწვდომი პროდუქტების სია. 

3)Პროგრამამ მომხმარებელს უნდა ჰკითხოს რომელი კერძის მომზადებას აპირებს
და ეკრანზე დაუბეჭდოს მაღაზიები, რომელში წასვლაც მოუწევს მომხმარებელს ამ კერძის 
პროდუქტების შესაგროვებლად. 

4)Პროგრამამ უნდა შეეცადოს რომ რაც შეიძლება ნაკლებ მაღაზიაში გაუშვას 
მომხმარებელი დროისა და ფულის დასაზოგად.

5)Თუ ვერ ხერხდება არჩეული კერძისთვის საჭირო ინგრედიენტების მოძიება, 
დაუწეროს რომ ამ კერძს ამ ქალაქში ვერ მოამზადებს.
"""
import json
from pathlib import Path
import traceback

base_dir = Path("homework_20")
json_file_market = base_dir / "homework_1_markets.json"
json_file_recipe = base_dir / "homework_1_recipes.json"
try:
    with json_file_recipe.open("r") as recipe_file:
        recipe_data = json.load(recipe_file)
        
    with json_file_market.open("r") as market_file:
        market_data = json.load(market_file)

    def select_dish(dish_name):
        dish_name = dish_name.lower()
        for recipe in recipe_data:
            if recipe.lower() == dish_name:
                return recipe_data[recipe]["ingredients"]
        print(f"No recipe found for '{dish_name}'.")
        return []

    def select_market(selected_dishes, market_data):
        selected_markets = set()
        remaining_ingredients = set(selected_dishes)

        for market, items in market_data.items():
            if remaining_ingredients & set(items):
                selected_markets.add(market)
                remaining_ingredients -= set(items)
        return selected_markets, remaining_ingredients

    def main():
        user_input = input("Which dish are you going to prepare? ").strip().lower()
        selected_dishes = select_dish(user_input)

        if not selected_dishes:
            return
        
        selected_markets, missing_ingredients = select_market(selected_dishes, market_data)
        
        if missing_ingredients:
            print(f"Cannot prepare the {user_input} in this town. Missing ingredients: {', '.join(missing_ingredients)}")
        else:
            print("You can get all the ingredients from the following markets:")
            print(", ".join(selected_markets))

    if __name__ == "__main__":
        main()

except FileNotFoundError as e:
    print(f"File not found: {e.filename}")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
except Exception as ex:
    print(f"An unexpected error occurred: {ex}")
    traceback.print_exc()
