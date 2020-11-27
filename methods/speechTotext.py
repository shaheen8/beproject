'''
Created on May 31, 2019

@author: Vinod Bhosale
'''
from gtts import gTTS
import os 
from googletrans import Translator

translator = Translator()
#translator.translate('india is my country')
text=(str)(translator.translate('india is my country', dest='en'))
print('Marathi conversion ::'+text)

language = 'en'
myobj = gTTS(text=text, lang=language, slow=False)
myobj.save("C:\\Users\\shaheen\\Desktop\\input-sign\\welcome.mp3") 
  
# Playing the converted file 
os.system("C:\\Users\\shaheen\\Desktop\\input-sign\\welcome.mp3") 