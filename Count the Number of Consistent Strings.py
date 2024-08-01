from typing import List

def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
    total = 0
    allowed_set = set(allowed)
    for word in words:
        if all(char in allowed_set for char in word):
            total +=1
    return total
