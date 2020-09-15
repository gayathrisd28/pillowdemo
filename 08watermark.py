#Import required Image library
from PIL import Image, ImageDraw, ImageFont

#Create an Image Object from an Image
im = Image.open('input-images/scenery.jpeg')
width, height = im.size

draw = ImageDraw.Draw(im)
text = "the watermark"

font = ImageFont.truetype('fonts/arial/Arial.ttf', 36)
textwidth, textheight = draw.textsize(text, font)

# calculate the x,y coordinates of the text
margin = 10
x = width - textwidth - margin
y = height - textheight - margin

# draw watermark in the bottom right corner
draw.text((x, y), text, font=font)
im.show()

#Save watermarked image
im.save('out-images/watermark.jpg')