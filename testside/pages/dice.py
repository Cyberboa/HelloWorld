from secrets import choice


class Dice:

    def __init__(self, side_one=1, side_two=2, side_three=3, side_four=4, side_five=5, side_six=6):
        self.side_one = side_one
        self.side_two = side_two
        self.side_three = side_three
        self.side_four = side_four
        self.side_five = side_five
        self.side_six = side_six

    def get_side_one(self):
        return self.side_one

    def get_side_two(self):
        return self.side_two

    def get_side_three(self):
        return self.side_three

    def get_side_four(self):
        return self.side_four

    def get_side_five(self):
        return self.side_five

    def get_side_six(self):
        return self.side_six

    def set_side_one(self, new_side_one):
        self.side_one = new_side_one

    def set_side_two(self, new_side_two):
        self.side_one = new_side_two

    def set_side_three(self, new_side_three):
        self.side_one = new_side_three

    def set_side_four(self, new_side_four):
        self.side_one = new_side_four

    def set_side_five(self, new_side_five):
        self.side_one = new_side_five

    def set_side_six(self, new_side_six):
        self.side_one = new_side_six

    def throw(self):
        random_number = [self.get_side_one(), self.get_side_two(), self.get_side_three(), self.get_side_four(),
                         self.get_side_five(), self.get_side_six()]
        chosen = choice(random_number)
        return chosen


my_dice = Dice(5, 8, 9, 15, 19, 22)
print(my_dice.throw())
