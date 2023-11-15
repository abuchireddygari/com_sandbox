def is_palindrome(num):
    rev_num=0
    while num>rev_num:
        rev_num=rev_num*10
        rev_num=rev_num+num%10
        num=num//10
    return num==rev_num or num==rev_num//10

print(is_palindrome(1001))