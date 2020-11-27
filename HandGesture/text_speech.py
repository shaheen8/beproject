from gtts import gTTS
import os




def audio(self,audiopath):
   
    print ('textfilepath in texttospeech class= '+audiopath)
    img=os.path.join(audiopath)
    file=img
    t = open(file,'r')
    r=t.read()

    tts = gTTS(text=r, lang='en')
    #path4='/home/admin1/workspace/TextToSpeech/data/'
   
    tts.save("C:\\Users\\shaheen\\Desktop\\input-sign\\abc.mp3")
    os.system("C:\\Users\\shaheen\\Desktop\\input-sign\\abc.mp3")
    
    ####################################################################
