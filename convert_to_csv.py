from __future__ import with_statement
from PIL import Image
 
im = Image.open('img.jpg') #relative path to file
 
#load the pixel info
pix = im.load()
 
#get a tuple of the x and y dimensions of the image
width, height = im.size
 
#open a file to write the pixel data
with open('waaargh.csv', 'w+') as f:
  f.write('X,Y,R,G,B\n')
 
  #read the details of each pixel and write them to the file
  for x in range(width):
    for y in range(height):
      r = pix[x,y][0]
      g = pix[x,y][1]
      b = pix[x,y][2]
      f.write('{0},{1},{2},{3},{4}\n'.format(x,y,r,g,b))