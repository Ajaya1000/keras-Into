# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 22:22:50 2020

@author: Aju
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

np.random.seed(42) 
tf.random.set_seed(42)


inputs = np.array([4,-2,3.5,5,-11,-4.7])

n_weights = 6

sol_per_pop = 8 #solution per population
pop_size = (sol_per_pop,n_weights)

#creating the initial population
new_population = np.random.uniform(low=-4.0,high=4.0,size= pop_size)

import ga
