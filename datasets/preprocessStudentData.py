# -*- coding: utf-8 -*-
"""
@author: JacobGulan
"""

# Preprocess data for Tableau visualzation
import pandas as pd

df = pd.read_csv(r"COVID-19SurveyStudentResponses.csv", 
                 encoding='latin-1')

# Remove entries with missing data
df = df.dropna()

# Convert ratings to numeric values
mapping = {'Very poor': 1, 'Poor': 2, 'Average': 3, 'Good': 4, 'Excellent': 5 }
df = df.replace({'Rating of Online Class experience': mapping})

# Save file
df.to_csv("studentResponses_preprocessed.csv", index=False) 