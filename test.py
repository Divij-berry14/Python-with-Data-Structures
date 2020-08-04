def compareVersion(version1,version2):
    import re
    # You can use str.split('.'), but you may want to show your knowledge of Regex to interviewer
    # regular expression
    v1 = re.split('\\.', version1)
    v2 = re.split('\\.', version2)

    max_length = max(len(v1), len(v2))
    print(max_length)
    for i in range(max_length):
        if i<len(v1):
            temp1=int(v1[i])
        else:
            temp1=0
        if i<len(v2):
            temp2=int(v2[i])
        else:
            temp2=0
        print(i,temp1,temp2)

        if temp1 > temp2:
            return 1
        elif temp1 < temp2:
            return -1
    # can not return 0 in the loop
    # make sure all of the element are compared

    # return 0 at the end (v1 = v2)
    return 0

m=compareVersion(input(),input())
print(m)



