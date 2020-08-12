# def hIndex(citations):
#     n = len(citations)
#     l, r = 0, n - 1
#     while (l <= r):
#         mid = int(l + (r - l) / 2)
#         print("mid",mid)
#         if citations[mid] < n - mid:
#             l = mid + 1
#             print("l",l)
#         else:
#             r = mid - 1
#             print("r",r)
#     return n - l
#
# li = [int(x) for x in input().split()]
# print(hIndex(li))
def isPalindrome(s):
    bad_chars = [';', ':', '!', "*", ",", "."]
    s = s.lower()
    print(s)
    s = ''.join(e for e in s if e.isalnum())
    print(s)
    # for i in bad_chars:
    #     s=s.replace(i,"")
    # s = s.replace(" ", "")
    # print(s)
    string = "".join(reversed(s))
    print(string)
    if s == string:
        return True
    else:
        return False


s="A man, a plan, a canal: Panama"
print(isPalindrome(s))