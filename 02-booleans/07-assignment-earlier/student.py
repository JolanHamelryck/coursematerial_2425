# write your code here
def earlier(h1, m1, h2, m2):
    # Compare hours first
    if h1 < h2:
        return True
    elif h1 == h2:
        # If hours are equal, compare minutes
        return m1 < m2
    else:
        return False