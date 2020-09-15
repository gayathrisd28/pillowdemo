from PIL import Image
image = Image.open('input-images/stockpic.jpg')
#image.show()
image.save('out-images/stockpic.bmp') # if no format is specified, it uses the file extension for output format 
image1 = Image.open('out-images/stockpic.bmp')
image.save('out-images/stockpic.gif', 'GIF')
image1.show()
image2 = Image.open('out-images/stockpic.gif')
image2.show()