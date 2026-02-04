class Food:
    def __init__(self, name, manufacturer):
        self.name = name
        self.manufacturer = manufacturer
class Drink:
    def __init__(self, name, manufacturer):
        self.name = name
        self.manufacturer = manufacturer

class Buffet:
    def __init__(self, foods, drinks):
        self.foods = foods
        self.drinks = drinks
    def take_food(self, food):
        self.foods.append(food)
    def give_food(self):
        return self.foods.pop()
    def take_drink(self, drink):
        self.drinks.append(drink)
    def give_drink(self):
        return self.drinks.pop()

food1 = Food("sandwich", "romanovskiy")
food2 = Food("...", "...")
food3 = Food("...", "...")
drink1 = Drink("...", "...")
drink2 = Drink("...", "...")
drink3 = Drink("...", "...")

buffet = Buffet(foods=[food1, food2, food3], drinks=[drink1, drink2, drink3])
