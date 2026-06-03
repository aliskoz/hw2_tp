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


class ShoppingList:
    def __init__(self):
        self._items = []

    def add_recipe(self, recipe, portions):
        if portions<=0:
            raise ValueError("Количество порций должно быть положительным")
        x = recipe.scale(portions)
        for a in x.ingredients:
            self._items.append((a, recipe.title))

    def remove_recipe(self, title):
        res = []
        for a, b in self._items:
            if b != title:
                res.append((a, b))
        self._items = res

    def get_list(self):
        d = {}
        for a, b in self._items:
            c = (a.name, a.unit)
            if c in d:
                d[c] += a.quantity
            else:
                d[c] = a.quantity
        m = []
        for i in d:
            m.append(i)
        m.sort()
        res = []
        for i in m:
            name = i[0]
            unit = i[1]
            quantity = d[i]
            res.append(Ingredient(name, quantity, unit))
        return res

    def __add__(self, other):
        res = ShoppingList()
        for a in self._items:
            res._items.append(a)
        for a in other._items:
            res._items.append(a)
        return res

# a = Recipe("ГРИБНОЙ СУП",[Ingredient('картошка', 30, 'г')])
# a.add_ingredient(Ingredient("гриб", 50, "г"))
# s = ShoppingList()
# s.add_recipe(a, 2)
# print(s.get_list())
# s.remove_recipe("ГРИБНОЙ СУП")
# print(s.get_list())


class DietaryRecipe(Recipe):
    def __init__(self, title, diet_type, ingredients=None):
        super().__init__(title, ingredients)
        self.diet_type = diet_type

    def scale(self, ratio):
        scaled = super().scale(ratio)
        return DietaryRecipe(scaled.title, self.diet_type, scaled.ingredients)

    def __str__(self):
        return "[" + self.diet_type + "] " + super().__str__()

# a=DietaryRecipe('пицца', 'веган', [a, b])
# print(a)
# print(a.scale(2))



