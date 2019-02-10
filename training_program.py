#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 19:15:08 2018

@author: a.gogohia
"""


import pandas as pd
import numpy as np
import training as tg
import evaluator_model as em

model = em.create_model()

game_counter = 1
data_for_graph = pd.DataFrame()

mode_list = ["Easy", "Hard"]

while game_counter <= 100000:
    mode_selected = np.random.choice(mode_list, 1, p=[0.5, 0.5])
    model, y, result = tg.train(model, mode=mode_selected[0], print_progress=False)
    data_for_graph = data_for_graph.append({"game_counter":game_counter,
                                            "result":result}, ignore_index=True)
    if game_counter % 1000 == 0:
        print("game#:", game_counter)
        print(mode_selected[0])
    game_counter += 1

bins = np.arange(1, game_counter/1000) * 1000
data_for_graph['game_counter_bins'] = np.digitize(data_for_graph["game_counter"],
                                                  bins, right=True)
counts = data_for_graph.groupby(['game_counter_bins', 'result']).game_counter.count().unstack()
ax = counts.plot(kind='bar', stacked=True, figsize=(17, 5))
ax.set_xlabel("Count of Games in Bins of 10,000s")
ax.set_ylabel("Counts of Draws/Losses/Wins")

model.save('my_model.h5')  # creates a HDF5 file 'my_model.h5'
