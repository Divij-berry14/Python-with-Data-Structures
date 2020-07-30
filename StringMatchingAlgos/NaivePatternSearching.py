def NaivePatternSearching(txt,pat):
    n=len(txt)
    m=len(pat)
    for i in range(n-m+1):
        j=0
        while(j<m):
            if(txt[i+j]==pat[j]):
                j=j+1
            else:
                break
        if j==m:
            print("Pattern found at index at position",i)

txt = "AABAACAADAABAAABAA"
pat = "AABA"
NaivePatternSearching(txt,pat)

#What is the best case?
# The best case occurs when the first character of the pattern is not present in text at all.
# txt[] = "AABCCAADDEE";
# pat[] = "FAA";
# The number of comparisons in best case is O(n).

# What is the worst case ?
# The worst case of Naive Pattern Searching occurs in following scenarios.
# 1) When all characters of the text and pattern are same.
# txt[] = "AAAAAAAAAAAAAAAAAA";
# pat[] = "AAAAA";

# 2) Worst case also occurs when only the last character is different.
# txt[] = "AAAAAAAAAAAAAAAAAB";
# pat[] = "AAAAB";
# The number of comparisons in the worst case is O(m*(n-m+1))