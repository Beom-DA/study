import pandas as pd
import dateutil

df_phone = pd.read_csv("phone_data.csv")
df_phone['date'] = df_phone['date'].apply(dateutil.parser.parse, dayfirst=True)
df_phone.head()

df_phone.pivot_table(["duration"],
                     index=[df_phone.month,df_phone.item], 
                     columns=df_phone.network, aggfunc="sum", fill_value=0)

df_movie = pd.read_csv("movie_rating.csv")
print(df_movie.head())



df_movie.pivot_table(["rating"], index=df_movie.critic, columns=df_movie.title,
                     aggfunc="sum", fill_value=0)

pd.crosstab(index=df_movie.critic,columns=df_movie.title,values=df_movie.rating,
            aggfunc="first").fillna(0)

df_movie.groupby(["critic","title"]).agg({"rating":"first"}).unstack().fillna(0)