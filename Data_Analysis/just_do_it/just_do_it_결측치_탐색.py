import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import platform
from just_do_it_데이터_병합 import df

####################### EDA 및 전처리 ##########################
print(df.isna().sum())
print(df.info())

