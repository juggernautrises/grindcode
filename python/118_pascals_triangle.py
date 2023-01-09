# https://leetcode.com/problems/pascals-triangle/
# Create a temp row by adding [0] to the start and end of the previous row.
# Add the current index plus the value of the one behind it and add that new row to the output.
def generate(numRows):
    res = [[1]]
    if numRows == 1:
        return res
    for n in range(numRows - 1):
        tmp = [0] + res[-1] + [0]
        row = []
        for i in range(1, len(tmp)):
            row.append(tmp[i - 1] + tmp[i])
        res.append(row)
    return res


res = generate(5)
print(res)
