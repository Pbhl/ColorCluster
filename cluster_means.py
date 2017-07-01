import pandas as pd
df = pd.read_csv("cluster.csv")#read cluster info file
df = df[['X','Y','R','G','B','Assignments']]
df_clust = df.groupby(['Assignments'])['R','G','B'].mean()#rgb means for every cluster

for x in range(31 + 1):
    for index,row in df.iterrows():
        if (row['Assignments'] == x):
            row['R']=df_clust.loc[x]['R']
            row['G']=df_clust.loc[x]['G']
            row['B']=df_clust.loc[x]['B']
df = df[['X','Y','R','G','B']]
df.to_csv("output_img.csv")