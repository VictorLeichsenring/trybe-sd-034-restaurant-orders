from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


def test_ingredient():
    ingredient_1 = Ingredient("Tomate")
    ingredient_2 = Ingredient("Tomate")
    assert ingredient_1.name == "Tomate"
    assert ingredient_1.restrictions == set()
    assert hash(ingredient_1) == hash("Tomate")
    assert ingredient_1 == ingredient_2
    assert repr(ingredient_1) == "Ingredient('Tomate')"
