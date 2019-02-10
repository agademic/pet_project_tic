#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 14:30:18 2018

@author: a.gogohia
"""


def legal_moves_generator(current_board_state, turn_monitor):
    """Function that returns the set of all possible legal moves and resulting
    board states, for a given input board state and player

    Args:
    current_board_state: The current board state
    turn_monitor: 1 if it is the player's turn who places the mark 1,
    0 if it is his opponents turn

    Returns:
    legal_moves_dict: A dictionary of a list of possible next
    coordinate-resulting board state pairs
    The resulting board state is flattened to 1d-array

    """
    legal_moves_dict = {}
    for i in range(current_board_state.shape[0]):
        for j in range(current_board_state.shape[1]):
            if current_board_state[i, j] == 2:
                board_state_copy = current_board_state.copy()
                board_state_copy[i, j] = turn_monitor
                legal_moves_dict[(i, j)] = board_state_copy.flatten()
    return legal_moves_dict
