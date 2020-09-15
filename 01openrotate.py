from PIL import Image
#Open image using Image module
im = Image.open("input-images/stockpic.jpg")
#Show actual Image
im.show()
#Show rotated Image
im = im.rotate(45)
im.show()