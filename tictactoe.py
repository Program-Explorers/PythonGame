#Main Code here

#importing libraries
import random


#functions

#Creates a board

def make_board(bard):
    for x in range(0, 3):
        bard.append(["_"] * 3)
    bard[2][0]=bard[2][1]=bard[2][2] = " "

def print_board(board):
  for row in board:
    print('|'.join(row))


#decides randomly which player goes first
def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'
        
#Ask for user_input and validate it
def user_choice_row(char):
    choice_row = 'WRONG'
    
    while choice_row.isdigit() == False:
    
        choice_row = input(f"Type in the ROW you would like to place your '{char}': ")
        
        if choice_row.isdigit() == False:
            print('Sorry that is not a valid number. Please type a number from 1 and 3')
            
    return int(choice_row)
    

def user_choice_col(char):
    choice_col = 'NOPE'
    
    while choice_col.isdigit() == False:
        
        choice_col = input(f"\nType in the COLUMN you would like to place your '{char}': ")
        
        if choice_col.isdigit() == False:
            print('Sorry that is not a valid number. Please type a number from 1 and 3')
            
    return int(choice_col)
    
    


#checks if the user won by a row

def row_win(board, row, character):
    if row == 1:
        if board[0][0] == character and board[0][1] == character and board[0][2] == character:
            return True
            
    elif row == 2:
        if board[1][0] == character and board[1][1] == character and board[1][2] == character:
            return True
            
    elif row == 3:
        if board[2][0] == character and board[2][1] == character and board[2][2] == character:
            return True
            

    return False
        
        
def col_win(board, col, character):
    
    if col == 1:
        if board[0][0] == character and board[1][0] == character and board[2][0] == character:
            return True
            
    elif col ==2:
        if board[0][1] == character and board[1][1] == character and board[2][1] == character:
            return True
            
    elif col ==3:
        if board[0][2] == character and board[1][2] == character and board[2][2] == character:
            return True
            
    
    return False

    
def diag_win(board, row, col ,character):
    if (row ==1 and col ==1)  or   (row ==2 and col ==2)  or  (row==3 and col==3):
        if board[0][0] == character and board[1][1]== character and board[2][2] == character:
            return True
            
    elif (row==3 and col==1)  or  (row==2 and col==2)  or  (row==1 and col==3):
        if board[2][0] == character and board[1][1] ==character and board[0][2]:
            return True
            
    return False
    

def random_char():
    result = random.randint(1,2)
    character = 'default'
    if result == 1:
        print('\nYou are X!\n')
        character = 'X'
        
    elif result == 2:
        print('\nYou are O!\n')
        character = 'O'
        
    else:
        print('Error in choosing your character XO')
    return character
   
# Checks if user wants to play again
def gameon():
    again = 'wrong'
    chosen = False
    acceptable_values = ['Y', 'N']
    
    while again not in acceptable_values:
        again = input('Would you like to play again? (Y/N) ')
        
        if again not in acceptable_values:
            print('Please type Y or N')
            
        elif again in acceptable_values:
            chosen = True
    
    return chosen
    

def main():
    board = []
    make_board(board)
    game_on = True

    #Calls function and gets the random character X or O, and assigns it to the variable
    character = random_char()
    print('\n\nWelcome to Tic Tac Toe!\nYou will be playing with a computer!\n')
    #Prints out which player is going first
    turn = whoGoesFirst()
    #While the user want to play
    while game_on == True:
        
        

        print('\n' + turn)
        
        print_board(board)

        #Gathers input for row and column
        if  turn == 'Player 1':
            character = 'X'
        else:
            character = 'O'
        input_col = user_choice_col(character)
    
        input_row = user_choice_row(character)
        
        print("[pick char")
        if input_row not in range(1,4) or input_col not in range(1,4):
            print('\n  OOPS, thats not on the board')
            
        elif board[input_row-1][input_col-1]==character:
            print('\n  You have guessed that already')
                
        else:
            board[input_row-1][input_col-1] = character
            won_row = row_win(board, input_row, character)
            won_col = col_win(board, input_col, character)
            won_diag = diag_win(board, input_row, input_col, character)
            print(won_row, won_col,won_diag)
            print("iffff")
            if won_row==False and won_col == False and won_diag ==False:
                print('\n'*100)
                print_board(board)
                if turn == 'Player 1':
                  # Player1's turn.
                    print_board(board)
                    position = player_choice(board)
                    place_marker(board, player1_marker, position)

                    if win_check(theBoard, player1_marker):
                         print_board(board)
                         print('Congratulations! You have won the game!')
                         game_on = False
                    else:
                        if full_board_check(board):
                            print_board(board)
                            print('The game is a draw!')
                            break
                        else:
                            print("SWITCH")
                            turn = 'Player 2'

                else:
                    # Player2's turn.
                    print("p2!")
                    print_board(board)
                    position = player_choice(board)
                    place_marker(board, player2_marker, position)
                    print("here")
                    if win_check(theBoard, player2_marker):
                        print_board(board)
                        print ('Player 2 has won!')
                        game_on = False
                    else:
                        print("ere")
                        if full_board_check(board):
                            print_board(board)
                            print ('The game is a tie!')
                            break
                        else:
                            print("SWITCH")
                            turn = 'Player 1'
                            game_on = gameon()
                print('\n'*100)
                if game_on == True:
                    print('Alright lets do it again\n')
                    board = []
                    make_board(board)
    
                    
                
                elif game_on == False:
                    print('Thanks for playing!\n')
                    break

            
                
                        
            
    
        
    
    
        



if __name__ == "__main__":
    main()
