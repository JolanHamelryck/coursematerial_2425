# write your code here
# def box(string):
#     dashes = len(string) * '-'
#     dashline = f'+ {dashes} +'
#     return f'{dashline}\n| {string} |\n{dashline}'
def box(string):
    border = '+' + '-' * (len(string) + 2) + '+'
    content = f"| {string} |"
    return f"{border}\n{content}\n{border}"
