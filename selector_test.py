#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 18:48:53 2018

@author: a.gogohia
"""

import game_class as gc
import move_selector as ms

# new game
game=gc.tic_tac_toe_game()
# toss
game.toss()
# choose the first move
print("Player assigned mark",game.turn_monitor," won the toss")
print("Initial board state:")
print(game.board)
selected_move,new_board_state,score=ms.move_selector(model,game.board,game.turn_monitor)
print("Selected move: ",selected_move)
print("Resulting new board state: ",new_board_state)
print("Score assigned to above board state by Evaluator(model): ", score)