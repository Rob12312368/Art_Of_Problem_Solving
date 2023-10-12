'''
    Hi, I am Tsao-Ching from UW-Madison, and this is my solution to this problem.

    To me, this is like a DFS problem. I tried to go through every path
    to see if the product of that path is equal to the target. In each recursion, I
    first go down in the array, which equals to going down left in the pyramid. After that 


'''


def backtrack(p, target, curval, path, curindex):
    # already bigger than the answer, try another path
    if curval > target:
        return
    # got the answer
    if curval == target:
        return "".join(path)

    left = None
    right = None
    if curindex[0] + 1 < len(p):
        path.append('L')
        left = backtrack(p, target, curval * p[curindex[0]+1][curindex[1]], path,(curindex[0]+1,curindex[1]))
        path.pop()
    if curindex[0] + 1 < len(p) and curindex[1] + 1 < len(p[curindex[0]]):
        path.append('R')
        right = backtrack(p, target, curval * p[curindex[0]+1][curindex[1]+1], path,(curindex[0]+1,curindex[1]+1))
        path.pop()
    return left or right


pyramid = []
target = None
# read file 
with open('./pyramid_sample_input.txt', 'r') as f:
    target = int(f.readline().split()[1])
    pyramid = [list(map(int, line.split(','))) for line in f]

ans = backtrack(pyramid, target, pyramid[0][0], [], (0,0))

with open('./myanswer.txt','w') as f:
    f.write(ans)

