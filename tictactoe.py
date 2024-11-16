#from IPython.display import clear_output

#Displaying the board 
def display_board(board):
    for row in board:
        print(f" {row[0]} | {row[1]} | {row[2]} ")
        print("---|---|--- ")
        
#Handling player's input & turns 
def player_input():
    while True:
        marker =  input("Please pick a marker 'X' or 'O'").upper()
        if marker == 'X' or 'O':
            return marker
        else:
            print("Invalid marker, please enter 'X' or 'O'")

#Handle player's marker on the board
def place_marker(board,marker,position):
    #Convert position (1-9) to row and column 
    row = (position - 1) // 3 
    col = (position - 1) % 3 
    
    # [(0,1), (0,2), (0,3)], 
    # [(1,0), (1,1), (1,2)],
    # [(2,0), (2,1), (2,2)]
    
    if(board[row][col] == " "):
        board[row][col] = marker 
    else: 
        print("Choose another position, this position is already taken")

#Check to see who win or a tie 
def win_check(board,mark):
    if(board[row[0]] ):
        return true
    elif(): 
        
    
print("Welcome To The Tic Tac Toe Game!")
board = [
    [" ", " ", " "], 
    [" ", " ", " "],
    [" ", " ", " "]
    ]
display_board(board);


turn = 0
player = 0
while turn != 8:
    print(f"It's player's {player + 1} turn")
    player += 1 
    marker = player_input()
    position = int(input("Please enter your position from 1 - 9 "))
    place_marker(board,marker,position)
    display_board(board);
    if(player >= 2):
        player = 0
    turn += 1
    










