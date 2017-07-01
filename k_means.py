from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
df=pd.read_csv("input_raw.csv") # raw input csv generated from input image
X=np.array(df) 
kmeans = KMeans(n_clusters=32, max_iter=100).fit_predict(X) #perform clustering (initialised using k-means++)
df['Assignments'] = kmeans #add cluster info with the color rows
df.to_csv('cluster_raw.csv',index=False)