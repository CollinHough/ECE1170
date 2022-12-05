# Collin Hough, Matthew Kaiser
# ECE 1170 Semester Project

from sklearn import linear_model
import pandas as pd
import sys

def create_model(X,y):
    mdl = linear_model.LinearRegression()
    mdl.fit(X,y)
    return mdl
