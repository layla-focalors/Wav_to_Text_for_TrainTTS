import os
import speech_recognition as sr
import soundfile
import dotenv
import shutil

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

print(os.environ['isremaked'])

    

# 나중에 절대경로로 변경

fileList = os.listdir('./nilou/wav')
filePath = []
for i in fileList:
    filePath.append('./nilou/wav/' + i)

r = sr.Recognizer()

remaked_store = []

OUTPUT_PATH = 'D:\\닐루_TTS\\IGISS\\output'

# print(filePath)
if os.environ['isremaked'] == '0':
# file ReConverter
    for u in filePath:
        print(u)
        try:
            os.chdir('D:\\닐루_TTS\\IGISS\\')
            data, samplerate = soundfile.read(u)
            remaked = 'D:\\닐루_TTS\\IGISS\\' + u.split('.')[1] + 'neo' + '.wav'
            # print('remaked : ' + remaked)
            os.chdir(OUTPUT_PATH)
            soundfile.write(remaked, data, samplerate, subtype='PCM_16')
            remaked_store.append(remaked)
        except:
            print("Error, BypassFiles : " + u)
    print(remaked_store)
    # file copy to output folder
    
    for x in remaked_store:
        print(x)
        try:
            shutil.copy(x, OUTPUT_PATH)
        except:
            print("An Error Occured, BypassFiles : " + x)
    dotenv.set_key(dotenv_file, "isremaked", "1")
else:
    print("this data is already remaked")

remaked_store = os.listdir(OUTPUT_PATH)

store = []
# print(remaked_store)
for j in remaked_store:
    
    with sr.AudioFile(OUTPUT_PATH + '\\' + j) as source:
        try:
            audio_data = r.record(source)
            text = r.recognize_google(audio_data, language = 'ko-KR', show_all = True )
            print(text)
            store.append('nilou/origin/' + j + '|0|' + text['alternative'][0]['transcript'])
        except:
            print("Error, BypassFiles : " + j)
            store.append('nilou/origin/' + j + '|0|' + '')
            
print(store)