#Importing Required Libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#Loading Dataset

data = pd.read_csv('diabetes.csv')
data.head()


#Checking for missing data







