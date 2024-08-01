def isAnagram(s: str, t: str) -> bool:
    from collections import Counter
    sc = Counter(s)
    tc = Counter(t)

    for i in sc:
        if tc[i] != sc[i]:
            return False
    return True


s = "anagram" 
t = "nagaram"
isAnagram(s,t)
