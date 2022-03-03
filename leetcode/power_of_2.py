def is_power_of_two(n):

    if n<=0:
        return False
    if n==1 or n==2:
        return True

    while n>2:
        if n%2!=0:
            return False
        n=n//2
    return True