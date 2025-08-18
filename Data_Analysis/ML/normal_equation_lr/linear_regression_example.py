import pandas as pd
import numpy as np
from normal_equation_lr import LinearRegression

df = pd.read_csv(r"test.csv")

X = df["x"].values.reshape(-1,1)
y = df["y"].values


lr = LinearRegression(fit_intercept=True)

lr.fit(X, y)

print(lr.intercept)
print(lr.coef)
print(lr.predict(X)[:10])