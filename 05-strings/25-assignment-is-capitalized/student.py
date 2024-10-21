# write your code here
# def is_capitalized(string):
#     # Check for empty string
#     if string == "":
#         return False
    
#     # Check if the first character is uppercase and the rest are lowercase
#     return string[0].isupper() and string[1:].islower()

def is_capitalized(string):
    # Check for empty string
    if string == "":
        return False
    
    # Check if the first character is uppercase and the rest (if any) are lowercase
    return string[0].isupper() and (len(string) == 1 or string[1:].islower())
