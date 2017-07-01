import gzip
import pandas as pd
df = pd.read_csv("output_img.csv")#read cluster info file
df.to_csv("opzipped.csv",compression='gzip')