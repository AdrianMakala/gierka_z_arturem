import os
import generate_map
import player

# generate map
game_map_obj = generate_map.Map(10, 1, 50, 50, 50)
game_map = game_map_obj.gen_map()
copy_game_map = game_map
# generate player
player = player.Player()
# controls
controls = {"w": player.go_up, "a": player.go_left, "s": player.go_down, "d": player.go_right}

while True:
    game_map = copy_game_map.copy()
    game_map_obj.set_player_position(game_map, player.get_position())
    print(game_map)
    # print(player.get_position())

    key = input(": ")
    if key in controls:
        controls[key]()

    else:
        print("WRONG COMMAND")

    os.system('cls')

