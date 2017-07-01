from PIL import Image, ImageDraw
import pandas as pd
m=2 #magnification
df=pd.read_csv("output_img.csv")#read csv file
out = Image.new("RGB",(int((df['X'].max()*m)),int((df['Y'].max()*m)))) #create new blank image of appropriate size
dout = ImageDraw.Draw(out)
for index,row in df.iterrows():
    dout.point((int(row['X'])*m,int(row['Y'])*m),fill=(int(row['R']),int(row['G']),int(row['B']))) #fill in points by iterating over csv
out.show() #output image