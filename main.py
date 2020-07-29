# The MIT License (MIT)
#
# Copyright (c) [year] [fullname]
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

################################################
## Description: Guess The Number - Game       ##
## Developer: Alex Anderson (Goodeath)        ##
## E-mail: alexandersonbm@hotmail.com         ##
## Date: 03/09/2017                           ##
################################################


## Libraries ##
import random;
import turtle;



##/////////////////////////////////////////
##                                       //
##            BOARD FUNCTIONS            //
##                                       //
##/////////////////////////////////////////

#############################################################
# Name: initializeBoard
# Description: Draw a graphic interface to the game
# Args: {none}
# Return: {none}
#############################################################

def initializeBoard(mode):
    # Clear Screen
    turtle.clearscreen()
    # Screen obj
    screen = turtle.Screen()
    # Title of game
    title = turtle.Pen()
    # Register Image
    screen.register_shape("title.gif")
    # Assign shape to pen cursor
    title.shape('title.gif')
    # Set x position
    title.setx(1);
    # Set y position
    title.sety(1)
    # Gray background color
    turtle.bgcolor("#707070")
    # Print a wait message
    print("Desenhando Tela...")
    # Create tables
    table(14,3,-300,-200,60)
    table(14,3, 100,-200,60)
    # Set pen
    pen = turtle.Pen()
    # Table title
    writeTitle('Vitorias',pen,-230)
    writeTitle('Números testados',pen,160)
    # UP pen
    pen.up();
    # Set column labels
    pen.setx(-285)
    pen.sety(230)
    pen.write("Player 1")
    pen.setx(-230)
    pen.write("Player 2")
    pen.setx(-160)
    pen.write("NPC")
    pen.setx(115)
    pen.write("Player 1")
    pen.setx(175)
    pen.write("Player 2")
    pen.setx(245)
    pen.write("NPC")
    # Finish message
    print("Tela desenhada!")
    #return guessedNumbers


#############################################################
# Name: markNumber
# Description: Draw a graphic interface to the game
# Args: {String} typ -> Player 1 = 0 | Player 2 = 1 | NPC = 2
#       {int} value -> Number typed
#       {int} count -> Quantity of numbers type
# Return: {none}
#############################################################
def markNumber(typ,value,count):
    # Set pen
    pen = turtle.Pen()
    
    pen.up()
    posy = 225 - count * 30
    pen.sety(posy)
    if(typ == 0):
        pen.setx(130)
        pen.write(str(value))
    elif(typ == 1):
        pen.setx(190)
        pen.write(str(value))
    elif(typ == 2):
        pen.setx(250)
        pen.write(str(value))
    return pen
    
    


def writeTitle(title,pen,posX):
    # Set title y default position
    posYTitle = 250;
    # Up pen
    pen.up();
    # Move cursor to y position
    pen.sety(posYTitle)
    # Move cursor to x position
    pen.setx(posX)
    # Write Title
    pen.write(title)
    

def table(cols,rows,posx,posy,length):
    # Set pen
    pen = turtle.Pen()
    pen.up()
    pen.setx(posx)
    pen.sety(posy)
    pen.down()
    tmp_len = length;
    print("Aguarde um momento...")
    pen.fillcolor('white')
    pen.begin_fill()
    # For rows
    for z in range(0,cols):
        pen.speed(10)
        
        
        # If it isn't the first iteraction
        if z != 0:
            # Don't draw anything
            pen.up()
            # Return to origin position
            pen.setx(posx)
            pen.sety(posy)
            # Next row
            posy += length/2
            # Set next row position
            pen.sety(posy)
            # Come back draw
            pen.down()
        # Create eight squares in one row
        for x in range(0,rows):
            # Draw square
            for y in range(0,4):
                # If is the first iteraction and x isn't the first square
                if y == 0 and x != 0:
                    # Advance fowards
                    length = tmp_len*2
                else:
                    if y % 2 == 0:
                        length = tmp_len
                    else:
                        # Set the default distance from origin
                        length = tmp_len
                # Draw line
                pen.fd(length);
                # Rotate 90 degrees
                pen.left(90);
    pen.end_fill()
    return pen

    
# Predefined functions
def header():
    print("#########################################")


###########################################
##           MENU FUNCTIONS              ##
###########################################


#############################################################
# Name: showTitle
# Description: Show the game title in ASCII
# Args: {none}
# Return: {none}
#############################################################

def showTitle():
    header();
    print("##            Guess the Number         ##")
    header();
    print("\n")

#############################################################
# Name: mainMenu
# Description: Show the main menu in ASCII
# Args: {none}
# Return: {String} option -> It has the value of a item menu
#############################################################

def mainMenu():
    header();
    print("##              MENU                   ##")
    header();
    print("1. Iniciar Jogo")
    print("2. Histórico")
    print("3. Configurações")
    print("4. Sair")
    option = input("> ")
    return option

####################################################
# Name: gameModeMenu()
# Description: The game mode menu.
# Args: {none}
# Return: {none}
####################################################

def gameModeMenu():
    print("1. Player")
    print("2. Player VS Player")
    print("3. Player VS NPC")
    print("4. Voltar")
    option = input("> ")
    return option

####################################################
# Name: config
# Description: The configuration menu of the program
# Args: {none}
# Return: {none}
####################################################

def config():
    # Default option value
    option = 0
    # Default difficut  ****************WARNING**********
    difficult = 1
    header();
    print("##           Configurações             ##")
    header();
    while(option != '2'):
        if option == '1':
            print("1. Fácil.")
            print("2. Médio.")
            print("3. Difícil.")
            difficult = input("> ")
        print("1. Selecionar Dificuldade")
        print("2. Voltar")
        option = input('> ')
    return difficult


###########################################
##              I.A FUNCTIONS            ##
###########################################


####################################################
# Name: difficultLevel
# Description: Increase game difficult by a chosen option.
# Args: String  {level} -> Difficult of the game
# Return: int {unamed} -> A number in one interval
####################################################
def difficultLevel(level):
    rand = random
    level = int(level)
    if level == 1:
       return rand.randrange(1,10)
    elif level == 2:
       return rand.randrange(1,30)
    elif level == 3:
        return rand.randrange(1,60)
    else:
        print('Condição não encontrada, por favor volte ao menu de configuração')
        print('e selecione uma dificuldade válida')
        return false


####################################################
# Name: npcIA
# Description: Define the npc IA.
# Args: String  {level} -> Difficult of the game
# Return: int {unamed} -> A number in one interval
####################################################
def npcIA(level):
    rand = random
    level = int(level)
    if level == 1:
       return rand.randrange(1,10)
    elif level == 2:
       return rand.randrange(1,30)
    elif level == 3:
        return rand.randrange(1,60)
    else:
        print('Condição não encontrada, por favor volte ao menu de configuração')
        print('e selecione uma dificuldade válida')
        return false


####################################################
# Name: gameMode
# Description: Shows all game modes( Multiplayer, SinglePlayer or with a NPC )
# Args: String  {difficult} -> Difficult of the game
# Return: {none}
####################################################

def gameMode(difficult):
    option = 5
    
    while(option != '4'):
        # Default play again value
        play_again = 'S';
        if option == '1':
            while(play_again == "S"):
                # Start a game
                playerGame(difficult,False,False)
                # Ask if want play again
                play_again = input("Gostaria de jogar novamente? (S/N)\n> ")
        elif option == '2':
            while(play_again == "S"):
                # Start a multiplayer game
                multiplayerGame(difficult);
                # Ask if want play again
                play_again = input("Gostaria de jogar novamente? (S/N)\n> ")
        elif option == '3':
            while(play_again == "S"):
                npcGame(difficult);
                # Ask if want play again
                play_again = input("Gostaria de jogar novamente? (S/N)\n> ")
        option = gameModeMenu();
        if option != '4':
            # Warning #
            initializeBoard(1)



####################################################
# Name: playerGame ( Maybe mainGame )
# Description: Plays a game ( Multiplayer, SinglePlayer or with a NPC )
# Args: String  {difficult} -> Difficult of the game
#       Boolean {npc} -> Play or not with a npc
# Return: {none}
####################################################

def playerGame(difficult,npc,multiplayer):
    # Get one number based on difficult level
    number = difficultLevel(difficult)
    # User number input default
    usr_number = 0
    # Start message
    print("\n\n !!!!!!!!!!!!!!!!!!!! Let's play!!!!!!!!!!!!!!!!!!!! ")
    # Explanation message
    print(" Vamos lá, tudo que você tem que fazer, é chutar um número, e eu te darei algumas dicas")
    # Array
    dic =[];
    playerTwoDic = [];
    npcDic = []
    # While #
    while(usr_number != number):
        if len(dic) > 1:
            print("\nNúmeros já utilizados:")
            print(dic)
            print("\n")


        #################
        #     Player    #
        #################
        
        # Get a number of the user
        usr_number = input("\n\nJogador1\n> ")

        
        # cast
        usr_number = int(usr_number)
        if usr_number > number:
            print('Olha, você está muito exaltado... vai precisar de um número um pouco menor')
            dic.append(markNumber(0,usr_number,len(dic)+1))
            #markNumber(0,usr_number,len(dic)+1)
        elif usr_number < number:
            dic.append(markNumber(0,usr_number,len(dic)+1))
            print('Não tenha medo cara, sente o dedo')
            #markNumber(0,usr_number,len(dic))
        else:
            print("Uaaaaaaaaaaaaaaaaaaau, você acertou")
            input("Aperte enter para continuar")
            for y in range(0,len(dic)):
                dic[y].clear()
                dic[y].hideturtle()
            if multiplayer == True:
                for y in range(0,len(playerTwoDic)):
                    playerTwoDic[y].clear()
                    playerTwoDic[y].hideturtle()
                for y in range(0,len(npcDic)):
                    npcDic[y].clear()
                    npcDic[y].hideturtle()
            elif npc == True:
                for y in range(0,len(playerTwoDic)):
                    playerTwoDic[y].clear()
                    playerTwoDic[y].hideturtle()
                for y in range(0,len(npcDic)):
                    npcDic[y].clear()
                    npcDic[y].hideturtle()
            break
        
        
        #################
        # Player Vs NPC #
        #################
        
        # Check if has a npc to play with
        if npc == True:
            npc_turn = npcIA(difficult)
            # Add a item to npc array to increase count
            playerTwoDic.append(markNumber(1,'x',len(playerTwoDic)+1))
            # Register x on graph
            #markNumber(1,'x',len(playerTwoDic))
            if npc_turn > number:
                npcDic.append(markNumber(2,npc_turn,len(npcDic)+1))
                print('O computador também chutou um número acima')
                #markNumber(2,npc_turn,len(npcDic))
            elif npc_turn < number:
                npcDic.append(markNumber(2,npc_turn,len(npcDic)+1))
                print('O computador também chutou um número abaixo')
                #markNumber(2,npc_turn,len(npcDic))
            else:
                print("Uaaaaaaaaaaaaaaaaaaau, Turn Down For What! Perdeu pra máquina rapá?")
                input("Aperte enter para continuar")
                for y in range(0,len(npcDic)):
                    npcDic[y].clear()
                    npcDic[y].hideturtle()
                for y in range(0,len(dic)):
                    dic[y].clear()
                    dic[y].hideturtle()
                for y in range(0,len(playerTwoDic)):
                    playerTwoDic[y].clear()
                    playerTwoDic[y].hideturtle()
                break
            
            
        ####################
        # Player Vs Player #
        ####################
        
        elif multiplayer == True:
            # Get a number of the user
            player_two = input("\n\nJogador 2 \n> ")
            # Add a item to npc array to increase count
            npcDic.append(markNumber(2,'x',len(npcDic)+1))
            # Register x on graph
            playerTwoDic.append(markNumber(1,player_two,len(playerTwoDic)+1))
            if playerTwoControl(number,player_two) == False:
                for y in range(0,len(playerTwoDic)):
                    playerTwoDic[y].clear()
                    playerTwoDic[y].hideturtle()
                for y in range(0,len(dic)):
                    dic[y].clear()
                    dic[y].hideturtle()
                for y in range(0,len(npcDic)):
                    npcDic[y].clear()
                    npcDic[y].hideturtle()
                break

####################################################
# Name: npcGame
# Description: Plays with a npc
# Args: {none}
# Return: {none}
####################################################

def npcGame(difficult):
    playerGame(difficult,True,False);

####################################################
# Name: multiplayerGame
# Description: Plays with a npc
# Args: {none}
# Return: {none}
####################################################
def multiplayerGame(difficult):
    playerGame(difficult,False,True);


##/////////////////////////////////////////
##                                       //
##            GAME CONTROLS              //
##                                       //
##/////////////////////////////////////////

####################################################
# Name: playerTwoControl
# Description: Plays with a npc
# Args: int {number} -> Current random number
# Return: {none|false} -> If the number chosen is
#         the correct.
####################################################
def playerOneControl(number,player_two):
   
    # cast
    player_two = int(player_two)
    if player_two > number:
        print('O Jogador 2 chutou um número acima')
        
    elif player_two < number:
        print('O Jogador 2 chutou um número abaixo')
       
    else:
        print("Uaaaaaaaaaaaaaaaaaaau, Turn Down For What! O Jogador 2 bota pra lá!")
        return False;
    

####################################################
# Name: playerTwoControl
# Description: Plays with a npc
# Args: int {number} -> Current random number
# Return: {none|false} -> If the number chosen is
#         the correct.
####################################################
def playerTwoControl(number,player_two):
    # cast
    player_two = int(player_two)
    if player_two > number:
        print('O Jogador 2 chutou um número acima')
    elif player_two < number:
        print('O Jogador 2 chutou um número abaixo')
    else:
        print("Uaaaaaaaaaaaaaaaaaaau, Turn Down For What! O Jogador 2 bota pra lá!")
        return False;

####################################################
# Name: playerName
# Description: Register a user name
# Args: {none}
# Return: {String} name -> Current user name
####################################################

def playerName():
    # Get the name
    name = input("Bem vindo! Por favor digite seu nome:\n> ")
    # Welcome Message
    print("\nEspero que se divirta "+name+"\n")
    # return name
    return name


###############################################
# Name: Main
# Description: The main function of program
# Args: {none}
# Return: {none}
###############################################

def main():
    # Option default: none
    option = 0
    # Play again Default:
    play_again = 'S'
    # Difficult default: Easy
    difficult = 1
    # Get user name
    name = playerName()
    # Show title
    showTitle();
    ## While ##
    while(option != '4'):
        if option == '1':
            # Show all type of games
            gameMode(difficult);           
        elif(option == '3'):
            # Set difficult
            difficult = config()
        # Main menu options
        option = mainMenu();
    print("Jogo finalizado")
    print('\
                            .xm*f\"\"??T?@hc.\n\
                          z@"` \'~((!!!!!!!?*m.\n\
                        z$$$K   ~~(/!!!!!!!!!Mh\n\
                      .f` \'#$k\'`~~\\!!!!!!!!!!!MMc\n\
                     :"     f*! ~:~(!!!!!!!!!!XHMk\n\
                     f      \" %n:~(!!!!!!!!!!!HMMM.\n\
                    d          X~!~(!!!!!!!X!X!SMMR\n\
                    M :   x::  :~~!>!!!!!!MNWXMMM@R\
\n n                  E \' *  ueeeeiu(!!XUWWWWWXMRHMMM>                :.\
\n E%                 E  8 .$$$$$$$$K!!$$$$$$$$&M$RMM>               :\"\
\nz  %                3  $ 4$$$$$$$$!~!*$$$$$$$$!$MM$               :\" `\
\nK   \":              ?> # \'#$$$$$#~!!!!TR$$$$$R?@MME              z   R\
\n?     %.             5     ^\"\"\"~~~:XW!!!!T?T!XSMMM~            :^    J\
\n \".    ^s             ?.       ~~d$X$NX!!!!!!M!MM             f     :~\
\n  \'+.    #L            *c:.    .~\"?!??!!!!!XX@M@~           z\"    .*\
\n    \'+     %L           #c`"!+~~~!/!!!!!!@*TM8M           z"    .~\
\n      \":    \'%.         \'C*X  .!~!~!!!!!X!!!@RF         .#     +\
\n        \":    ^%.        9-MX!X!!X~H!!M!N!X$MM        .#`    +"\
\n         #:    "n       \'L\'!~M~)H!M!XX!$!XMXF      .+`   .z"\
\n           #:    ":      R *H$@@$H$*@$@$@$%M~     z`    +"\
\n              %:   `*L    \'k\' M!~M~X!!$!@H!tF    z"    z"\
\n                *:   ^*L   "k ~~~!~!!!!!M!X*   z*   .+\"\
\n                  \"s   ^*L  \'%:.~~~:!!!!XH\"  z#   .*\"\
\n                    #s   ^%L  ^"#4@UU@##"  z#   .*"\
\n                      #s   ^%L           z#   .r"\
\n                        #s   ^%.       u#   .r"\
\n                          #i   \'%.   u#   .@"\
\n                            #s   ^%u#   .@"\
\n                              #s x#   .*"\
\n                               x#`  .@%.\
\n                             x#`  .d\"  \"%.\
\n                           xf~  .r\" #s   \"%.\
\n                     u   x*`  .r\\"     #s   \"%.  x.\
\n                     %Mu*`  x*\"         #m.  \"%zX\"\
\n                     :R(h x*              \"h..*dN.\
\n                   u@NM5e#>                 7?dMRMh.\
\n                 z$@M@$#\"#\"                 *\"\"*@MM$hL\
\n               u@@MM8*                          \"*$M@Mh.\
\n             z$RRM8F"                             "N8@M$bL\
\n            5`RM$#                                  \'R88f)R\
\n            \'h.$\"                                     #$x*\"\'')

# Let's play!!!!
main()
