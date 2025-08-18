import pandas as pd
df_time_series = pd.read_csv(r"AirPassengers.csv")
df_time_series.head()

df_time_series["step"] = range(len(df_time_series))

df_time_series["cum_sum"] = df_time_series["#Passengers"].cumsum()
df_time_series["cum_max"] = df_time_series["#Passengers"].cummax()
df_time_series["cum_min"] = df_time_series["#Passengers"].cummin()
df_time_series.head()

import numpy as np
temp_date = df_time_series["Month"].map(lambda x : x.split("-"))
temp_date = np.array(temp_date.values.tolist())
temp_date[:5]

df_time_series["year"] = temp_date[:, 0]
df_time_series["month"] = temp_date[:, 1]
df_time_series.head()

df_time_series["diff"] = df_time_series["#Passengers"].diff().fillna(0)
df_time_series[:5]

df_time_series["#Passengers"].pct_change().map(lambda x : x*100).map(lambda x : " %.2f" % x)


df_time_series["pct"]= df_time_series["#Passengers"].pct_change().map(lambda x: "%.2f" % (x * 100))
 
patent = pd.read_csv(r"sea_managing_raw.csv",encoding="cp949")
patent.head()


patent["출원번호"].isnull().sum()

df_patent = patent[["출원번호","Original US Class All[US]"]]
df_patent["Original US Class All[US]"][:5]

df_patent["Original US Class All[US]"].map(lambda x : x.split("|")).tolist()

edge_list = []
for data in zip(df_patent["출원번호"].tolist() ,df_patent["Original US Class All[US]"].map(lambda x : x.split("|")).tolist()):
    for value in data[1]:
        edge_list.append([data[0], value.strip()])
    
edge_list[:10]

df_edge_list = pd.DataFrame(edge_list)
df_edge_list["rating"] = 1
df_edge_list.groupby([0,1])["rating"].sum().unstack().fillna(0)

