import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
from src.models.ingredient import Restriction


def test_dish():
    pasta_dish = Dish("Spaghetti Carbonara", 15.50)
    fish_dish = Dish("Grilled Salmon", 25.75)
    pasta_dish_duplicate = Dish("Spaghetti Carbonara", 15.50)

    assert pasta_dish.name == "Spaghetti Carbonara"
    assert hash(pasta_dish) == hash(pasta_dish_duplicate)
    assert hash(pasta_dish) != hash(fish_dish)

    assert pasta_dish == pasta_dish
    assert pasta_dish == pasta_dish_duplicate
    assert pasta_dish != fish_dish

    assert str(pasta_dish) == "Dish('Spaghetti Carbonara', R$15.50)"

    with pytest.raises(TypeError):
        Dish("Invalid Dish", "Fifteen Fifty")
    with pytest.raises(ValueError):
        Dish("Invalid Dish", -10)

    ingredient_bacon = Ingredient("bacon")
    pasta_dish.add_ingredient_dependency(ingredient_bacon, 200)
    assert pasta_dish.recipe.get(ingredient_bacon) == 200

    assert pasta_dish.get_restrictions() == {
        Restriction.ANIMAL_DERIVED, Restriction.ANIMAL_MEAT}

    assert Ingredient("bacon") in pasta_dish.get_ingredients()
