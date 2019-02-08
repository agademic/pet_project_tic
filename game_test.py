#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 12:05:33 2018

@author: a.gogohia
"""

import game_class as gc

# create an object of the class tick_tac_toe_game
game=gc.tic_tac_toe_game()
# toss to decide which player goes first
game.toss()
print("Player ",game.turn_monitor," has won the toss")
# make the first move
print("Initial board state")
print(game.board)
print("Let first player place their mark on 0,0")
game_status,board=game.move(game.turn_monitor,(0,0))
print("New Board State: ")
print(board)
print("Let second player place their mark on 0,1")
game_status,board=game.move(game.turn_monitor,(0,1))
print("New Board State: ")
print(board)
print("Let first player place their mark on 1,1")
game_status,board=game.move(game.turn_monitor,(1,1))
print("New Board State: ")
print(board)
print("Let second player place their mark on 0,2")
game_status,board=game.move(game.turn_monitor,(0,2))
print("New Board State: ")
print(board)
print("Let first player place their mark on 2,2")
game_status,board=game.move(game.turn_monitor,(2,2))
print("New Board State: ")
print(board)
print("Player ",1-game.turn_monitor," Has ",game_status)
