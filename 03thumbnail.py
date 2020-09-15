from PIL import Image

image = Image.open('input-images/panda.jpg')
image.show()
image.thumbnail((160,160))
image.save('out-images/pandathumbnail.jpg')
image1 = Image.open('out-images/pandathumbnail.jpg')
image1.show()