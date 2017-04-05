import pandas as pd
import numpy as np


#string = input string, n_beg = number of chars to delete in beginning (default 0)
#n_end = number of chars to delete at end (default 0), returns string
def kill_chars(string, n_beg=0, n_end=0):
	if n_beg > 0:
		temp = string[n_beg:]
	elif n_end > 0:
		temp = string[:-n_end]
	return temp