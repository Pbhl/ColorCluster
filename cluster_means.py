import pandas as pd
df = pd.read_csv("cluster_raw.csv")#read cluster info file
df = df[['X','Y','R','G','B','Assignments']]#remove any redundant columns
df_clust = df.groupby(['Assignments'])['R','G','B'].mean()#calculate rgb means for every cluster
#replace color values with mean values of respective cluster
for x in range(31 + 1):
    for index,row in df.iterrows():
        if (row['Assignments'] == x):
            row['R']=df_clust.loc[x]['R']
            row['G']=df_clust.loc[x]['G']
            row['B']=df_clust.loc[x]['B']
df = df[['X','Y','R','G','B']]
df.to_csv("output_img.csv")