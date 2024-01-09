"""Given two integer variables a and b, and a boolean variable flag. The task is to check the status and return accordingly.
Return True for the following cases:

Either a or b (not both) is non-negative and flag is false.
Both a and b are negative and flag is true.
Otherwise, return false."""

def checkStatus(a,b,flag):
    if (((a >= 0 and b < 0) or (a < 0 and b >= 0)) and flag is False) or ((a < 0 and b < 0) and flag is True):
        return True
    else:
        return False

print(checkStatus(-1,-1,True))