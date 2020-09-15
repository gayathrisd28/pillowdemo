#Import required Image library
from PIL import Image, ImageFilter
 
#Open existing image
OriImage = Image.open('images/cat.jpg')
OriImage.show()

#Applying BoxBlur filter
boxImage = OriImage.filter(ImageFilter.BoxBlur(7))
boxImage.show()

#Save Boxblur image
boxImage.save('images/blurredcat.jpg')