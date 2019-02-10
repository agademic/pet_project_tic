#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 19:04:47 2018

@author: a.gogohia
"""


import random
import numpy as np
import legal_moves_func as lmg

def row_winning_move_check(current_board_state, legal_moves_dict, turn_monitor):
    """Function to scan rowwise and identify coordinate amongst the legal
    coordinates that will result in a winning board state

    Args:
    legal_moves_dict: Dictionary of legal next moves
    turn_monitor: whose turn it is to move

    Returns:
    selected_move: The coordinates of numpy array where placing the 0 will lead
    to win for the opponent

    """
    legal_move_coords = list(legal_moves_dict.keys())
    random.shuffle(legal_move_coords)
    for legal_move_coord in legal_move_coords:
        current_board_state_copy = current_board_state.copy()
        current_board_state_copy[legal_move_coord] = turn_monitor
        #check for a win along rows
        for i in range(current_board_state_copy.shape[0]):
            if 2 not in current_board_state_copy[i, :] and \
            len(set(current_board_state_copy[i, :])) == 1:
                selected_move = legal_move_coord
                return selected_move

def column_winning_move_check(current_board_state, legal_moves_dict, turn_monitor):
    """Function to scan column wise and identify coordinate amongst the legal
    coordinates that will result in a winning board state

    Args:
    legal_moves_dict: Dictionary of legal next moves
    turn_monitor: whose turn it is to move

    Returns:
    selected_move: The coordinates of numpy array where placing the 0 will
    lead to win for the opponent
    """
    legal_move_coords = list(legal_moves_dict.keys())
    random.shuffle(legal_move_coords)
    for legal_move_coord in legal_move_coords:
        current_board_state_copy = current_board_state.copy()
        current_board_state_copy[legal_move_coord] = turn_monitor
        for j in range(current_board_state_copy.shape[1]):
            if 2 not in current_board_state_copy[:, j] and \
            len(set(current_board_state_copy[:, j])) == 1:
                selected_move = legal_move_coord
                return selected_move

def diag1_winning_move_check(current_board_state, legal_moves_dict, turn_monitor):
    """Function to scan diagonal and identify coordinate amongst the legal
    coordinates that will result in a winning board state

    Args:
    legal_moves_dict: Dictionary of legal next moves
    turn_monitor: whose turn it is to move

    Returns:
    selected_move: The coordinates of numpy array where placing the 0 will lead
    to win for the opponent

    """
    legal_move_coords = list(legal_moves_dict.keys())
    random.shuffle(legal_move_coords)
    for legal_move_coord in legal_move_coords:
        current_board_state_copy = current_board_state.copy()
        current_board_state_copy[legal_move_coord] = turn_monitor
        if 2 not in np.diag(current_board_state_copy) and \
        len(set(np.diag(current_board_state_copy))) == 1:
            selected_move = legal_move_coord
            return selected_move

def diag2_winning_move_check(current_board_state, legal_moves_dict, turn_monitor):
    """Function to scan second diagonal and identify coordinate amongst
    the legal coordinates that will result in a winning board state

    Args:
    legal_moves_dict: Dictionary of legal next moves
    turn_monitor: whose turn it is to move

    Returns:
    selected_move: The coordinates of numpy array where placing the 0 will
    lead to win for the opponent

    """
    legal_move_coords = list(legal_moves_dict.keys())
    random.shuffle(legal_move_coords)
    for legal_move_coord in legal_move_coords:
        current_board_state_copy = current_board_state.copy()
        current_board_state_copy[legal_move_coord] = turn_monitor
        if 2 not in np.diag(np.fliplr(current_board_state_copy)) and \
        len(set(np.diag(np.fliplr(current_board_state_copy)))) == 1:
            selected_move = legal_move_coord
            return selected_move

#------------#

def row_block_move_check(current_board_state, legal_moves_dict, turn_monitor):
    """Function to scan rowwise and identify coordinate amongst the legal coordinates
    that will prevent the program from winning

    Args:
    legal_moves_dict: Dictionary of legal next moves
    turn_monitor: whose turn it is to move

    Returns:
    selected_move: The coordinates of numpy array where placing the 0 will block 1 from winning

    """
    legal_move_coords = list(legal_moves_dict.keys())
    random.shuffle(legal_move_coords)
    for legal_move_coord in legal_move_coords:
        current_board_state_copy = current_board_state.copy()
        current_board_state_copy[legal_move_coord] = turn_monitor
        for i in range(current_board_state_copy.shape[0]):
            if 2 not in current_board_state_copy[i, :] and \
            (current_board_state_copy[i, :] == 1).sum() == 2:
                if not (2 not in current_board_state[i, :] and \
                        (current_board_state[i, :] == 1).sum() == 2):
                    selected_move = legal_move_coord
                    return selected_move

def column_block_move_check(current_board_state, legal_moves_dict, turn_monitor):
    """Function to scan column wise and identify coordinate amongst the legal
    coordinates that will prevent 1 from winning

    Args:
    legal_moves_dict: Dictionary of legal next moves
    turn_monitor: whose turn it is to move

    Returns:
    selected_move: The coordinates of numpy array where placing the 0 will block 1 from winning

    """
    legal_move_coords = list(legal_moves_dict.keys())
    random.shuffle(legal_move_coords)
    for legal_move_coord in legal_move_coords:
        current_board_state_copy = current_board_state.copy()
        current_board_state_copy[legal_move_coord] = turn_monitor

        for j in range(current_board_state_copy.shape[1]):
            if 2 not in current_board_state_copy[:, j] and \
            (current_board_state_copy[:, j] == 1).sum() == 2:
                if not (2 not in current_board_state[:, j] and \
                        (current_board_state[:, j] == 1).sum() == 2):
                    selected_move = legal_move_coord
                    return selected_move

def diag1_block_move_check(current_board_state, legal_moves_dict, turn_monitor):
    """Function to scan diagonal 1 and identify coordinate amongst the legal
    coordinates that will prevent 1 from winning

    Args:
    legal_moves_dict: Dictionary of legal next moves
    turn_monitor: whose turn it is to move

    Returns:
    selected_move: The coordinates of numpy array where placing the 0 will block 1 from winning

    """
    legal_move_coords = list(legal_moves_dict.keys())
    random.shuffle(legal_move_coords)
    for legal_move_coord in legal_move_coords:
        current_board_state_copy = current_board_state.copy()
        current_board_state_copy[legal_move_coord] = turn_monitor
        if 2 not in np.diag(current_board_state_copy) and \
        (np.diag(current_board_state_copy) == 1).sum() == 2:
            if not (2 not in np.diag(current_board_state) and \
                    (np.diag(current_board_state) == 1).sum() == 2):
                selected_move = legal_move_coord
                return selected_move

def diag2_block_move_check(current_board_state, legal_moves_dict, turn_monitor):
    """Function to scan second diagonal wise and identify coordinate amongst the
    legal coordinates that will
    result in a column having only 0s

    Args:
    legal_moves_dict: Dictionary of legal next moves
    turn_monitor: whose turn it is to move

    Returns:
    selected_move: The coordinates of numpy array where placing the 0 will lead
    to two 0s being there (and no 1s)

    """
    legal_move_coords = list(legal_moves_dict.keys())
    random.shuffle(legal_move_coords)
    for legal_move_coord in legal_move_coords:
        current_board_state_copy = current_board_state.copy()
        current_board_state_copy[legal_move_coord] = turn_monitor
        if 2 not in np.diag(np.fliplr(current_board_state_copy)) and \
        (np.diag(np.fliplr(current_board_state_copy)) == 1).sum() == 2:
            if not (2 not in np.diag(np.fliplr(current_board_state)) and \
                    (np.diag(np.fliplr(current_board_state)) == 1).sum() == 2):
                selected_move = legal_move_coord
                return selected_move

#---------------#
def row_second_move_check(current_board_state, legal_moves_dict, turn_monitor):
    """Function to scan rowwise and identify coordinate amongst the legal coordinates that will
    result in a row having two 0s and no 1s

    Args:
    legal_moves_dict: Dictionary of legal next moves
    turn_monitor: whose turn it is to move

    Returns:
    selected_move: The coordinates of numpy array where placing the 0 will lead
    to two 0s being there (and no 1s)

    """
    legal_move_coords = list(legal_moves_dict.keys())
    random.shuffle(legal_move_coords)
    for legal_move_coord in legal_move_coords:
        current_board_state_copy = current_board_state.copy()
        current_board_state_copy[legal_move_coord] = turn_monitor

        for i in range(current_board_state_copy.shape[0]):
            if 1 not in current_board_state_copy[i, :] and \
            (current_board_state_copy[i, :] == 0).sum() == 2:
                if not (1 not in current_board_state[i, :] and \
                        (current_board_state[i, :] == 0).sum() == 2):
                    selected_move = legal_move_coord
                    return selected_move

def column_second_move_check(current_board_state, legal_moves_dict, turn_monitor):
    """Function to scan column wise and identify coordinate amongst the legal coordinates that will
    result in a column having two 0s and no 1s

    Args:
    legal_moves_dict: Dictionary of legal next moves
    turn_monitor: whose turn it is to move

    Returns:
    selected_move: The coordinates of numpy array where placing the 0 will lead
    to two 0s being there (and no 1s)

    """
    legal_move_coords = list(legal_moves_dict.keys())
    random.shuffle(legal_move_coords)
    for legal_move_coord in legal_move_coords:
        current_board_state_copy = current_board_state.copy()
        current_board_state_copy[legal_move_coord] = turn_monitor

        for j in range(current_board_state_copy.shape[1]):
            if 1 not in current_board_state_copy[:, j] and \
            (current_board_state_copy[:, j] == 0).sum() == 2:
                if not (1 not in current_board_state[:, j] and \
                        (current_board_state[:, j] == 0).sum() == 2):
                    selected_move = legal_move_coord
                    return selected_move

def diag1_second_move_check(current_board_state, legal_moves_dict, turn_monitor):
    """Function to scan diagonal wise and identify coordinate amongst the legal
    coordinates that will result in a column having two 0s and no 1s

    Args:
    legal_moves_dict: Dictionary of legal next moves
    turn_monitor: whose turn it is to move

    Returns:
    selected_move: The coordinates of numpy array where placing the 0 will lead
    to two 0s being there (and no 1s)

    """
    legal_move_coords = list(legal_moves_dict.keys())
    random.shuffle(legal_move_coords)
    for legal_move_coord in legal_move_coords:
        current_board_state_copy = current_board_state.copy()
        current_board_state_copy[legal_move_coord] = turn_monitor
        if 1 not in np.diag(current_board_state_copy) and \
        (np.diag(current_board_state_copy) == 0).sum() == 2:
            if not (1 not in np.diag(current_board_state) and \
                    (np.diag(current_board_state) == 0).sum() == 2):
                selected_move = legal_move_coord
                return selected_move

def diag2_second_move_check(current_board_state, legal_moves_dict, turn_monitor):
    """Function to scan second diagonal wise and identify coordinate amongst
    the legal coordinates that will result in a column having two 0s and no 1s

    Args:
    legal_moves_dict: Dictionary of legal next moves
    turn_monitor: whose turn it is to move

    Returns:
    selected_move: The coordinates of numpy array where opponent places their mark

    """
    legal_move_coords = list(legal_moves_dict.keys())
    random.shuffle(legal_move_coords)
    for legal_move_coord in legal_move_coords:
        current_board_state_copy = current_board_state.copy()
        current_board_state_copy[legal_move_coord] = turn_monitor
        if 1 not in np.diag(np.fliplr(current_board_state_copy)) and \
        (np.diag(np.fliplr(current_board_state_copy)) == 0).sum() == 2:
            if not (1 not in np.diag(np.fliplr(current_board_state)) and \
                    (np.diag(np.fliplr(current_board_state)) == 0).sum() == 2):
                selected_move = legal_move_coord
                return selected_move

def opponent_move_selector(current_board_state, turn_monitor, mode):
    """Function that picks a legal move for the opponent

    Args:
    current_board_state: Current board state
    turn_monitor: whose turn it is to move
    mode: whether hard or easy mode

    Returns:
    selected_move: The coordinates of numpy array where placing the 0 will lead
    to two 0s being there (and no 1s)

    """
    legal_moves_dict = lmg.legal_moves_generator(current_board_state, turn_monitor)

    winning_move_checks = [row_winning_move_check, column_winning_move_check,
                           diag1_winning_move_check, diag2_winning_move_check]
    block_move_checks = [row_block_move_check, column_block_move_check,
                         diag1_block_move_check, diag2_block_move_check]
    second_move_checks = [row_second_move_check, column_second_move_check,
                          diag1_second_move_check, diag2_second_move_check]

    if mode == "Hard":
        random.shuffle(winning_move_checks)
        random.shuffle(block_move_checks)
        random.shuffle(second_move_checks)

        for i in winning_move_checks:
            if i(current_board_state, legal_moves_dict, turn_monitor):
                return i(current_board_state, legal_moves_dict, turn_monitor)

        for i in block_move_checks:
            if i(current_board_state, legal_moves_dict, turn_monitor):
                return i(current_board_state, legal_moves_dict, turn_monitor)

        for i in second_move_checks:
            if i(current_board_state, legal_moves_dict, turn_monitor):
                return i(current_board_state, legal_moves_dict, turn_monitor)

        selected_move = random.choice(list(legal_moves_dict.keys()))
        return selected_move

    elif mode == "Easy":
        legal_moves_dict = lmg.legal_moves_generator(current_board_state, turn_monitor)
        selected_move = random.choice(list(legal_moves_dict.keys()))
        return selected_move
