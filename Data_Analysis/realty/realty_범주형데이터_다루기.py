from realty_missingno import df
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df_object = df.describe(include='object')
print(df_object)