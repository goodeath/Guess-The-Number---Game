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
from tkinter import *;
# Define variables
rand = random;

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
    # Default play again value
    play_again = 'S';
    while(option != '4'):
        if option == '1':
            while(play_again == "S"):
                # Start a game
                playerGame(difficult,False)
                # Ask if want play again
                play_again = input("Gostaria de jogar novamente? (S/N)\n> ")
        elif option == '2':
            while(play_again == "S"):
                # Start a multiplayer game
                multiplayerGame();
                # Ask if want play again
                play_again = input("Gostaria de jogar novamente? (S/N)\n> ")
        elif option == '3':
            while(play_again == "S"):
                npcGame(difficult);
                # Ask if want play again
                play_again = input("Gostaria de jogar novamente? (S/N)\n> ")
        option = gameModeMenu();



####################################################
# Name: playerGame ( Maybe mainGame )
# Description: Plays a game ( Multiplayer, SinglePlayer or with a NPC )
# Args: String  {difficult} -> Difficult of the game
#       Boolean {npc} -> Play or not with a npc
# Return: {none}
####################################################

def playerGame(difficult,npc):
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
    
    # While #
    while(usr_number != number):
        if len(dic) > 1:
            print("\nNúmeros já utilizados:")
            print(dic)
            print("\n")
        # Get a number of the user
        usr_number = input("> ")

        
        # cast
        usr_number = int(usr_number)
        if usr_number > number:
            print('Olha, você está muito exaltado... vai precisar de um número um pouco menor')
            dic.append(usr_number)
        elif usr_number < number:
            dic.append(usr_number)
            print('Não tenha medo cara, sente o dedo')
        else:
           print("Uaaaaaaaaaaaaaaaaaaau, você acertou")
           break
        # Check if has a npc to play with
        if npc == True:
            npc_turn = npcIA(difficult)
            if npc_turn > number:
                print('O computador também chutou um número acima')
            elif npc_turn < number:
                print('O computador também chutou um número abaixo')
            else:
               print("Uaaaaaaaaaaaaaaaaaaau, Turn Down For What! Perdeu pra máquina rapá?")
               break

####################################################
# Name: npcGame
# Description: Plays with a npc
# Args: {none}
# Return: {none}
####################################################

def npcGame(difficult):
    playerGame(difficult,True);
    

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
        # Value unknown
        unknown = rand.randrange(0,10)
        #print(unknown)
    print("Jogo finalizado")

# Let's play!!!!
main()
