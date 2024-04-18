import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = self._read_csv_and_create_dishes()

    def _read_csv_and_create_dishes(self):
        dish_dict = {}

        with open(self.source_path, "r") as file:
            arquivo = csv.DictReader(file)
            for linha in arquivo:
                dish_name = linha["dish"]
                price = float(linha["price"])
                ingredient_name = linha["ingredient"]
                quantity = int(linha["recipe_amount"])

                if dish_name not in dish_dict:
                    new_dish = Dish(dish_name, price)
                    new_dish.add_ingredient_dependency(
                        Ingredient(ingredient_name), quantity)
                    dish_dict[dish_name] = new_dish
                else:
                    existing_dish = dish_dict[dish_name]
                    existing_dish.add_ingredient_dependency(
                        Ingredient(ingredient_name), quantity)

        return set(dish_dict.values())
