import pywhatkit
import os

path = ".\\images"
# path = "D:\\projects\\whatsapp\\images"
phoneNum = "+61123456789" #dummy number

for filename in os.scandir(path):
    if filename.path.endswith('png'):
        # print('files: ')
        # print(filename.name)    
        imgName = filename.name
        phone = imgName.removesuffix('.png')
        filePath = path + '\\' + str(imgName)
        # print('file path: ', filePath)
        pywhatkit.sendwhats_image(phoneNum, ".\\images\\aa.gif","hello how are you")
        # pywhatkit.sendwhats_image(phone, filePath,"hello how are you")
        
        
        # if os.path.isfile(f):
        #     print('files: ')
        #     print(f)
        #     pywhatkit.sendwhats_image(receiver, img_path)

# pywhatkit.sendwhatmsg_instantly(phoneNum, 'hello')



# pywhatkit.sendwhats_image(phoneNum, "D:\\projects\\whatsapp\\test.png","test img")
# pywhatkit.sendwhats_image(phoneNum, "D:\\projects\\whatsapp\\test.png","test img")

