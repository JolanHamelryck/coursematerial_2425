# write your code here
def player_movement(position, left_arrow, right_arrow, shift):
    move_amount = 1 if not shift else 2
    
    if left_arrow and not right_arrow:
        position -= move_amount

    elif right_arrow and not left_arrow:
        position += move_amount

    return position

