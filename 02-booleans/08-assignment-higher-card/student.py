# write your code here
def higher_card(card1, card2):
    if card2 == 1:
        return False 
    
    if card1 == 1:
        return True  
    
    return card1 > card2
