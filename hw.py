class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value<=0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = float(value)

    def __str__(self):
        return f"{self.name}: {self.quantity}{self.unit}"

    def __repr__(self):
        return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"

    def __eq__(self, other):
        return self.name == other.name and self.unit == other.unit

# a = Ingredient('мука', 50, 'г')
# b = Ingredient('мука', 100, 'г')
# print(a)
# print(str(a))
# print(a==b)

class Recipe:
    def __init__(self, title, ingredients):
        self.title = title
        self.ingredients = ingredients

    def add_ingredient(self, ingredient):
        for a in self.ingredients:
            if a.name==ingredient.name and a.unit==ingredient.unit:
                a.quantity+=ingredient.quantity
                break
        else:
            self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        if ratio > 0:
            return True
        return False

    def scale(self, ratio):
        res = Recipe(self.title, [])
        for a in self.ingredients:
            ing = Ingredient(a.name, a.quantity*ratio, a.unit)
            res.add_ingredient(ing)
        return res

    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        res = self.title + ": "
        for a in self.ingredients:
            res += str(a) + "; "
        return res

# a=Recipe('blablabla', [Ingredient('мука', 30, 'г')])
# a.add_ingredient(Ingredient('мука', 30, 'г'))
# print(a.ingredients)
# print(a)
# print(a.scale(2))





