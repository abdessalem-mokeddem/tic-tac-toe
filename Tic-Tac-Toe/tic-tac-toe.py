

board = ["-", "-", "-",
    "-", "-", "-",
        "-", "-", "-"]
joueuractuel = "X"
gagnant = None
jeuxencours = True
stope_game = False


def printboard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])


def playerinput(board):
    inp =int(input("Veuillez entrer un nombre de 1-9: "))
    if inp >= 1 and inp <=9 and board[inp-1] == "-":
        board[inp-1] = joueuractuel
    else:
        print("Un joueur est déja en position ici!")
        


def checkHorizontale(board):
    global gagnant
    if board[0] == board[1] == board[2] and board[1] != "-":
        gagnant = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        gagnant = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True


def checkverticale(board):
    global gagnant
    if board[0] == board[3] == board[6] and board[0] != "-":
        gagnant = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        gagnant = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[0] != "-":
        gagnant = board[2]
        return True


def checkDiag(board):
    global gagnant
    if board[0] == board[4] == board[8] and board[0] != "-":
        gagnant = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        gagnant = board[2]
        return True


def checkTie(board):
   
    if "-" not in board:
        printboard(board)
    print("égalité")  
    jeuxencours = False


def checkWin():
    global jeuxencours
    global stope_game

    if checkDiag(board) or checkHorizontale(board):
       print(f" The winner is {gagnant}") 
       stope_game = True

    
    



 

def switchPlayer():
    global joueuractuel
    if joueuractuel == "X":
        joueuractuel = "O"
    else:
        joueuractuel = "X"
        





while jeuxencours == True:
    
    printboard(board)
    playerinput(board)
    checkWin()
    if stope_game == True:
        print('felicitations {}'.format(gagnant))
        break
    
    switchPlayer()
   