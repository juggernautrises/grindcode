# https://leetcode.com/problems/valid-anagram/description/

#  1) Check if the lengths of the two string differ and return False if they do
#  2) Construct a hashmap that keeps track of the count of each character for each word.
#  3) Loop through one of the hashmaps. If the character does not exist in the other hashmap or if the counts differ,
#     return False

def isAnagram(s, t):
    if len(s) != len(t):
        return False
    word = {}
    anagram = {}
    for i in range(len(s)):
        word[s[i]] = word.get(s[i], 1) + 1
        anagram[t[i]] = anagram.get(t[i], 1) + 1

    for char, count in word.items():
        if char not in anagram or anagram[char] != count:
            return False
    return True
