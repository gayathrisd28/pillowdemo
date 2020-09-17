from PIL import Image
image = Image.open('input-images/stockpic.jpg')

# Save in BMP format
image.save('out-images/stockpic.bmp') # if no format is specified, it uses the file extension for output format
image.save('out-images/stockpic.gif', 'GIF') 

# Open and show the saved images
image1 = Image.open('out-images/stockpic.bmp')
image1.show()
image2 = Image.open('out-images/stockpic.gif')
image2.show()