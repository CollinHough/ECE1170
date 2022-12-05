# Collin Hough, Matthew Kaiser
# ECE 1170 Semester Project

import pandas as pd

def get_model_data(type,player_id):
    # Load data depending on offense type
    if type == "passing":
        data = pd.read_csv("../../data/processed/passing.csv")
        player_data = data[data["id"] == player_id]
        rookie = checkIfRookie(player_data)
        if rookie:
            return "rookie"
        else:
            model_data = player_data[["GS","Cmp","Att","Cmp%","Yds","TD","TD%","Y/A","AY/A","Y/C","Y/G","Rate","QBR","NY/A","ANY/A","Cmp/G","Att/G"]]
    elif type == "rushing":
        data = pd.read_csv("../../data/processed/rushing.csv")
        player_data = data[data["id"] == player_id]
        rookie = checkIfRookie(player_data)
        if rookie:
            return "rookie"
        else:
            player_data.head()
            model_data = player_data[["GS","Att","Yds","TD","Y/A","Y/G","TD/G","Att/G"]]
    else: # type == "receiving"
        data = pd.read_csv("../../data/processed/receiving.csv")
        player_data = data[data["id"] == player_id]
        rookie = checkIfRookie(player_data)
        if rookie:
            return "rookie"
        else:
            model_data = player_data[["G","Tgt","Rec","Yds","TD","Y/R","R/G","Y/G","TD/G"]]
    return model_data

def checkIfRookie(player_data):
    # We know a player is a rookie if they only have 1 year of data
    numberOfYears = len(player_data.index)
    return numberOfYears <= 2