def longest(s):
    max_char=""
    max_num=0
    prev_char=""
    for i in s:
        if prev_char==i:
            count+=1
        else:
            count=1
        if count>max_num:
            max_num=count
            max_char=i
        prev_char=i
    return {max_char:max_num}

s = "AABCDDBBBEA"
#s = "AABCDDBBBEEEEEFFFFFFFA"
print(longest(s))