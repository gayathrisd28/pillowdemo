#Import required Image library
from PIL import Image

#Create an Image Object from an Image
im = Image.open('input-images/koala.jpg')

#Display actual image
im.show()

#left, upper, right, lower
#Crop
cropped = im.crop((220,80,520,380))

#Display the cropped portion
cropped.show()

#Save the cropped image
cropped.save('out-images/croppedkoala.jpg')