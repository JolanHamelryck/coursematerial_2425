# write your code here
def last_character(string):
    lengte_string = len(string)
    last_char = lengte_string - 1
    if len(string) == 0:
        return None 
    return string[last_char]