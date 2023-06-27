from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    dish1 = Dish("ratatuia", 18.0)
    food = Ingredient("presunto")
    food2 = Ingredient("camarão")
    dish1.add_ingredient_dependency(food, 1)
    dish1.add_ingredient_dependency(food2, 1)
    dish2 = Dish("caviar", 1000.0)

    ingredients = {
        food,
        food2,
    }

    restrictions = {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
        Restriction.SEAFOOD,
    }

    assert hash(dish1) == hash(dish1)
    assert hash(dish1) != hash(dish2)
    assert dish1.name == "ratatuia"
    assert dish1.__eq__(dish1) is True
    assert dish1.__eq__(dish2) is False
    assert dish1.__repr__() == "Dish('ratatuia', R$18.00)"
    assert dish1.recipe.get(food) == 1
    assert dish1.recipe.get(food2) == 1
    assert dish1.get_restrictions() == restrictions
    assert dish1.get_ingredients() == ingredients

    with pytest.raises(ValueError):
        Dish("ratatuia", 0.0)
    with pytest.raises(TypeError):
        Dish("ratatuia", "18.0")
