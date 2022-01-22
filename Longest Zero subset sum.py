li = [int(i) for i in input().split()]
hash_map = {}
summ = 0
max_len = 0
for i in range(len(li)):
    summ += li[i]
    if li[i] is 0 and max_len is 0:
        max_len = 1

    if summ is 0:
        max_len = i + 1
    if summ in hash_map:
        max_len = max(max_len, i-hash_map[summ])
    else:
        hash_map[summ] = i
print(max_len)
