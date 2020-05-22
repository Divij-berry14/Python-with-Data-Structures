# def countFrequency(string, ch):
#     count = 0;
#
#     for i in range(len(string)):
#
#         # Check for vowel
#         if (string[i] == ch):
#             count += 1;
#
#     return count;
#
#
# def sortArr(string):
#     n = len(string);
#
#     vp = [];
#
#     for i in range(n):
#         vp.append((countFrequency(string, string[i]), string[i]));
#         print(vp)
#
#     vp.sort(reverse=True);
#     print(vp)
#     for i in range(len(vp)):
#         print(vp[i][1], end="");
#
# s="aabbbbccc"
# sortArr(s)

s="abbbbccc"
d={}
for w in s:
    d[w]=d.get(w,0)+1
print(d)
print(sorted(d.items(),reverse=True, key=lambda kv: (kv[1], kv[0])))