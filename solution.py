'''
    Hi, I am Tsao-Ching from UW-Madison, and this is my solution to this problem.

    To me, this is like a DFS problem, and I store the pyramid in a 2D list.
    I tried to go through every path to see if the product of that path is equal to the target. 
    
    1. If the current value is bigger than the target, that means it is not the right path, and I
    should go back to the upper level.
    2. If it is equal to the target. That means we got the answer! Therefore, I return the current path.
    3. If it is smaller than the target, I need to keep going down that path to see if it is right.

    For the return value, it can either be None or a string of "L*R*", so I do an OR operation to 
    make sure I can have the answer if either of them is not None.

    --------------------------------------------------------------------------------------------
    Edge Cases Control
    1. If there is no such a path's product equivalent to the target, print and write 'No answer in the pyramid.'.
    2. If the pyramid only has one element, and it equals to the target, print and write 'The first element of the pyramid equals to the product. No L or R printed.'
    3. Otherwise, print and write the answer to 'myanswer.txt'.

'''


def backtrack(p:list, target:int, curval:int, path:list, curindex:tuple):
    # already bigger than the answer, try another path
    if curval > target:
        return
    # got the answer
    if curval == target:
        return "".join(path)

    left = None
    right = None
    # go left in the pyramid (down in the list)
    if curindex[0] + 1 < len(p):
        path.append('L')
        left = backtrack(p, target, curval * p[curindex[0]+1][curindex[1]], path,(curindex[0]+1,curindex[1]))
        path.pop()
    # go right in the pyramid (down right in the list)
    if curindex[0] + 1 < len(p) and curindex[1] + 1 < len(p[curindex[0]+1]):
        path.append('R')
        right = backtrack(p, target, curval * p[curindex[0]+1][curindex[1]+1], path,(curindex[0]+1,curindex[1]+1))
        path.pop()
    return left or right


pyramid = []
target = None
# read file 
print('start')
with open('./pyramid_sample_input.txt', 'r') as f:
    # read first line to get target
    target = int(f.readline().split()[1])
    # store value into 2d list and transform from str into int
    pyramid = [list(map(int, line.split(','))) for line in f]

ans = backtrack(pyramid, target, pyramid[0][0], [], (0,0))
with open('./myanswer.txt','w') as f:
    if ans == '':
        print('The first element of the pyramid equals to the product. No L or R printed.')
        f.write('The first element of the pyramid equals to the product. No L or R printed.')
    elif ans == None:
        print('No answer in the pyramid.')
        f.write('No answer in the pyramid.')
    else:
        print(ans)
        f.write(ans)
print('end...answer has been written to myanswer.txt')

