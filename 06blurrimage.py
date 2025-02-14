#Import required Image library
from PIL import Image, ImageFilter
 
#Open existing image
OriImage = Image.open('input-images/cat.jpg')
OriImage.show()

#Applying BoxBlur filter
boxImage = OriImage.filter(ImageFilter.BoxBlur(7))
boxImage.show()
OriImage.filter(ImageFilter.EMBOSS).show()

#Save Boxblur image
boxImage.save('out-images/blurredcat.jpg')