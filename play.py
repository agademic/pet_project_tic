#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 21:51:19 2018

@author: a.gogohia
"""
import game_class as gc
import move_selector as ms
from evaluator_model import create_model
from keras.optimizers import SGD

model = create_model()
model.load_weights("my_model.h5")
sgd = SGD(lr=0.001, momentum=0.8,nesterov=False)
model.compile(loss='mean_squared_error', optimizer=sgd)
print("___________________________________________________________________")
print("Welcome to the Tic Tac Toe Game")
print("You will be playing against a self learned Program")
print("When it is your move, enter the coordinates in the form rownumber,columnnumber")
print(" For example, to place 0 at the top right corner, enter 0,2")
print("___________________________________________________________________")

play_again="Y"
while(play_again=="Y"):
    print("___________________________________________________________________")
    print("Starting a new Game")
    game=gc.tic_tac_toe_game()    
    game.toss()
    print(game.board)
    print(game.turn_monitor," has won the toss")
    while(1):
        if game.game_status()=="In Progress" and game.turn_monitor==0:
            print("Your Turn")
            while(1):
                try:
                    print('Enter where you would like to place a 0 in the form rownumber,columnnumber: ')
                    instr = input()
                    inList = [int(n) for n in instr.split(',')] 
                    coord = tuple(inList)
                    print(coord)
                    game_status,board=game.move(0,coord)
                    print(board)
                    break
                except:
                    print("Invalid Move")
        elif game.game_status()=="In Progress" and game.turn_monitor==1:
            print("Program's turn")
            chosen_move,new_board_state,score=ms.move_selector(model,game.board,game.turn_monitor)
            game_status,board=game.move(game.turn_monitor,chosen_move)
            print(board)
        else:
            break
    if game_status=="Won" and (1-game.turn_monitor)==1: 
        print("Program has won")
    if game_status=="Won" and (1-game.turn_monitor)==0:
        print("You have won")
    if game_status=="Drawn":
        print("Game Drawn")
    print("Would you like to play again? Y/N")
    play_again=input()