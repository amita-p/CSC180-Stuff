"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Authors: Michael Guerzhoy.  Last modified: Nov. 3, 2015
"""


'''Return a boolean value. True is the board is empty, False if not. Take in a
2D list called board.'''
def is_empty(board):
    for i in board: #go through every row in the board
        for k in i: #go through every column in the row
            if (k!=" "): 
                return False #return False if the element is not empty
    return True 

'''Return a boolean value. True is the board is full, False if not. Take in a
2D list called board.'''
def is_full(board):
    for i in board: #go through every row in the board
        for k in i: #go through every column in the row
            if (k==" "):
                return False #return False if the element is empty
    return True
    
    
'''Take in a 2D list called board, two indicies, y_end and x_end which specify
the row index and column index respectively, length of a sequence of colours,
and the direction which the sequence follows from its starting index, specified
by d_y and d_x for the y and x directions respectively. Return OPEN if the
sequence is open, CLOSED if the sequence is closed, and SEMIOPEN if the sequence
is semiopen. '''
def is_bounded(board, y_end, x_end, length, d_y, d_x):
    #boolean variable to keep track of whether side 1 (starting side) is blocked
    side_1_blocked=False 
    #boolean variable to keep track of whether side 2 is blocked
    side_2_blocked=False  
    #index right beside side 1 in the direction of the sequence 
    side_1_x=x_end-d_x*length 
    side_1_y=y_end-d_y*length
    #index right beside side 2 in the direction of the sequence
    side_2_x=x_end+d_x
    side_2_y=y_end+d_y
    #side 1 and 2 are blocked (cannot put anything there) if they are not on the board
    #or if something is already there
    if (side_1_x>=len(board[0]) or side_1_y>=len(board) or side_1_x<0 or side_1_y<0 or board[side_1_y][side_1_x]!=" "):
        side_1_blocked=True
    if (side_2_x>=len(board[0]) or side_2_y>=len(board) or side_2_x<0 or side_2_y<0 or board[side_2_y][side_2_x]!=" "):
        side_2_blocked=True
    #if both sides are blocked, the sequence is closed, return CLOSED
    if (side_1_blocked==True and side_2_blocked==True):
        return "CLOSED"
    #if both sides are not blocked, the sequence is open, return OPEN
    elif (side_1_blocked==False and side_2_blocked==False):
        return "OPEN"
    #otherwise, the sequence must be semiopen, return SEMIOPEN
    else:
        return "SEMIOPEN"
        
        
'''Return the number of (int) open and semiopen sequences of colour col in a 
sequence of squares on the board as a tuple. Take in a board, the starting index
of the sequence, y_start and x_start, the length of the sequence of colours,
and the direction of the sequence.'''
def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    if (length==0):
        return 0,0
    y=y_start
    x=x_start
    seq_length=0
    semi_open_seq_count=0
    open_seq_count=0
    end_of_board_reached=False
    actual_seq=0
    while (end_of_board_reached==False):       
        if (board[y][x]==col):
            seq_length+=1
        if (board[y][x]!=col):
            if (seq_length==length):
                if (is_bounded(board,y-d_y,x-d_x,length,d_y,d_x)=="OPEN"):
                    open_seq_count+=1
                elif (is_bounded(board,y-d_y,x-d_x,length,d_y, d_x)=="SEMIOPEN"):
                    semi_open_seq_count+=1
            seq_length=0
        y+=d_y
        x+=d_x
        if (y>=len(board) or x>=len(board) or y<0 or x<0):
            end_of_board_reached=True
            
    if (seq_length==length):
        if (is_bounded(board,y-d_y,x-d_x,length,d_y,d_x)=="OPEN"):
            open_seq_count+=1
        elif (is_bounded(board,y-d_y,x-d_x,length,d_y, d_x)=="SEMIOPEN"):
            semi_open_seq_count+=1           
    return open_seq_count, semi_open_seq_count

'''Return if a sequence of 5 of the colour col exists'''
def detect_5_row(board, col, y_start, x_start, d_y, d_x):
    y=y_start
    x=x_start
    seq_length=0
    end_of_board_reached=False
    while (end_of_board_reached==False):
        if (board[y][x]==col):
            seq_length+=1
        else:
            if (seq_length>=5):
                return True
            seq_length=0
        y+=d_y
        x+=d_x
        if (y>=len(board) or x>=len(board)):
            end_of_board_reached=True
    if (seq_length>=5):
        return True
    return False
            
                
'''Return if sequence of 5 of color col exists in entire board'''
def detect_5_rows(board, col):
    open_seq_count, semi_open_seq_count = 0, 0
    i=0
    while (i<len(board)):
        if (detect_5_row(board,col,0,i,1,0)==True):
            return True
        if (detect_5_row(board,col,i,0,0,1)==True):
            return True
            
        if (detect_5_row(board,col,i,0,1,1)==True):
            return True
        if (detect_5_row(board,col,0,i,1,1)==True):
            return True
            
        if (detect_5_row(board,col,0,i,1,-1)==True):
            return True
        if (detect_5_row(board,col,i,len(board)-1,1,-1)==True):
            return True
        i+=1
    return False
        
       
    

    
    
    
def detect_rows(board, col, length):
    
    open_seq_count, semi_open_seq_count = 0, 0
    i=0
    while (i<len(board)):
        open_seq_count+=detect_row(board,col,i,0,length,0,1)[0]
        semi_open_seq_count+=detect_row(board,col,i,0,length,0,1)[1]
        open_seq_count+=detect_row(board,col,0,i,length,1,0)[0]
        semi_open_seq_count+=detect_row(board,col,0,i,length,1,0)[1]
        
        
        open_seq_count+=detect_row(board,col,0,i,length,1,1)[0]
        semi_open_seq_count+=detect_row(board,col,0,i,length,1,1)[1]
        if (i!=0):
            open_seq_count+=detect_row(board,col,i,0,length,1,1)[0]
            semi_open_seq_count+=detect_row(board,col,i,0,length,1,1)[1]
            
            
        open_seq_count+=detect_row(board,col,0,i,length,1,-1)[0]
        semi_open_seq_count+=detect_row(board,col,0,i,length,1,-1)[1]
        if (i!=0):
            open_seq_count+=detect_row(board,col,i,len(board)-1,length,1,-1)[0]
            semi_open_seq_count+=detect_row(board,col,i,len(board)-1,length,1,-1)[1]
        i+=1
            

    return open_seq_count, semi_open_seq_count

    

    
def search_max(board):
    i=0
    k=0
    max_score=0
    y=0
    x=0
    for i in range (len(board)):
        for k in range (len(board)):
            if (board[i][k]==" "):
                board[i][k]="b"
                if (score(board)>max_score):
                    y=i
                    x=k
                    max_score=score(board)
                board[i][k]=" "
    return y,x
            
                
        
        
    return move_y, move_x
    
def score(board):
    MAX_SCORE = 100000
    
    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}
    
    for i in range(2, 7):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)
        
    
    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE
    
    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE
        
    return (-10000 * (open_w[4] + semi_open_w[4])+ 
            500  * open_b[4]                     + 
            50   * semi_open_b[4]                + 
            -100  * open_w[3]                    + 
            -30   * semi_open_w[3]               + 
            50   * open_b[3]                     + 
            10   * semi_open_b[3]                +  
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])

    
def is_win(board):
    if (detect_5_rows(board,"b")):
        return "Black won"
    elif (detect_5_rows(board,"w")):
        return "White won"
    elif  (is_full(board)):
        return "Draw"
    else:
        return "Continue playing"


def print_board(board):
    s = "*"
    for i in range(len(board[0])):
        s += str(i%10)
    s += "*\n"
    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])):
            s += str(board[i][j])
    
        s += "*\n"
    s += (len(board[0])+2)*"*"
    print(s)
    

def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board
                


def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))
        
    
    

        
    
def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])
    
    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)
            
        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
            
            
        
        
        
        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
        
            
            
def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col        
        y += d_y
        x += d_x
        
def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    
    y = 3; x = 5; d_x = -1; d_y = 1; length = 2
    
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #     
    
    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);
    
    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #        
    #        
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0


  
            
if __name__ == '__main__':

    board=make_empty_board(8)
    board[5][1], board[1][5],board[2][4], board[3][3], board[4][2]="w","w","w","w","w"
    board[4][1], board[0][5],board[1][4], board[2][3], board[3][2]="w","w","w","w","w"
    board[0][0],board[1][1],board[2][2]="w","w","w"
    print_board(board)
    print(detect_rows(board, "w", 3))
    print (detect_5_rows(board,"w"))
    some_tests()

    

    
    
    