# write your code here
def passing_percentage(grades):
    passed = 0
    students = len(grades)
    if students == 0:
        return 0
    
    for i in grades:
        if i >= 10:
            passed += 1

    return  (passed / students) * 100 

