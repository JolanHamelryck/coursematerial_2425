# write your code here
def next_player(player, player_count):

    x = (player + 1) % player_count
    
    return x


print(next_player(24,25))
