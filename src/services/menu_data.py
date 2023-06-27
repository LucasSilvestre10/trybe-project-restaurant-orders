# Req 3
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        csv_rows = self._read_csv(source_path)
        self._dishes_gen(csv_rows)

    def _read_csv(self, source_path):
        with open(source_path, "r") as csv_file:
            return csv_file.readlines()[1:]

    def _dishes_gen(self, csv_rows):
        dishes_dict = {}
        for row in csv_rows:
            name, price, ingredient, ingredient_amount = row.split(",")

            dish = dishes_dict.get(name)
            if dish is None:
                dishes_dict[name] = Dish(name, float(price))

            ingredient = Ingredient(ingredient)
            dishes_dict[name].add_ingredient_dependency(
                ingredient, int(ingredient_amount)
            )

        self.dishes = set(dishes_dict.values())
