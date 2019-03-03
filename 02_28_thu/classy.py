class Ingredient:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def buy(self, num):
        self.amount += num


# ing_dict = {'carrots': 2, 'apples': 5}
# f"{ing_dict['apples']}{ing_dict['carrots']"