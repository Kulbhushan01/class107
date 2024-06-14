import pandas as pd 
import csv 
import plotly.graph_objects as go


df = pd.read_csv("C:/Users/Kulbh/OneDrive/Desktop/Data-Analysis-by-visualisation-master/data.csv")

student_df = df.loc[df['student_id'] =="TRL_987"]

print(student_df.groupby("level")["attempt"].mean())
fig = go.Figure(go.bar(
            x=student_df.groupby("level1")["attempt"].mean(),
            y=['Level 1', 'Level 2', 'Level 3', 'Level 4' ],
            orientaiton = 'h'
))