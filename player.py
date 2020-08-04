import pandas as pd
from random import randint
import sys


class Character:
    def __init__(self, description):
        self.description = description
        self.hp = 1
        self.attack = 1
        self.defence = 1
        self.friendly = False
        self.eq = []


class Player(Character):
    def __init__(self, description, borders):
        super(Player, self).__init__(description)
        self.x_position = 0
        self.y_position = 0
        self.borders = borders

    def get_position(self):
        return self.x_position, self.y_position

    def go_up(self):
        if self.x_position != 0:
            self.x_position -= 1
        else:
            print("MAP LIMIT TOP")

    def go_down(self):
        if self.x_position != self.borders - 1:
            self.x_position += 1
        else:
            print("MAP LIMIT BOTTOM")

    def go_left(self):
        if self.y_position != 0:
            self.y_position -= 1
        else:
            print("MAP LIMIT LEFT")

    def go_right(self):
        if self.y_position != self.borders - 1:
            self.y_position += 1
        else:
            print("MAP LIMIT RIGHT")

    def look(self, whats_in_room):
        if whats_in_room == 101 or whats_in_room == 103 or whats_in_room == 105 or whats_in_room == 107:
            print("Monster!")
        if whats_in_room == 102 or whats_in_room == 103 or whats_in_room == 106 or whats_in_room == 107:
            print("Coin!")
        if whats_in_room == 104 or whats_in_room == 105 or whats_in_room == 106 or whats_in_room == 107:
            print("Object!")

    def pick_up(self):
        print("Picked up")
        self.eq.append("Coin")

    def show_eq(self):
        eq_df = pd.DataFrame(self.eq)
        print(eq_df.value_counts())


class Monster(Character):
    def __init__(self, description):
        super(Monster, self).__init__(description)
        self.chance_to_drop = randint(0, 10)
        self.is_elite = False
        print("You see {}".format(description))

    def fight(self):
        is_won = randint(0, 1)
        if is_won:
            print("WON")
        else:
            print("YOU DIED")
            sys.exit()
