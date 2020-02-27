def isMonotonic(A) -> bool:
    if A == sorted(A) or A == sorted(A)[::-1]:
        return True
    else:
        return False