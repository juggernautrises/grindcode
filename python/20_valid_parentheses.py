# https://leetcode.com/problems/valid-parentheses/
# Create a map of opening parentheses and their corresponding closing parentheses. Iterate through each character and
# check if it exists in the map (aka it's an opening paren). If it exists, add it to the stack.
# If it's not an opening paren, that means it's a closing one in which case we
# a) Check if the stack is empty or
# b) Check if the corresponding closing paren for the opening paren popped off the stack matches our current character.
# Return False if either of those are true
# Once we iterate through all characters, we can return true as long as nothing else remains in the stack.

def isValid(s):
    par_map = {'(': ')', '{': '}', '[': ']'}
    stack = []

    for char in s:
        if char in par_map:
            stack.append(char)
        else:
            if not stack or par_map[stack.pop()] != char:
                return False
    return len(stack) == 0
