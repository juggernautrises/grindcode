# https://leetcode.com/problems/contains-duplicate/description/

# Nothing fancy here, just add the values to the set and if the value already exists in the set, return True
def containsDuplicate(nums):
    dupes = set()
    for n in nums:
        if n in dupes:
            return True
        dupes.add(n)
    return False
