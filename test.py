"""
Just to test stuff.
"""

def spiralOrder(matrix):
        
        """
        when you move down/right a col/row the value for the corresponding variable is 1
        if you move in the opposite direction, the value is -1
        if you are going down a column, the index for that column doesn't change, so it stays 0.

        every time you hit a corner, you subtract the variable by 1. 1 -> 0 -> -1
        
        we cab use a circular array for this
        """
        
        directions = (0,1,0,-1)
        #these are the pointers to the above tuple
        move_horizontal, move_vertical = 0, 1

        #to keep track of what you visited, at the end we will turn this into a list and print it.
        #it seems like the numbers inside the matrix don't repeat, so we should be fine with this technique
        s = set()

        curr_x, curr_y = 0, 0
    
        while True:
            num = matrix[curr_x][curr_y]
            if num not in s:
                s.add(num)
            elif len(s) == len(matrix)*len(matrix[0]):
                break
            else:
                if move_vertical==3:
                    move_vertical = 0
                else:
                    move_vertical += 1

            
            if (curr_x + 1 == len(matrix[0])-1) or (num in s):
                if move_vertical==3:
                    move_vertical = 0
                else:
                    move_vertical += 1
            elif (curr_y + 1 == len(matrix)-1) or (num in s):
                if move_horizontal==3:
                    move_horizontal = 0
                else:
                    move_horizontal += 1
                

            curr_x += directions[move_horizontal]
            curr_y += directions[move_vertical]


        return list(s)


matrix = [[1,2,3],[4,5,6],[7,8,9]]
spiralOrder(matrix)