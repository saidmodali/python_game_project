"""
Author: Said Modali
Project Title: Word Puzzle Game

Description:
To understand how the game operates and the rules for playing, please refer to the ReadMe PDF file.

It contains step-by-step instructions, explanations of game mechanics,
and any additional information necessary for a complete understanding of the project.

All Rights reserved...
"""

def read_file(filename="test_puzzle.txt"):
    with open("{}".format(filename),"r") as w_and_n:
        all_list = []
        content = w_and_n.read()
        e_str = ""
        for words in content:
            if words != "\n":
                e_str += words
            else:
                all_list.append(e_str)
                e_str = ""
                continue
        all_list.append(e_str)
        word_list = []
        number_list = []
        for i in all_list:
            if i != "":
                word_list.append(i)
            else:
                break
        for i in all_list[len(word_list) + 1 : ]:
                    number_list.append(i)
    return (word_list,number_list)

def check_consistency(board):
    k = 1
    for i in board[0:-1 ] :
        if len(i) == len(board[k]):
            k +=1
            continue
        else :
            return False
    return True

def create_board(board):
    empty_list = []
    empty_list2 = []
    for i in board :
        for k in i:
            empty_list += [int(k)]
        empty_list2 += [empty_list]
        empty_list = []
    board.clear()
    for i in empty_list2:
        board.append(i)
    return None
    

    
def identifier(words):
    empty_list = []
    for i in words:
        empty_list.append(False)
    return empty_list



def print_board(board):
    for i in board:
        for k in i:
            if k == 1:
                print(" ",end = "")
            if type(k) == str:
                print("{}".format(k),end = "")
            if k == 0 :
                print("+",end="")
        print("\n",end = "")
    return None


def print_board_w_c(board):
    number_of_rows = len(board)
    number_of_columns = len(board[0])
    print("  ",end = "")
    for i in range(1,number_of_columns + 1):
        if i == number_of_columns:
            print("C{}".format(i),end = "")
            break
        print("C{}".format(i),end = " ")
    print("\n",end = "")
    jumping = 1
    for k in board:
            print("R{}".format(jumping),end = " ")
            for c in k:
                if c == 1 :
                    print(" ",end = "  ")
                if type(c) == str:
                    print("{}".format(c),end = "  ")
                    
                if c == 0 :
                    print("+",end = "  ")
            print("\n",end = "")
            jumping += 1
    return None


def print_wordlist(words,wstatus):
    max = 0
    
    for i in words:
        if len(i) > max:
            max = len(i)
        
    print("Word List",max*" ","Status",sep = "")
    for i in range(1,len(words)+1):
        if wstatus[i-1] == True:
            print("W{}".format(i),"{}".format(words[i-1]),abs((9+max)-(5+len(words[i-1])))*" ","USED")
        else:
            print("W{}".format(i),"{}".format(words[i-1]),abs((9+max)-(5+len(words[i-1])))*" ","NOT USED")
    return None

def check_entries(coordinates,wordno,board,words):
    valid1 = False
    valid2 = False
    if len(board) >= coordinates[0] and coordinates[0] > 0:
        if len(board[0]) >= coordinates[1] and coordinates[1] > 0:
            valid1 = True
    if len(words) >= wordno and wordno > 0 :
        valid2 = True
    return (valid1,valid2)

def check_location(board,words,coordinates,wordno,direction='H'):
    row_coordinates = coordinates[0]
    column_coordinates = coordinates[1]
    totalnum_row = len(board)
    totalnum_column = len(board[0])
    totaldig_words = len(words[wordno -1 ])
    if board[row_coordinates - 1][column_coordinates - 1] == 0:
        return (False,1)
    if row_coordinates - 2 >= 0 :
        if direction == "V" and board[row_coordinates - 2][column_coordinates - 1] != 0:
            return (False,2)
    if column_coordinates - 2 >= 0:
        if direction == "H" and board[row_coordinates - 1][column_coordinates - 2 ] != 0:
            return (False,3)
    try:
        
        if direction == "H" and not((totalnum_column >= (column_coordinates +totaldig_words -1)) and  (totalnum_row >= row_coordinates)):
            return (False,4)
        if direction == "V" and not((totalnum_column >= column_coordinates) and (totalnum_row >= (row_coordinates + totaldig_words-2))):
            return (False,7)
    except IndexError:
        pass
    a = 0
    try:
        if direction == "H":
            for i in range(column_coordinates,column_coordinates + totaldig_words ):
                if board[row_coordinates - 1][i-1] == 0 :                              
                    return (False,5) #!
                if board[row_coordinates - 1][i-1] != words[wordno -1][a] :
                    if board[row_coordinates - 1][i-1] == 1:
                        pass
                    else:
                        return (False,5)
                a += 1
        b = 0
        if direction == "V":
            for i in range(row_coordinates,row_coordinates + totaldig_words ):
                if board[i -1][column_coordinates - 1] == 0  :
                    return (False,8) #!
                if board[i -1][column_coordinates - 1] != words[wordno -1][b]:
                    if board[i -1][column_coordinates - 1] == 1:
                        pass
                    else:
                        return (False,8)     
                b += 1
    except IndexError:
        pass
    try:
        if direction == "H":
            if board[row_coordinates - 1][column_coordinates + totaldig_words - 1] != 0:
                return (False,6)   
        if direction == "V":
            if board[row_coordinates + totaldig_words - 1][column_coordinates - 1] !=0:
                return (False,9)
    except IndexError:
        pass
    return (True,0)

def check_word_fits(board,words,coordinates,wordno,direction='H'):
    row_coordinates = coordinates[0]  ## reel
    column_coordinates = coordinates[1] ## real
    totaldig_words = len(words[wordno -1 ]) ## real
    count = 0  ##word index
    ## for horizontal dimension
    try :
        if direction == "H":
            for i in range(column_coordinates,column_coordinates + totaldig_words):
                if board[row_coordinates - 1][i -1] == words[wordno -1 ][count] or board[row_coordinates - 1][i -1] == 1:
                    count += 1
                else:
                    return (False,2)
        ## for vertical dimension
        if direction == "V":
            for i in range(row_coordinates,row_coordinates + totaldig_words):
                if board[(row_coordinates - 1) + count ][column_coordinates -1] == 1  or board[(row_coordinates - 1) + count ][column_coordinates -1] == words[wordno -1 ][count]:
                    count += 1
                else:
                    return (False,1)
    except IndexError:
        pass
    return (True,0)

def clear_board(board,wstatus) :
    copy_board = board[:]
    num_row = 0
    num_column = 0
    board_row_n = 0
    for i in board:
        num_row += 1
    for i in board[0]:
            num_column += 1
    board.clear()
    for i in range(num_row):
        board.append([])
        board_row_n += 1
        for k in range(num_column):
            if copy_board[board_row_n- 1][k] != 0:
                board[board_row_n - 1].append(1)
            else:
                board[board_row_n - 1].append(0)
    copy_wstatus = wstatus[:]
    wstatus.clear()
    for i in copy_wstatus:
        wstatus.append(False)
    return None

def decompose_command(str1):
    str1 = str1.upper()    ##     W 1 R 2 C 4 D V
    asci_list = []
    for i in str1:
        asci_list.append(ord(i))
    #### control according to format
    for i in asci_list:
        if (i >= 48 and i <= 57) or (i>=65 and i<=90):
            pass
        else:
            return (-1,None,None,None)
    if (asci_list[0] >= 48) and (asci_list[0] <= 57):
        return (-1,None,None,None)
    
    if (len(str1) >= 8)  and len(str1) <= 11 :
        pass
    else:
        return (-1,None,None,None)
    #### control is finished
    ### giving commands
    
    ### finding dimension
    dimension = []
    d_flag  = 0                                       
    for i in asci_list:                                     
        if d_flag == 1 :                                  
            dimension.append(i)                          
            break                                                        
        if i == 68:                                                                
            d_flag = 1
                
    if dimension[0] == 86:
        pass
    else: 
        dimension [0]= 72           
    ### dimension done
    ##finding wordno
    word_no  = []
    w_index = 0
    w_flag = 0
    for i in asci_list:
        if i == 87:
            w_index = asci_list.index(i)
            break
    for i in asci_list[w_index + 1 :]:
        w_flag += 1
        if i >= 48 and i <= 57:
            word_no.append(i)
        if w_flag == 2:
            break
    ##wordno is finished
    column_no = []
    col_index = 0
    col_flag = 0
    for i in asci_list:
        if i == 67:
            col_index = asci_list.index(i)
            break
    for i in asci_list[col_index + 1 : ]:
        col_flag +=1
        if i >= 48 and i <= 57:
            column_no.append(i)
        if col_flag == 2:
            break
    ##columno is finished
    row_no = []
    row_index = 0
    row_flag = 0
    for i in asci_list:
        if i == 82:
            row_index = asci_list.index(i)
            break
    for i in asci_list[row_index + 1 : ]:
        row_flag += 1
        if i >= 48 and i <= 57:
            row_no.append(i)
        if row_flag == 2:
            break
    ##rowno is done
    
    ## escape from asciilist to charlist !!!! one by one
    word_no2 = []
    for i in word_no:
        word_no2.append(chr(i))
    column_no2 = []
    for i in column_no:
        column_no2.append(chr(i))
    row_no2 = []
    for i in row_no:
        row_no2.append(chr(i))
    dimension2 = []
    for i in dimension:
        dimension2.append(chr(i))
    ## is done
    
    ## finally
    word_no3 = ""
    for i in word_no2:
        word_no3 += "{}".format(i)
    word_no3 = int(word_no3)  ## it is wordnumber
    
    row_no3 = ""
    for i in row_no2:
        row_no3 += "{}".format(i)
    row_no3 = int(row_no3)      ## it is rownumber
    
    column_no3 = ""
    for i in column_no2:
        column_no3 += "{}".format(i)
    column_no3 = int(column_no3) ## it is columnumber..
    
    dimension3 = dimension2[0]
    
    return (0,word_no3,[row_no3,column_no3],dimension3)
    ####finishhhhhhhhhh
    
def word_it(board,words,wstatus,coordinates,wordno,direction):
    ##control is available?
    if check_location(board,words,coordinates,wordno,direction)[0] :
        if check_word_fits(board,words,coordinates,wordno,direction)[0]:
            if wstatus[wordno -1] == False:
                pass
            else:
                return False
        else:
            return False
    else:
        return False
    ### yes it is available
    ##change board according to word:
    row_coordinates = coordinates[0]
    column_coordinates = coordinates[1]
    the_word = words[wordno -1]
    len_word = len(the_word)
    try:
        if direction =="H":
            for i in range(0,column_coordinates+ len_word ):
                board[row_coordinates-1][column_coordinates -1 + i] = words[wordno -1 ][i]
    except IndexError:
        pass
    
    try:
        if direction == "V":
            for i in range(0,row_coordinates+len_word):
                board[row_coordinates - 1 + i][column_coordinates - 1] = words[wordno -1][i]
    except IndexError:
        pass
    ## it is changed
    ## changing wstatus
    wstatus[wordno-1] = True
    
    ##finally
    return True

def copy_board(board):
    copp = [c[:] for c in board]
    return copp

def track_move(mvn,trackboard,coordinates,wordno,direction,board,wstatus):
    w_copy = wstatus[:]
    mvn += 1
    trackboard.append((coordinates,wordno,direction,copy_board(board),w_copy))
    return mvn

def check_solved(board):
    empty_list = []
    
    for i in board:
        for k in i :
            empty_list.append(k)
    
    if 1 in empty_list:
        return False
    else:
        return True
    
def solve_board(board,words):
    if len(words) % 2  == 0:
        return True
    else:
        return False
    
def word_puzzle():
    print("Game starts")
    while True:
        print("Enter the file name (default=sample_puzzle.txt):")
        a = input()
        if a == "":
            a = "sample_puzzle.txt"
        wordlistm,boardm = read_file(a)
        if check_consistency(boardm) == True:
            break
        else:
            print("The puzzle board of {} is not consistent!".format(a))
            print("Do you want to try a new file?")
            print("y:yes, n:yo")
            y_n = input()
            y_n = y_n.upper()
            if y_n == "Y":
                continue
            else:
                print("GAME OVER")
                return None
    create_board(boardm)
    wstatusm = identifier(wordlistm)
    while True:
        print_wordlist(wordlistm,wstatusm)
        print_board_w_c(boardm)
        
        print("Please choose a word from word list,")
        print("choose a row and a column, and")
        print("direction of the word, V: Vertical H:Horizontal")
        print("enter your move as in the format: (WXRYCZDT)")
        print("Other options:")
        print(" cb - clear board")
        print(" q - quit game")
        print(" s - solve puzzle")
        user_input = input().upper()
        if user_input == "Q":
            print("GAME OVER")
            return None
        elif user_input == "CB":
            print("Restarting the game!")
            clear_board(boardm,wstatusm)
            continue
        elif user_input == "S":
            if solve_board(boardm,wordlistm) == True:
                print("SORRYYY!!! THAT WAS DIFFICULT.")
                print("GAME OVER")
                return None
                
            else:
                print("ERROR")
                print("GAME OVER")
                return None
        else:
        
            if decompose_command(user_input) == (-1,None,None,None):
                print_wordlist(wordlistm,wstatusm)
                print_board_w_c(boardm)
                print("YOUR ENTRY İS WRONG")
                print("Do you want to try a new move?")
                print("yes:y no:n")
                input10 = input().upper()
                if input10 =="Y":
                    continue
                else:
                    print("GAME OVER")
                    return None
            dumpy,wordnom,rowcolnom,dimensionm = decompose_command(user_input)
            if check_entries(rowcolnom,wordnom,boardm,wordlistm) == (False,False):
                print_wordlist(wordlistm,wstatusm)
                print_board_w_c(boardm)
                print("CHECK_ENTRİES ERROR..")
                print("Do you want to try a new move?")
                print("yes:y no:n")
                input11 = input().upper()
                if input11 =="Y":
                    continue
                else:
                    print("GAME OVER")
                    return None
        
            if check_location(boardm,wordlistm,rowcolnom,wordnom,dimensionm)[0] == False:
                print("CHECK_LOCATİON ERROR..")
                print("Do you want to try a new move?")
                print("yes:y no:n")
                input12 = input().upper()
                if input12 =="Y":
                    continue
                else:
                    print("GAME OVER")
                    return None
                
            if check_word_fits(boardm,wordlistm,rowcolnom,wordnom,dimensionm)[0] == False:
                print_wordlist(wordlistm,wstatusm)
                print_board_w_c(boardm)
                print("CHECK_WORD_FİTS ERRORR..")
                print("Do you want to try a new move?")
                print("yes:y no:n")
                input11 = input().upper()
                if input11 =="Y":
                    continue
                else:
                    print("GAME OVER")
                    return None
            word_it(boardm,wordlistm,wstatusm,rowcolnom,wordnom,dimensionm)
            if check_solved(boardm) == True:
                print("Congratulations!!!")
                print("PUZZLE SOLVED")
                print_wordlist(wordlistm,wstatusm)
                print_board_w_c(boardm)
                print("Would you like to play again?")
                print("y:yes n:no")
                input40 = input().upper()
                if input40 == "Y":
                    word_puzzle()
                else:
                    print("GAME OVER...")
                    return None

                
#start 
word_puzzle()

                    





































































            

    
    
   
            
     



    
    
    
    
    
    





    
    
            

        
                                        
            
        
        



    




                
             
             
        
         




    
                
                
                
            
            
    
        














    
    
    
        






        
        

    
                

            
            
        
    
        




            
            
                



