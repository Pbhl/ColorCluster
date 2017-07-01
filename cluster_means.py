def calc_mean():
    import pandas as pd
    df = pd.read_csv("cluster_raw.csv")#read cluster info file
    df = df[['X','Y','R','G','B','Assignments']]#remove any redundant columns
    df_clust = df.groupby(['Assignments'])['R','G','B'].mean().reset_index().set_index('Assignments').T.to_dict('list')#calculate rgb means for every cluster
    #replace color values with mean values of respective cluster
    df[['R','G','B']]=pd.DataFrame(x for x in df['Assignments'].map(df_clust))
    df.drop('Assignments', axis=1, inplace=True)
    df.to_csv("output_img.csv")