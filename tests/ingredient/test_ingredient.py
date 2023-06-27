from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
from src.models.ingredient import Restriction


# Req 1
def test_ingredient():
    ingredient = Ingredient("farinha")
    assert ingredient.name == "farinha"
    assert ingredient.restrictions == {Restriction.GLUTEN}

    ingredient = Ingredient("unknown_ingredient")
    assert ingredient.name == "unknown_ingredient"
    assert ingredient.restrictions == set()

    ingredient = Ingredient("farinha")
    assert repr(ingredient) == "Ingredient('farinha')"

    ingredient1 = Ingredient("farinha")
    ingredient2 = Ingredient("farinha")
    assert ingredient1 == ingredient2

    ingredient1 = Ingredient("farinha")
    ingredient2 = Ingredient("bacon")
    assert not ingredient1 == ingredient2

    ingredient1 = Ingredient("farinha")
    ingredient2 = Ingredient("farinha")
    assert hash(ingredient1) == hash(ingredient2)

    ingredient1 = Ingredient("farinha")
    ingredient2 = Ingredient("bacon")
    assert hash(ingredient1) != hash(ingredient2)
