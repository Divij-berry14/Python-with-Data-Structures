def longest_palindrome_string(s):
    if len(s) <= 1:
        return s
    max_len = 1
    n = len(s)
    st, end_s = 0, 0

    # odd length
    for i in range(n - 1):
        start, end = i, i
        while start >= 0 and end < n:
            if s[start] == s[end]:
                start -= 1
                end += 1
            else:
                break
        temp_length = end - start - 1
        if temp_length > max_len:
            max_len = temp_length
            st, end_s = start+1, end - 1

    # Even length
    for i in range(n - 1):
        start, end = i, i + 1
        while start >= 0 and end < n:
            if s[start] == s[end]:
                start, end = start - 1, end + 1
            else:
                break
        _len = end - start - 1
        if _len > max_len:
            max_len = _len
            st, end_s = start + 1, end - 1

    return s[st:end_s + 1]


string_ = input()
print(longest_palindrome_string(string_))
