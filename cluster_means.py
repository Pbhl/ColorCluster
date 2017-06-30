import pandas as pd
df = pd.read_csv("cluster.csv")#read csv file
df_clust = df.groupby(['Assignments'])['R','G','B'].mean()
#for x in map(str, range(31 + 1)):
#df_clust[cluster] =  
print(df_clust)