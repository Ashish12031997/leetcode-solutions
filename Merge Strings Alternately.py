def mergeAlternately(word1: str, word2: str) -> str:
    string = ''
    n=1
    while n <= len(word1) and n <= len(word2):
        string = string + word1[n-1:n] + word2[n-1:n]
        n+=1
        print(string)
    if len(word1) > len(word2):
        string += word1[len(word2)-1:]
        return string
    elif len(word2) > len(word1):
        string += word2[len(word1):]
        return string
    else:
        return string


word1 = "ab"
word2 = "pqrs"
print(mergeAlternately(word1, word2))
