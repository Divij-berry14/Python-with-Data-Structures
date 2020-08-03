def reverse(s):
    bad_chars = [';', ':', '!', "*", ",", "."]
    s = s.lower()
    s = ''.join(e for e in s if e.isalnum())
    # for i in bad_chars:
    #     s=s.replace(i,"")
    s = s.replace(" ", "")
    string = "".join(reversed(s))
    if s == string:
        return True
    else:
        return False


s = "race a car"
print(reverse(s))