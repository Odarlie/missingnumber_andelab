def find_missing(one, two):
    '''
function that finds a missing number between two arrays 
'''
    missing = []
    for n in one:
        if n not in two:
            missing.append(n)
    for n in two:
        if n not in one:
            missing.append(n)

    if len(missing) > 0:
        if len(missing) == 1:
            return missing[0]
        else:
            return missing
    else:
        return 0
