#!/usr/bin/python

# Head ends here
def check_dirty(board):
    dirty = [(i,j)  for i in range(len(board)) for j in range(len(board[i])) if 'd' in board[i][j][0]]
    return dirty

def print_board(board):
    print("\n".join([" ".join(i) for i in board]))

def next_move(posr, posc, board):
    if 'd' in board[posr][posc]:
        return 'CLEAN', [posr, posc]

    def unneg(x):
        if x<0: return -1*x
        return x

    def manhattan(x1,y1,x2,y2):
        return unneg(x2-x1) + unneg(y2-y1)

    dirty = check_dirty(board)
    min_dirty = [dirty[0], manhattan(posr,posc,dirty[0][0],dirty[0][1])]
    for dirt in dirty[1:]:
        dist = manhattan(posr,posc,dirt[0],dirt[1])
        if dist < min_dirty[1]:
            min_dirty = [dirt, dist]

    the_dirty = min_dirty[0]
    print(min_dirty)
    print(unneg(the_dirty[0]-posr), unneg(the_dirty[1] - posc))
    if unneg(the_dirty[0]-posr) > unneg(the_dirty[1] - posc):
        print("U-D")
        if the_dirty[0]<posr:
            # posr-=1 
            return 'UP', [posr, posc]
        # posr+=1
        return 'DOWN', [posr, posc]
    else:
        print("L-R")
        if the_dirty[1]<posc: 
            # posc-=1
            return 'LEFT', [posr, posc]
        # posc+=1
        return 'RIGHT', [posr, posc]


    print("")

# Tail starts here
def update_sim(board, pos, move):
    maxr, maxc = len(board), len(board[0])
    if move == 'CLEAN':
        if board[pos[0]][pos[1]] != 'bd': return 'ERROR'
        else:
            board[pos[0]][pos[1]] = 'b'
            return pos, board

    if move == 'RIGHT':
        if pos[1]+1>maxc: return 'ERROR'
        else:
            board[pos[0]][pos[1]+1] = 'b' + board[pos[0]][pos[1]+1]
            board[pos[0]][pos[1]] = '-'
            pos[1] +=1
            return pos, board

    if move == 'LEFT':
        if pos[1]-1<0: return 'ERROR'
        else:
            board[pos[0]][pos[1]-1] = 'b' + board[pos[0]][pos[1]-1]
            board[pos[0]][pos[1]] = '-'
            pos[1] -=1
            return pos, board
    
    if move == 'DOWN':
        if pos[0]+1>maxr: return 'ERROR'
        else:
            board[pos[0]+1][pos[1]] = 'b' + board[pos[0]+1][pos[1]]
            board[pos[0]][pos[1]] = '-'
            pos[0] +=1
            return pos, board

    if move == 'UP':
        if pos[0]-1<0: return 'ERROR'
        else:
            board[pos[0]-1][pos[1]] = 'b' + board[pos[0]-1][pos[1]]
            board[pos[0]][pos[1]] = '-'
            pos[0] -=1
            return pos, board

    
    

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    while len(check_dirty(board))!=0:
        print("\n\n\n")
        n_move, curr_pos = next_move(pos[0], pos[1], board)

        print(n_move)
        pos, board = update_sim(board, curr_pos, n_move)

        print_board(board)
