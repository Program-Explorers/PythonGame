#Main Code here
# new branch test!
#importing libraries
# import numpy as np
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
            
    else:
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
            
    else:
        return False

    
def diag_win(board, row, col ,character):
    if (row ==1 and col ==1)  or   (row ==2 and col ==2)  or  (row==3 and col==3):
        if board[0][0] == character and board[1][1]== character and board[2][2] == character:
            return True
            
    elif (row==3 and col==1)  or  (row==2 and col==2)  or  (row==1 and col==3):
        if board[2][0] == character and board[1][1] ==character and board[0][2]:
            return True
            
    else:
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
   
def character_swap(player1):
    if player1:
        return True
    
    return False


def main():
    board = []
    make_board(board)
    game_on = True

    #Calls function and gets the random character X or O, and assigns it to the variable
    #character = random_char()
    
    player1 = True
    
    
    #While the user want to play
    while game_on == True:
        if character_swap(player1):
            character = 'X'
            
        elif character_swap(player1)==False:
            character = 'O'
        
        
        print('\n'*100)
        print('\n\nWelcome to Tic Tac Toe!\nYou will be playing with a computer or with friend!\n')
        print_board(board)

        if player1:
            print("\nPlayer 1's turn")
            player1 = False
            #Gathers input for row and column
            input_col = user_choice_col(character)
    
            input_row = user_choice_row(character)
        
       
            if input_row not in range(1,4) or input_col not in range(1,4):
                print('\n  OOPS, thats not on the board')
            
            elif board[input_row-1][input_col-1]==character:
                print('\n  You have guessed that already')
                
            else:
                board[input_row-1][input_col-1] = character
            
                won_row = row_win(board, input_row, character)
                won_col = col_win(board, input_col, character)
                won_diag = diag_win(board, input_row, input_col, character)
            
                if won_row==True or won_col == True or won_diag ==True:
                    print('\n'*100)
                    print_board(board)
                    
                    if player1 == False:
                        print('\nPlayer 1 won! Great Job\n')
                        
                        
                    else:
                        print('\nPlayer 2 won! Great Job\n')
                        
                    game_on = gameon()
                
                    if game_on == True:
                        print('Alright lets do it again\n')
                        board = []
                        make_board(board)
                        
                    elif game_on == False:
                        print('Thanks for playing!\n')
                        break

        elif player1 == False:
            print("\nPlayer 2's turn")
            player1 = True
            #Gathers input for row and column
            input_col = user_choice_col(character)
            
            input_row = user_choice_row(character)
                
               
            if input_row not in range(1,4) or input_col not in range(1,4):
                print('\n  OOPS, thats not on the board')
                    
            elif board[input_row-1][input_col-1]==character:
                print('\n  You have guessed that already')
                        
            else:
                board[input_row-1][input_col-1] = character
                
                won_row = row_win(board, input_row, character)
                won_col = col_win(board, input_col, character)
                won_diag = diag_win(board, input_row, input_col, character)
                    
                if won_row==True or won_col == True or won_diag ==True:
                    print('\n'*100)
                    print_board(board)
                        
                    if player1 == False:
                        print('\nPlayer 1 won! Great Job\n')
                            
                            
                    else:
                        print('\nPlayer 2 won! Great Job\n')
                        
                    game_on = gameon()
                
                    if game_on == True:
                        print('Alright lets do it again\n')
                        board = []
                        make_board(board)
                        
                    elif game_on == False:
                        print('Thanks for playing!\n')
                        break
                        
                    if game_on == True:
                        print('Alright lets do it again\n')
                        board = []
                        make_board(board)
                                
                    elif game_on == False:
                        print('Thanks for playing!\n')
                        break
            
                
                        
            
    
        
    
    
        



if __name__ == "__main__":
    main()