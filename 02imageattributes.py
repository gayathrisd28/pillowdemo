from PIL import Image

image = Image.open('input-images/stockpic.jpg')

print("Name: " + image.filename)
print("Format: " + image.format)
print("Mode: " + image.mode)
print('Size: {0}'.format(image.size))
print("Width:",image.width)
