def print_board(board):
    print("\n".join([" ".join(i) for i in board]))

def manhattan(x1,y1,x2,y2):
        return unneg(x2-x1) + unneg(y2-y1)

def unneg(x):
    if x<0: return -1*x
    return x

def pos_letter(letter, board):
    loc =  [[i,j] for i in range(len(board)) for j in range(len(board[i])) if letter in board[i][j]][0]
    # print(loc)
    return loc

def nextMove(n,r,c,grid):
    princess_pos = pos_letter('p', grid)
    curr_pos = pos_letter('m', grid)

    if unneg(princess_pos[0]-curr_pos[0]) > unneg(princess_pos[1] - curr_pos[1]):
        # print("U-D")
        if princess_pos[0] < curr_pos[0]:
            # posr-=1 
            return 'UP'
        # posr+=1
        return 'DOWN'
    else:
        # print("L-R")
        if princess_pos[1] < curr_pos[1]: 
            # posc-=1
            return 'LEFT'
        # posc+=1
        return 'RIGHT'

    
    return ""



# Tail starts here
def update_sim(board, move):
    pos = pos_letter('m', board)
    # print(pos)
    maxr, maxc = len(board), len(board[0])
    if move == 'DONE':
        if board[pos[0]][pos[1]] != 'mp': return 'ERROR'
        else:
            board[pos[0]][pos[1]] = 'm'
            return pos, board

    if move == 'RIGHT':
        if pos[1]+1>maxc: return 'ERROR'
        else:
            board[pos[0]][pos[1]+1] = 'm' + board[pos[0]][pos[1]+1]
            board[pos[0]][pos[1]] = '-'
            pos[1] +=1
            return pos, board

    if move == 'LEFT':
        if pos[1]-1<0: return 'ERROR'
        else:
            board[pos[0]][pos[1]-1] = 'm' + board[pos[0]][pos[1]-1]
            board[pos[0]][pos[1]] = '-'
            pos[1] -=1
            return pos, board
    
    if move == 'DOWN':
        if pos[0]+1>maxr: return 'ERROR'
        else:
            board[pos[0]+1][pos[1]] = 'm' + board[pos[0]+1][pos[1]]
            board[pos[0]][pos[1]] = '-'
            pos[0] +=1
            return pos, board

    if move == 'UP':
        if pos[0]-1<0: return 'ERROR'
        else:
            board[pos[0]-1][pos[1]] = 'm' + board[pos[0]-1][pos[1]]
            board[pos[0]][pos[1]] = '-'
            pos[0] -=1
            return pos, board



if __name__ == '__main__':
    n = int(input())
    r,c = [int(i) for i in input().strip().split()]
    grid1 = []
    for i in range(0, n):
        grid1.append(input())

    # print(grid1)
    grid = [[i for i in j] for j in grid1]

    while pos_letter('m',grid)!=pos_letter('p',grid):
        print("\n\n\n")
        print_board(grid)
        next_move = nextMove(n,r,c,grid)
        print(next_move)
        pos, grid = update_sim(grid, next_move)

