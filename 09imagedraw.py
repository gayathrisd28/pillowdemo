#Import required modules from Pillow package
from PIL import Image, ImageDraw, ImageFont

# get an image
base = Image.open('input-images/tiger.jpg').convert('RGBA')

# make a blank image for the text, initialized to transparent text color
txt = Image.new('RGBA', base.size, (255,255,255,0))

# get a font
fnt = ImageFont.truetype('fonts/pacifico/Pacifico.ttf', 160)

# get a drawing context
d = ImageDraw.Draw(txt)

# draw text, half opacity
d.text((14,14), "Save", font=fnt, fill=(255,255,255,128))

# draw text, full opacity
d.text((14,120), "Tigers", font=fnt, fill=(255,255,255,255))
out = Image.alpha_composite(base, txt)

#Show image
out.show()