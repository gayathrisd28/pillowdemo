# import required image module
from PIL import Image

# Open an already existing image
imageObject = Image.open("input-images/spiderman.jpg")

# Do a flip of left and right
hori_flippedImage = imageObject.transpose(Image.FLIP_LEFT_RIGHT)

# Show the original image
imageObject.show()

# Show the horizontal flipped image
hori_flippedImage.show()