# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 15:03:15 2021

@author: JacobGulan
"""

# Preprocess data for Tableau visualzation
import pandas as pd

df = pd.read_csv(r"tableauPreProcessStudents.csv", 
                 encoding='latin-1')

# Remove entries with missing data
df = df.dropna()

# Save file
df.to_csv("preprocessedVisualizizationData.csv", index=False) 