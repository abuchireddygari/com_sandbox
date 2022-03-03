def word_pat(pattern,s):
    words=s.split()
    print(words)
    w2p={}

    if len(pattern)!=len(words):
        return False

    if len(set(pattern))!=len(set(words)):
        return False

    for i in range(len(words)):
        if words[i] not in w2p:
            w2p[words[i]]=pattern[i]
        elif w2p[words[i]]!=pattern[i]:
            return False

    return True

print(word_pat("abba", "dog cat cat dog"))
print(word_pat("abba", "dog cat cat fish"))