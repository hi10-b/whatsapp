from re import I
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


img = Image.open('.\\images\\+61424493831.png')

# myFont = ImageFont.truetype(font=None, size=65)
 
# Add Text to an image

I1 = ImageDraw.Draw(img)
I1.text((800,100), "hello world", font=(ImageFont.truetype(font="arial.ttf",size=100)) ,fill =(255, 0, 0))

# I1.text((800,100), "hello world", font=myFont,fill=(255, 0, 0))

img.save('.\\updated\\updated.png')