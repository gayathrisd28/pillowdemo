from PIL import ImageEnhance, Image

img = Image.open('input-images/tulip.jpg')
img.show()
#
colorenhancer = ImageEnhance.Color(img)

colorenhancer.enhance(0.25).show()

contrastenhancer = ImageEnhance.Contrast(img)
contrastenhancer.enhance(2).show()

brightenhancer = ImageEnhance.Brightness(img)
brightenhancer.enhance(2.0).show()

enhancer = ImageEnhance.Sharpness(img)
enhancer.enhance(0.5).show()

