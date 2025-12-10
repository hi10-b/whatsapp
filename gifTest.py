import pywhatkit
import os
import json

# path = "D:\\projects\\whatsapp\\images"
path = ".\\gifTest\\out.gif"
xlist = '{"+610413598987":"HitenBhai","+61424493831":"TrishBhai", "+61430249808":"Maheshbhai","+61431791055":"Mr Dipeshbhai","+61466002329":"Dipakbhai", "+61499046634":"Davendrabhai"}'
ylist = json.loads(xlist)
imgName = path


     
phone = "+61413598987"
filePath = path + '\\' + str(imgName)
msg = "Jay Swaminarayan , We Wish you a Happy Diwali and a Prosporous New Year. \n This is a test message."
# print('file path: ', filePath)
pywhatkit.sendwhats_image(phone, path,msg, 15, True, 2)
        
    

