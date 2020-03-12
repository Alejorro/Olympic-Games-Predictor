#Importación de librerías
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import numpy as np

from Src.errorHandler import *

#Coding

@jsonErrorHandler
def ploting(tipo=1):

    #Seleccionar tipo de plotting
    if tipo == "1":
        df = pd.read_csv("Input/athlete_events.csv")  
        dfGames = df[["Year","Season","Medal"]]
        dfGames = dfGames.groupby(["Year", "Season"]).agg({"Medal":"count"}).reset_index()
        fig_dims = (25, 4)
        fig, ax = plt.subplots(figsize=fig_dims)
        sns.barplot(x="Year", y="Medal", hue="Season",ax=ax,data=dfGames)

        return fig

        
    # elif tipo == "2":
    #     df = pd.read_csv("Input/athlete_events.csv")  
    #     df = pd.get_dummies(df,columns=["Medal"])
    #     df = pd.DataFrame(df[["Name",'Medal_Gold','Medal_Silver', 'Medal_Bronze']].groupby("Name").agg({'Medal_Gold':"sum",'Medal_Silver':"sum", 'Medal_Bronze':"sum"}))
    #     df['Medals'] = df.loc[:, 'Medal_Gold':'Medal_Bronze'].sum(1)
    #     df = df.sort_values(by=["Medals"], ascending = False).iloc[:10].reset_index()

    #     Athletes=df["Name"]
    #     fig = go.Figure(data=[
    #         go.Bar(name='Gold_Medal', x=Athletes, y=df["Medal_Gold"]),
    #         go.Bar(name='Silver_Medal', x=Athletes, y=df["Medal_Silver"]),
    #         go.Bar(name='Bronze_Medal', x=Athletes, y=df["Medal_Bronze"])
    #     ])

    #     fig.update_layout(barmode='group')

    #     return fig
        

    elif tipo == "2":
        df = pd.read_csv("Input/athlete_events.csv")  
        df.drop(columns="ID", inplace=True)
        corr = df.corr()
        mask = np.triu(np.ones_like(corr, dtype=np.bool))
        fig, ax = plt.subplots(figsize=(11, 9))
        cmap = sns.diverging_palette(220, 10, as_cmap=True)
        sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
                    square=True, linewidths=.5, cbar_kws={"shrink": .5}, annot=True)
        return fig



    raise Exception("You can only choose between option 1 and option 2")







