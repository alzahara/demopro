def isAnagram(s, t):
    if len(s) != len(t):
        return False

    for char in s:
        if char in t:
            t = t.replace(char, '', 1)
        else:
            return False

    return t == ''

# Test cases
print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))