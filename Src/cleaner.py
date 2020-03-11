import pandas as pd

def cleaner(df, type="ML"):

    if type == "ML"
        df2 = pd.read_csv("../Input/noc_regions.csv")  
        df2 = df2.drop(columns=["notes"])

        df3 = df.merge(df2, on='NOC')
        df3 = df3.loc[df3["Season"] == "Summer"].drop(columns="Season")
        df3 = df3.drop(columns=["ID","Games","Event","Team","NOC","Height","Weight"])
        df3 = df3.rename(columns={"City": "Host City", "region": "Region","Name":"Athlete"})

        df4 = pd.read_csv("../Input/host_cities.csv") 

        df5 = df3.merge(df4, on='Host City').drop(columns="Host City")
        df5 = df5[["Host Country", "Athlete", "Age", "Year", "Sport", "Region", "Sex_F", "Sex_M", "Medal"]]
        df5 = pd.get_dummies(df5,columns=["Medal"])
        df5 = pd.DataFrame(df5.groupby(['Host Country','Year','Region']).agg({'Athlete':"nunique", 'Sport':"nunique",'Medal_Gold':"sum",'Medal_Silver':"sum", 'Medal_Bronze':"sum"}))
        df5['Medals']= df5.iloc[:, -4:-1].sum(axis=1)
        df5 = df5.reset_index()
        df5 = df5.loc[df5["Year"]>=1990].sort_values(by=["Year"]).reset_index(drop=True)

        return df5
    
    if type == "plot"

        
