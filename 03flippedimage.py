from PIL import Image

imageObject = Image.open("input-images/spiderman.jpg")

# Do a flip of left and right
hori_flippedImage = imageObject.transpose(Image.FLIP_LEFT_RIGHT)

# Show the original image
imageObject.show()

# Show the horizontal flipped image
hori_flippedImage.show()