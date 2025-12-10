import pywhatkit
import os
import json

# path = "D:\\projects\\whatsapp\\images"
path = ".\\images"
xlist = '{"+610413598987":"HitenBhai","+61424493831":"TrishBhai", "+61430249808":"Maheshbhai","+61431791055":"Mr Dipeshbhai","+61466002329":"Dipakbhai", "+61499046634":"Davendrabhai"}'
ylist = json.loads(xlist)

for filename in os.scandir(path):
    if filename.path.endswith('png'):
        # print('files: ')
        # print(filename.name)    
        imgName = filename.name
        phone = imgName.removesuffix('.png')
        filePath = path + '\\' + str(imgName)
        msg = "Jay Swaminarayan " + str(ylist[str(phone)]) + ", We Wish you a Happy Diwali and a Prosporous New Year. \n This is a test message."
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

