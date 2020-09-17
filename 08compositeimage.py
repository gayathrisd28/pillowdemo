from PIL import Image, ImageDraw, ImageFilter

im1 = Image.open('input-images/lena.jpg')
im2 = Image.open('input-images/rocket.jpg').resize(im1.size)
im1.show()
im2.show()

# L - stands for grayscale mode , 0 means black in color. 
mask = Image.new("L", im1.size, 0)
draw = ImageDraw.Draw(mask) 
# We draw a circle of diameter 120 
draw.ellipse((140, 50, 260, 170), fill=255)
mask_blur = mask.filter(ImageFilter.GaussianBlur(10))
mask_blur.show()
im = Image.composite(im1, im2, mask_blur)
im.show()