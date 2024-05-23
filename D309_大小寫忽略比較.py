def compare_strings(s, t):
    s = s.lower()
    t = t.lower()
    
    if s < t:
        return "Smaller"
    elif s > t:
        return "Greater"
    else:
        return "Equal"

s = input()
t = input()
result = compare_strings(s, t)
print(result)