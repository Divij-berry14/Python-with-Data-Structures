from collections import Counter 
def isValid(s):  
    s1 = Counter(s) 
    values = list(s1.values()) 
    val_max = max(values) 
    val_min = min(values) 
    
    if val_max == val_min or (val_max - val_min == 1 and values.count(val_max) == 1) or (val_min == 1 and values.count(val_min) == 1 and len(set(values)) == 2 ):
        return 'YES' 
    else: 
        return 'NO'

s=input()
output=isValid(s)
print(output)