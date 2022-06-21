def search_binary(test_list,value):
    first=0
    last=len(test_list)-1
    is_found=False

    while first<=last and not is_found:
        mid=(first+last)//2
        if test_list[mid]==value:
            is_found=True
        else:
            if value<test_list[mid]:
                last=mid-1
            else:
                first=mid+1
    return is_found

print("search binary")
print(search_binary([0, 1, 2, 8, 13, 17, 19, 32, 42],32))
print(search_binary([0, 1, 2, 8, 13, 17, 19, 32, 42],20))

