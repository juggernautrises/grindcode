# https://leetcode.com/problems/combination-sum/
def combinationSum(candidates, target):
    """
    :param candidates:
    :param target:
    :return:
    """
    # For each candidate, we'll attempt to build a value from 0->target (i).
    # If i == candidate, add the candidate by itself
    # if i-c >0, iterate through each combination and append the candidate value
    # The last item in the list will be the combination of the target value

    dp = [[] for _ in range(target + 1)]

    for c in candidates:
        for i in range(1, target + 1):
            if i < c:
                continue
            if i == c:
                dp[i].append([c])
            else:
                for combo in dp[i - c]:
                    dp[i].append(combo + [c])
    return dp[target]


c = [2, 3, 6, 7]
t = 7

res = combinationSum(c, t)
print(res)
