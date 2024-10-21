# write your code here

def is_digit(char):
    return char in '0123456789'

def is_student_id(string):
    
    if len(string) != 8:
        return False
    
    first_char = string[0]
    if not (first_char == 'r' or first_char == 'R' or first_char == 's' or first_char == 'S'):
        return False
    
    if not (is_digit(string[1]) and 
            is_digit(string[2]) and 
            is_digit(string[3]) and 
            is_digit(string[4]) and 
            is_digit(string[5]) and 
            is_digit(string[6]) and 
            is_digit(string[7])):
        return False
    
    return True
