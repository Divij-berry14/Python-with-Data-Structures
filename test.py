from collections import Counter


def removeChars(str1, str2):
    # make dictionaries from both strings
    dict1 = Counter(str1)
    dict2 = Counter(str2)
    print(dict1)
    print(dict2)
    # extract keys from dict1 and dict2
    keys1 = dict1.keys()
    keys2 = dict2.keys()

    # count number of keys in both lists of keys
    count1 = len(keys1)
    count2 = len(keys2)

    # convert list of keys in set to find common keys
    set1 = set(keys1)
    print(set1)
    commonKeys = len(set1.intersection(keys2))
    print(commonKeys)

    if (commonKeys == 0):
        return count1 + count2
    else:
        return (max(count1, count2) - commonKeys)

    # Driver program


if __name__ == "__main__":
    str1 = 'bcadeh'
    str2 = 'hea'
    print(removeChars(str1, str2))