# Import required libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from pylab import rcParams

# Import data
file_path = "data/dermatology_database_1.csv"
data = pd.read_csv(file_path)
data = pd.DataFrame(data)

#print(data.info())

data['age'] = pd.to_numeric(data['age'], errors='coerce')

data['age'].fillna(data['age'].median())

#print(data.isna())

# Plot features
rcParams['figure.figsize'] = 20, 15
sns.set_style('whitegrid')

data.hist(bins=10, figsize=(20,15))
# plt.show()

fig, axes = plt.subplots(nrows = 6, ncols = 6, figsize = (20,15))

for i, column in enumerate(data.columns):
    row = i // 6
    col = i % 6
    sns.boxplot(x=data[column], ax=axes[row, col])
    axes[row, col].set_title(column)

plt.tight_layout()
plt.show()

#print(len(data.columns))

