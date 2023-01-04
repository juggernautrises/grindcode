# https://leetcode.com/problems/maximum-number-of-balloons/
# Keep a count of the balloon characters in the text. Divide each count by the required count to construct balloon
# and get the minimum of each balloon character.

def maxNumberOfBalloons(text):
    balloon = {}
    for c in 'balloon':
        balloon[c] = balloon.get(c, 0) + 1
    count = {}
    res = len(text) + 1
    for c in text:
        count[c] = count.get(c, 0) + 1

    for char in balloon:
        res = min(res, count[char] // balloon[char])
    return res


text = 'loonbalxballpoon'
res = maxNumberOfBalloons(text)
print(res)
