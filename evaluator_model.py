#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 14:46:49 2018

@author: a.gogohia
"""

from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
from keras.layers import Dropout

def create_model():
    """Function that creates a neural network for evaluation of the following
    turn.

    """
    model = Sequential()

    model.add(Dense(18, input_dim=9, kernel_initializer='normal', activation='relu'))
    model.add(Dropout(0.1))
    model.add(Dense(9, kernel_initializer='normal', activation='relu'))
    model.add(Dropout(0.1))
    model.add(Dense(1, kernel_initializer='normal'))

    learning_rate = 0.001
    momentum = 0.8
    sgd = SGD(lr=learning_rate, momentum=momentum, nesterov=False)
    model.compile(loss='mean_squared_error', optimizer=sgd)
    model.summary()
    return model
