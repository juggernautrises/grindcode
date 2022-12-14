# https://leetcode.com/problems/balanced-binary-tree/

def isBalanced(root):
    def balance_checker(node):
        if not node:
            return True, 0
        left = balance_checker(node.left) + 1
        right = balance_checker(node.right) + 1
        is_balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        return is_balanced, max(left, right) + 1

    return balance_checker(root)[0]
