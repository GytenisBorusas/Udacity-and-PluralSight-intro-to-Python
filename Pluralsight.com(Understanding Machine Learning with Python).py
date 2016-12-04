#Predicting Diabetes

#Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("./data/pima-data.csv")      #load Pima data. adjust path as necessary
df.shape

df.head