"""
destinations.py

A collection of functions to analyse tour data from a JSON file.
Current metrics include:
- Duration averages
"""
import json #import the json library

# Funciton for loading the data from a .json file
def load_data(filepath):
    """
    Load tour data from a JSON file
    Arguments: filepath (str): the relative or absolute path to the .json file
    Returns: a list of dictionaries (the parsed JSON data)
    """
    with open(filepath, 'r') as file:
        return json.load(file)

# Load the core dataset to be used by analysis functions
tour_list = load_data('./tours.json')

# ==========================================
# 1. CORE PRICE AND DURATION METRICS
# ==========================================

def get_average_duration(tours):
    """
    Calculate the average duration of all tours
    Arguments: tours (list)
    Returns: the average duration in days
    """
    duration = 0 # Set the duration to 0
    # For loop 
    for tour in tours:
        duration += tour['duration']
    return duration / len(tours)

# ==========================================
# MAIN BLOCK
# ==========================================

if __name__ == "__main__":
    average_duration = get_average_duration(tour_list)
    print(f"The average tour duration is {average_duration:.2f} days")