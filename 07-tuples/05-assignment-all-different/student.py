# write your code here
def all_different(xs):
    if len(xs) <= 1: 
        return True
    
    for i in range(len(xs)):
        for j in range(i + 1, len(xs)):
            if xs[i] == xs[j]:
                return False
    return True