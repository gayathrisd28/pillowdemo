#Import required modules from Pillow package
from PIL import Image, ImageDraw, ImageFont

# convert image to true color with transparancy mask
base = Image.open('input-images/tiger.jpg').convert('RGBA')

# make a blank image for the text, initialized to transparent text color
mask = Image.new('RGBA', base.size, (255,255,255,0))

# get a font
fnt = ImageFont.truetype('fonts/pacifico/Pacifico.ttf', 160)

# create an object to draw on the image 'txt'
d = ImageDraw.Draw(mask)

# draw text, half opacity
d.text((14,14), "Save", font=fnt, fill=(255,255,255,128))

# draw text, full opacity
d.text((14,120), "Tigers", font=fnt, fill=(255,255,255,255))
base.show()
mask.show()
# Adds the image txt over the image base
out = Image.alpha_composite(base, mask)

#Show image
out.show()