#Main Code here
# new branch test!
#importing libraries
# import numpy as np
#TEST
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

def computer_char(character):
    if character =='X':
          return 'O'
    elif character == 'O':
          return 'X'


#We can use this function for the computer to win or to block the opponent
def computer_move_row(row1, row2, row3, board, character, look_char):
  
    row_list = [row1, row2, row3]
    
    for row_num, row in enumerate(row_list):
        check_values = 0
        
        for i in range(2):
            if row[i] == character:
                check_values += 1
                
            if check_values == 2:
                #it will then put its character here in place of the dash or space
                
                for j in range(2):
                    if board[row_num][j] == ' ' or board[row_num][j] == '_':     board[row_num][j] == look_char
                        
            
def computer_move_col(col1, col2, col3, board, character, look_char):
    col_list = [col1, col2, col3]
    
    for col_num, col in enumerate(col_list):
        check_values = 0
        
        for i in range(2):
            if col[i] == character:
                check_values += 1
                
            if check_values == 2:
                for j in range(2):
                    if board[col_num][j] == ' ' or board[col_num][j] == '_':
                        board[col_num][j] == look_char
                        
                        
def computer_move_dia(dia1, dia2, board, character, look_char):
    dia_list = [dia1, dia2]
    
    for dia_num, dia in enumerate(dia_list):
        check_values = 0
        
        for i in range(2):
            if dia[i] == character:
                check_values += 1
                
            if check_values == 2:
                for j in range(2):
                    if board[dia_num][j] == ' ' or board[dia_num][j] == '_':
                        board[dia_num][j] == look_char


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
    character ='X'
    
    #Calls function and gets the random character X or O, and assigns it to the variable
    #character = random_char()
    
    player1 = True
    is_user = True
  
    #While the user want to play
    while game_on == True:
        
        
        
        print('\n'*100)
        print('\n\nWelcome to Tic Tac Toe!\nYou will be playing with a computer or with friend!\n')
        
        choice = input('Do you want to play with the computer? (Y/N): ')
        
        if choice == 'Y':
            computer_yes = True
            
        elif choice == 'N':
            computer_yes = False
            
        
        
        while computer_yes:
            print('\n'*100)

            row1 = board[0]
            row2 = board[1]
            row3 = board[2]
            
            col1 = [board[0][0], board[1][0], board[2][0]]
            col2 = [board[0][1], board[1][1], board[2][1]]
            col3 = [board[0][2], board[1][2], board[2][2]]
            
            dia1 = [board[0][0], board[1][1], board[2][2]]
            dia2 = [board[0][2], board[1][1], board[2][0]]
            
            print_board(board)
        
            
            
            
            #user
            if is_user == True:
                print("\nYour turn")
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
                    print('\nPlayer 1 won! Great Job\n')
                    break
                                           
                is_user == False
                
                
                
                
              #computer
            if is_user == False:
                print("It's the computer's turn")
                computer_move_row(row1, row2, row3, board, character, look_char)
                computer_move_row(row1, row2, row3, board, look_char, character)
                
                computer_move_col(col1,col2, col3, board, character, look_char)
                computer_move_col(col1,col2, col3, board, look_char, character)
                
                computer_move_dia(dia1, dia2, board, character, look_char)
                computer_move_dia(dia1, dia2, board, look_char, character)
                
                
                is_user == True
                
            
        if character == 'X':
                look_char = 'O'
        else:
            look_char == 'X'
                
        while computer_yes == False:
        
            row1 = board[0]
            row2 = board[1]
            row3 = board[2]
            
            col1 = [board[0][0], board[1][0], board[2][0]]
            col2 = [board[0][1], board[1][1], board[2][1]]
            col3 = [board[0][2], board[1][2], board[2][2]]
            
            dia1 = [board[0][0], board[1][1], board[2][2]]
            dia2 = [board[0][2], board[1][1], board[2][0]]
            
            print_board(board)
            
            if character_swap(player1):
                character = 'X'
                
            elif character_swap(player1)==False:
                character = 'O'
                
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
                        print('\nPlayer 2 won! Great Job\n')
                        break
             
             
             
        game_on = gameon()
                
                
        if game_on == True:
            print('Alright lets do it again\n')
            board = []
            make_board(board)
                        
        elif game_on == False:
            print('Thanks for playing!\n')
            break
            
                
            
        
    
    
        



if __name__ == "__main__":
    main()
