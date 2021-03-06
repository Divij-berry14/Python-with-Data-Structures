#Sliding Window Algorithm

def findLongestSubstring(string):
    if len(string) == 0:
        return 0
    li = list(string)
    # print(li)
    n = len(string)
    d = {}
    for i in string:
        if i not in d:
            d[i] = 0
    print(d)
    i = 0
    j = 0
    ans = 1
    d[li[0]] = 1
    while(j != n - 1):
        key = li[j+1]
        if(d[key] == 0):
            j += 1
            d[li[j]] = 1
            ans = max(ans, j-i+1)
            print(d)
        else:
            d[li[i]] -= 1
            i += 1
            print(d)
    return ans

string = "abrexrz"
print(findLongestSubstring(string))
# def findLongestSubstring(string):
#     n = len(string)
#
#     # starting point of current substring.
#     st = 0
#
#     # maximum length substring without
#     # repeating characters.
#     maxlen = 0
#
#     # starting index of maximum
#     # length substring.
#     start = 0
#
#     # Hash Map to store last occurrence
#     # of each already visited character.
#     pos = {}
#
#     # Last occurrence of first
#     # character is index 0
#     pos[string[0]] = 0
#
#     for i in range(1, n):
#         #"GEEKSFORGEEKS"
#         # If this character is not present in hash,
#         # then this is first occurrence of this
#         # character, store this in hash.
#         if string[i] not in pos:
#             pos[string[i]] = i
#             print(pos)
#
#         else:
#             # If this character is present in hash then
#             # this character has previous occurrence,
#             # check if that occurrence is before or after
#             # starting point of current substring.
#             # "GEEKSFORGEEKS"
#             if pos[string[i]] >= st:
#
#                 # find length of current substring and
#                 # update maxlen and start accordingly.
#                 currlen = i - st
#                 print("currlen", currlen)
#                 if maxlen < currlen:
#                     maxlen = currlen
#                     start = st
#                     print("maxlen", maxlen)
#                     print("start", start)
#
#                 # Next substring will start after the last
#                 # occurrence of current character to avoid
#                 # its repetition.
#                 st = pos[string[i]] + 1
#                 print("st", st)
#
#             # Update last occurrence of
#             # current character.
#             pos[string[i]] = i
#             print("pos2", pos)
#
#         # Compare length of last substring with maxlen
#     # and update maxlen and start accocrdingly.
#     if maxlen < i - st:
#         maxlen = i - st
#         start = st
#         print("maxlen", maxlen)
#         print("start", start)
#
#
#     # The required longest substring without
#     # repeating characters is from string[start]
#     # to string[start+maxlen-1].
#     return string[start: start + maxlen]
#
#
# # Driver Code
# if __name__ == "__main__":
#     # string = "GEEKSFORGEEKS"
#     string = "aayush"
#     print(findLongestSubstring(string))

