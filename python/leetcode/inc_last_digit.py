def plus_one(digits):
    end=len(digits)-1
    add=digits[end]+1
    carry=add//10
    while carry==1 and end>0:
        digits[end]=0
        end=end-1
        add=digits[end]+carry
        carry=add//10

    if carry==1 and end==0 and digits[end]==9:
        digits[end]=0
        digits.insert(0,1)
        return digits
    else:
        digits[end]=digits[end]+1
        return digits

print(plus_one([9,9,9]))
print(max(9,9))