# -*- coding: utf-8 -*-
"""Task4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1elgmXZC-4hnlxl8_hAlfrSu0t_utCRoo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import os
import plotly.express as px

from google.colab import drive
drive.mount('/content/drive')
os.chdir('/content/drive/My Drive/Task_4')
os.listdir()

df1 = pd.read_csv('college_1.csv')
df2 = pd.read_csv('college_2.csv')
df1,df2

df = pd.concat([df1,df2])
df.head()

df.shape

df.info()

df = df.fillna(0)
df.isnull().sum()

"""###Exceed Expectations

"""

exceed = df[df['CodeKata Score']>15000]
exceed.reset_index(drop=True)

exceed.to_csv("Exceeded expectations.csv",index=False)

"""###Reached_expectations"""

reached = df[(df['CodeKata Score']>10000) & (df['CodeKata Score']<15000)]
reached.reset_index(drop=True)

reached.to_csv("Reached_expectations.csv",index=False)

"""###Needs_Improvement"""

improve = df[(df['CodeKata Score']>7000) & (df['CodeKata Score']<10000)]
improve.reset_index(drop=True)

improve.to_csv("Needs_Improvement.csv",index=False)

"""###Unsatisfactory"""

unsatisfied = df[df['CodeKata Score']<7000]
unsatisfied.reset_index(drop=True)

unsatisfied.to_csv("Unsatisfactory.csv",index=False)

"""###Average of previous week geekions vs this week geekions"""

df['Previous Geekions'].mean(), df['CodeKata Score'].mean()

"""###No of students participated"""

len(df['Name'].unique())

"""###Average"""

print(df['python'].mean())
print(df['python_en'].mean())
print(df['mysql'].mean())
print(df['computational_thinking'].mean())

"""###Rising star of the week"""

df.sort_values('CodeKata Score',ascending=False)[:3]

"""###Shining star"""

df.sort_values('Previous Geekions',ascending=False)[:3]

"""###Department wise codekata perfamance"""

fig = px.pie(df,values='CodeKata Score',names='Department',)
fig.show()

"""###Department wise toppers"""

df1 = df.sort_values('CodeKata Score',ascending=True)
fig = px.bar(df1,'Department','CodeKata Score',color='Previous Geekions',hover_name='Name')
fig.show()