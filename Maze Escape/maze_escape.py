def unneg(x):
        if x<0: return -1*x
        return x

def manhattan(x1,y1,x2,y2):
    return unneg(x2-x1) + unneg(y2-y1)

def update_orientation(o,point):
    if point[0]==1: o['v']+=0
    elif point[0]>1: o['v']-=1
    else: o['v']+=1

    if point[1]==1: o['h']+=0
    elif point[1]<1: o['h']-=1
    else: o['h']+=1
    # print(point, o)

    
    return o
    
def orient(grid):
    o = {'h':0, 'v':0}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # print("\n",i,j, grid[i][j])
            if i==j==1 or grid[i][j]=='#': continue

            o = update_orientation(o, [i,j])


    if unneg(o['h'])>unneg(o['v']):
        if o['h']<0 and grid[1][0]=='-':
            return 'LEFT'
        elif grid[1][2]=='-':
            return 'RIGHT'

    if o['v']<0 and grid[2][1]=='-':
        return 'DOWN'
    else:
        return 'UP'



if __name__ == '__main__':
    # player = int(inp###ut())
    grid1 = []
    for i in range(0, 3):
        grid1.append(input())

    # print(grid1)
    grid = [[i for i in j] for j in grid1]
    
    print(orient(grid))