# Import required libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

# Import data
file_path = "data/dermatology_database_1.csv"
data = pd.read_csv(file_path)
data = pd.DataFrame(data)

print(data.info())

data['age'] = pd.to_numeric(data['age'], errors='coerce')

data['age'].fillna(data['age'].median())

print(data.dtypes)