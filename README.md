# Art_Of_Problem_Solving

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

    10/13/2023
