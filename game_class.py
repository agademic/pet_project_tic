#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 11:33:12 2018

@author: a.gogohia
"""


import numpy as np

class tic_tac_toe_game(object):
    """Game class to initialize Tic Tac Toe board, to make moves on the board
    and to check whether the game has been won or lost

    """

    def __init__(self):
        self.board = np.full((3, 3), 2) # initialize empty board

    def toss(self):
        """Function to simulate a coin toss to decide which player will start
        Returns 1 if player assigned to mark 1 has won, or 0 if his opponent
        has won
        """
        turn = np.random.randint(0, 2, size=1)
        if turn.mean() == 0:
            self.turn_monitor = 0
        elif turn.mean() == 1:
            self.turn_monitor = 1
        return self.turn_monitor

    def move(self, player, coord):
        """Function to perform the action of placing a mark on the board
        After placing the mark, the function flips the value of turn_monitor to
        the next player

        Args:
        player: 1 if player who assigned the mark 1 is performing the action,
        0 if his opponent is performing teh action
        coord: the coordinate where the 1 or 0 is to be placed on the board

        Returns:
        game_status(): Calls the game status function and returns its value
        board: Returns the new board state after making the move

        """
        if self.board[coord] != 2 or self.game_status() != 'In Progress' \
        or self.turn_monitor != player:
            raise ValueError('Invalid move')
        self.board[coord] = player
        self.turn_monitor = 1-player
        return self.game_status(), self.board

    def game_status(self):
        """Function to check the game status, whether the game has been won,
        drawn or is in progress

        Returns:
        "Won" if the game has been won, "Drawn" if the game has been drawn or
        "In Progress" if the game is still in progress

        """
        #check for a win along rows
        for i in range(self.board.shape[0]):
            if 2 not in self.board[i, :] and len(set(self.board[i, :])) == 1:
                return 'Won'

        #check for a win along columns
        for j in range(self.board.shape[1]):
            if 2 not in self.board[:, j] and len(set(self.board[i, :])) == 1:
                return 'Won'

        #check for a win along diagonals
        if 2 not in np.diag(self.board) and len(set(np.diag(self.board))) == 1:
            return 'Won'
        if 2 not in np.diag(np.fliplr(self.board)) \
        and len(set(np.diag(np.fliplr(self.board)))) == 1:
            return 'Won'

        #check for a draw
        if not 2 in self.board:
            return 'Drawn'
        else:
            return 'In Progress'
            