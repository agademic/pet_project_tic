#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 14:39:05 2018

@author: a.gogohia
"""
import pprint

import game_class as gc
import legal_moves_func as lm

game = gc.tic_tac_toe_game()

game.toss()

print("Player ",game.turn_monitor," has won the toss")
print("Current board state")
print(game.board)
print("Legal Moves:")
legal_moves_dict=lm.legal_moves_generator(game.board,game.turn_monitor)
pprint.pprint(legal_moves_dict)
