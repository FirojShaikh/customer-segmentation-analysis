import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage
import datetime as dt

# Load the data
file_path = './data/Online Retail.xlsx' 
data = pd.read_excel(file_path)

# Display the first few rows of the data
print(data.head())

# Display the column names
print(data.columns)

# Display the data types of each column
print(data.dtypes)