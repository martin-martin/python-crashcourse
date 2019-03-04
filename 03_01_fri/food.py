class Food:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def buy(self, number):
        self.amount += number

    def expire(self):
        self.name = f"expired {self.name}"

    def __str__(self):
        return f"{self.amount} of {self.name}"


class Spice(Food):
    def __init__(self, name, amount, spiciness):
        super().__init__(name, amount)
        self.spiciness = spiciness

    def expire(self):
        print(f"{self.name} does not expire!")

