import pywhatkit
import os

path = "D:\\projects\\whatsapp\\images"

for filename in os.scandir(path):
    if filename.path.endswith('png'):
        # print('files: ')
        # print(filename.name)    
        imgName = filename.name
        phone = imgName.removesuffix('.png')
        filePath = path + '\\' + str(imgName)
        # print('file path: ', filePath)
        pywhatkit.sendwhats_image(phone, filePath,"hello how are you")
        
        
        # if os.path.isfile(f):
        #     print('files: ')
        #     print(f)
        #     pywhatkit.sendwhats_image(receiver, img_path)

# pywhatkit.sendwhatmsg_instantly('+61413598987', 'hello')



# pywhatkit.sendwhats_image("+61413598987", "D:\\projects\\whatsapp\\test.png","test img")
# pywhatkit.sendwhats_image("+61452426758"+61413598987, "D:\\projects\\whatsapp\\test.png","test img")

