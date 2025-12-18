#TicTacToe Game

#First make a 3x3 board
B1 = {"value" : '1', "occupied" : False}
B2 = {"value" : '2', "occupied" : False}
B3 = {"value" : '3', "occupied" : False}
B4 = {"value" : '4', "occupied" : False}
B5 = {"value" : '5', "occupied" : False}
B6 = {"value" : '6', "occupied" : False}
B7 = {"value" : '7', "occupied" : False}
B8 = {"value" : '8', "occupied" : False}
B9 = {"value" : '9', "occupied" : False}


#Some global variables
Name1 =''
Name2 =''
Player1 =''
Player2 =''

#Combinations
# combination1 = [B1,B2,B3]
# combination2 = [B4,B5,B6]
# combination3 = [B7,B8,B9]
# combination4 = [B1,B4,B7]
# combination5 = [B2,B5,B8]
# combination6 = [B3,B6,B9]
# combination7 = [B1,B5,B9]
# combination8 = [B3,B5,B7]

Combinations = [
    [B1['value'], B2['value'], B3['value']],  # Row 1
    [B4['value'], B5['value'], B6['value']],  # Row 2
    [B7['value'], B8['value'], B9['value']],  # Row 3
    [B1['value'], B4['value'], B7['value']],  # Column 1
    [B2['value'], B5['value'], B8['value']],  # Column 2
    [B3['value'], B6['value'], B9['value']],  # Column 3
    [B1['value'], B5['value'], B9['value']],  # Diagonal 1
    [B3['value'], B5['value'], B7['value']]   # Diagonal 2
]

#Choose which player is which
def ChoosingPlayers():
    global Name1
    global Name2
    global Player1
    global Player2

    Name1 = input('Player 1, what is your name? ')
    Name2 = input('Player 2, what is your name? ')
    Player1 = input(f"{Name1}, do you want to be X or O? ").upper()
    while Player1 != 'X' and Player1 != 'O':
        Player1 = input(f"{Name1}, Enter a valid choice (X or O): ").upper()
    if Player1 == 'X':
        Player2 = 'O'
    else:
        Player2 = 'X'


#Print the board
def print_board():
    print("")
    print(f"{Name1} - {Player1} and {Name2} - {Player2}")
    print("")
    print(f"{B1['value']} | {B2['value']} | {B3['value']}")
    print("---------")
    print(f"{B4['value']} | {B5['value']} | {B6['value']}")
    print("---------")
    print(f"{B7['value']} | {B8['value']} | {B9['value']}")
    print("")

#Check if the game is over

def check_winner(Combinations,AllPositions):

    for combination in Combinations:
        if combination == ['X', 'X', 'X']:
            return 'X'
        elif combination == ['O', 'O', 'O']:
            return 'O'
    space = False
    for i in AllPositions:
            if i['occupied'] == False:
                space = True
    if space == False:
        return 'D'
    return 'F'

#Updating the positions
def UpdatePositions(pos,playerInput):
    global B1 
    global B2 
    global B3 
    global B4 
    global B5 
    global B6 
    global B7 
    global B8
    global B9 

    match pos:
        case 1:
            B1['value'] = playerInput
            B1['occupied'] = True
        case 2:
            B2['value'] = playerInput
            B2['occupied'] = True
        case 3:
            B3['value'] = playerInput
            B3['occupied'] = True
        case 4:
            B4['value'] = playerInput
            B4['occupied'] = True
        case 5:
            B5['value'] = playerInput
            B5['occupied'] = True
        case 6:
            B6['value'] = playerInput
            B6['occupied'] = True
        case 7:
            B7['value'] = playerInput
            B7['occupied'] = True
        case 8:
            B8['value'] = playerInput
            B8['occupied'] = True
        case 9:
            B9['value'] = playerInput
            B9['occupied'] = True

#Getting the player input
def GettingTheValue(player):
    found = False
    if player == 1:
        player_name = Name1
    else:
        player_name = Name2

    AllElements = [B1,B2,B3,B4,B5,B6,B7,B8,B9]
        
    while True:
        try:
            while True:
                position = int(input(f"{player_name}, Enter the position: "))
                if AllElements[position-1]['occupied'] == False:
                    break
                else:
                    print(f"Position - {position} already occupied!")

            if position >= 1 and position <= 9:
                break   
            else:
                print(f"Enter a Valid position {player_name}: ")
        except ValueError:
            print("Invalid input! Please enter a number (1-9)!")

    return position


#Switch Players
def SwitchPlayers(lastplayer):
    if lastplayer == 1:
        currentPlayer = 2
    else:
        currentPlayer = 1
    return currentPlayer

#TicTacToeBIG
def TicTacToeGame():

    ChoosingPlayers()
    currentPlayer = 1
    
    while True:
        print_board()
        BoardPosition = GettingTheValue(currentPlayer)
        if currentPlayer == 1:
            UpdatePositions(BoardPosition,Player1)
        else:
            UpdatePositions(BoardPosition,Player2)
        AllPositions = [B1,B2,B3,B4,B5,B6,B7,B8,B9]
        winner_combinations = [
                            [B1['value'], B2['value'], B3['value']],  # Row 1
                            [B4['value'], B5['value'], B6['value']],  # Row 2
                            [B7['value'], B8['value'], B9['value']],  # Row 3
                            [B1['value'], B4['value'], B7['value']],  # Column 1
                            [B2['value'], B5['value'], B8['value']],  # Column 2
                            [B3['value'], B6['value'], B9['value']],  # Column 3
                            [B1['value'], B5['value'], B9['value']],  # Diagonal 1
                            [B3['value'], B5['value'], B7['value']]   # Diagonal 2
                            ]
        
        status = check_winner(winner_combinations, AllPositions)
        if status == 'X':
            if Player1 =='X':
                print("")
                print(f"{Name1} won!")
                print_board()
                break
            else:
                print("")
                print(f"{Name2} won!")
                print_board()
                break
        elif status == 'O':
            if Player1 =='O':
                print("")
                print(f"{Name1} won!")
                print_board()
                break
            else:
                print("")
                print(f"{Name2} won!")
                print_board()
                break
        elif status == 'D':
            print("")
            print("Draw!")
            print_board()
            break

        currentPlayer = SwitchPlayers(currentPlayer)


TicTacToeGame()