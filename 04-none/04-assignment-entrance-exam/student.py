def entrance_exam(grade1, grade2, grade3, grade4, grade5):

    # variable tracking skipped tests
    skipped_tests = 0

    # variable count number taken tests
    
    taken_tests = 0
    # variable total grade
    total_grade = 0
    for grade in [grade1, grade2, grade3, grade4, grade5]:
        if grade is None:
            skipped_tests += 1

        else:
            taken_tests += 1
            total_grade += grade

    if skipped_tests > 1:
        return False
    
    if taken_tests > 0 and total_grade/taken_tests >= 12:
        return True
    return False

    # if 2 grades = none return false
    
    # average must be at least 12 else return false



