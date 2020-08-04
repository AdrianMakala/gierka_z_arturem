import numpy as np
from numpy import random


class Map:
    def __init__(self, size, biom, enemy_ratio, item_ratio, object_ratio):
        self.size = size
        self.biom = biom

        self.enemy_ratio = enemy_ratio
        self.item_ratio = item_ratio
        self.object_ratio = object_ratio
        self.all_ratios = [self.enemy_ratio, self.item_ratio, self.object_ratio]

        self.matrix_size = (self.size, self.size)
        self.matrix = np.zeros(self.matrix_size)

    def get_position(self, a, b):
        return self.matrix[a][b]

    def set_player_position(self, matrix, player_position):
        matrix[player_position] = 100

    def gen_map(self):
        for counter in range(len(self.all_ratios)):
            if counter == 0:
                marker = 1
            elif counter == 1:
                marker = 2
            elif counter == 2:
                marker = 4

            num_of_objects = self.size * self.size * (self.all_ratios[counter] / 10000)
            indices = np.random.choice(np.arange(self.matrix.size), replace=False, size=int(self.matrix.size * num_of_objects))

            for i in indices:
                if i > 9:
                    i = str(i)
                    x_pos = i[0]
                    y_pos = i[1]
                    self.matrix[int(x_pos), int(y_pos)] += marker
                    # print("ADDED VALUE {} X:{}, Y:{}".format(marker, x_pos, y_pos))
                else:
                    self.matrix[0, i] += marker
                    # print("ADDED VALUE {} X:{}, Y:{}".format(marker, 0, i))

        return self.matrix
