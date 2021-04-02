from numpy import matrix 

grid = [

[6,0,0, 0,0,2, 5,0,0],
[0,1,7, 5,0,0, 0,0,0],
[4,0,0, 0,0,0, 0,2,0],

[0,7,0, 0,2,3, 0,6,0],
[0,0,0, 0,1,0, 3,0,0],
[0,0,2, 0,0,5, 7,0,0],

[0,0,0, 4,0,0, 0,0,0],
[0,9,5, 0,0,0, 0,3,0],
[1,0,8, 0,3,0, 9,0,0]

]

"""
write grid printer use .format()
(x,y)
(0,0), (3,0), (6,0)
(0,3), (3,3), (6,3)
(0,6), (3,6), (6,6)
"""
def checkTrinet(startX,startY,n):
    global grid
    endX = startX+2
    endY = startY+2
    arr = []
    for i in range(startY, endY+1):
        for j in range(startX, endX+1):
            arr.append(grid[i][j])
    
    if n in arr:
        return True
    else:
        return False
        
def canPlace(x,y,n):
    global grid
    
    for i in range(9):
        if grid[y][i] == n:
            return False
    
    for j in range(9):
        if grid[j][x] == n:
            return False    
        
    strtX = (x//3)*3
    strtY = (y//3)*3
        
    if checkTrinet(strtX,strtY,n):
        return False
            
    return True
        
def solve():
    global grid
    
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0: #Empty slot
                for num in range(1,10):
                    if canPlace(x,y,num):
                        grid[y][x]=num
                        solve()
                        grid[y][x]=0
                
                return



    print(matrix(grid))
        
solve()
