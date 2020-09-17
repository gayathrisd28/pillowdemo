from PIL import Image

im = Image.open('input-images/koala.jpg')
im.show()

#pass the coordinates for the upper left and lower right corner of the rectangle to cr
cropped = im.crop((220,80,520,380))

cropped.show()

#Save the cropped image
cropped.save('out-images/croppedkoala.jpg')