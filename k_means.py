from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
df=pd.read_csv("billgates.csv")
X=np.array(df)
kmeans = KMeans(n_clusters=32, max_iter=100).fit_predict(X)
df['Assignments'] = kmeans
df.to_csv('myclustertest.csv',index=False)