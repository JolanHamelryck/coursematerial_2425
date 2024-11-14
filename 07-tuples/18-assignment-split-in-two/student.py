# write your code here
def split_in_two(xs):
    
    mid = (len(xs) + 1) // 2 
    
    return (xs[:mid], xs[mid:])
