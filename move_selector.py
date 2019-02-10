#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 14:57:59 2018

@author: a.gogohia
"""

import legal_moves_func as lm
import evaluator_model as em

def move_selector(model, current_board_state, turn_monitor):
    """Function that selects the next move to make from a set of all possible
    legal moves

    Args:
    model: The evaluator function to evaluate ech possible next board state
    current_board_state: The current board state
    turn_monitor: 1 if it's the player who places the mark 1's turn to play,
    0 if its his opponent's turn

    Returns:
    selected_move: The numpy array coordinates, where player should place its
    mark
    new_board_state: The flattened new board state resulting from selected move
    score: The score which was assigned by the evaluator model

    """
    tracker = {}
    model = em.create_model()
    legal_moves_dict = lm.legal_moves_generator(current_board_state, turn_monitor)
    for legal_move_coord in legal_moves_dict:
        score = model.predict(legal_moves_dict[legal_move_coord].reshape(1, 9))
        tracker[legal_move_coord] = score
    selected_move = max(tracker, key=tracker.get)
    new_board_state = legal_moves_dict[selected_move]
    score = tracker[selected_move]
    return selected_move, new_board_state, score
            