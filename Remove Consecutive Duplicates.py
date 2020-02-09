#aabccbaa
#abcba

def remove_1(S):
    n=len(S)
    j=0
    for i in range(n):
        if (S[j] !=S[i]): 
            j += 1
            S[j]=S[i]
            
    j += 1
    S=S[:j]
    return S

S=input()
S = list(S) 
str1=remove_1(S)
str2=''.join(str1)
print(str2)