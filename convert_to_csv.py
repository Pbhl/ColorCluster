from __future__ import with_statement
from PIL import Image
def img_to_csv(ip):
  op="input_raw.csv" #path to output file
  im = Image.open(ip)
  pix = im.load()#load the pixel info
  width, height = im.size #get a tuple of the x and y dimensions of the image
  with open('input_raw.csv', 'w+') as f:
    f.write('X,Y,R,G,B\n') 
  #read the details of each pixel and write them to the file
    for x in range(width):
      for y in range(height):
        r = pix[x,y][0]
        g = pix[x,y][1]
        b = pix[x,y][2]
        f.write('{0},{1},{2},{3},{4}\n'.format(x,y,r,g,b))