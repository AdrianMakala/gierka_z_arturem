import os
import generate_map
from player import Player, Monster
import gameLogics

map_size = 10
# generate map
game_map_obj = generate_map.Map(map_size, 1, 50, 50, 50)
game_map = game_map_obj.generated_map
copy_game_map = game_map
# generate player
player = Player("This is you", map_size)
# controls
controls = {"w": player.go_up,
            "a": player.go_left,
            "s": player.go_down,
            "d": player.go_right,
            "l": player.look,
            "p": player.pick_up,
            "eq": player.show_eq,
            "help": gameLogics.show_help
            }

while True:
    game_map = copy_game_map.copy()
    game_map_obj.set_player_position(game_map, player.get_position())
    print(game_map)
    # print(player.get_position())
    current_floor = game_map[player.get_position()]
    if current_floor == 101 or current_floor == 103 or current_floor == 105 or current_floor == 107:
        monster = Monster("ugly mother fucker")
        if not monster.friendly:
            monster.fight()

    key = input(": ")

    if key in controls:
        if key == "l":
            controls[key](current_floor)
        else:
            controls[key]()

    else:
        print("WRONG COMMAND")

    os.system('cls')
