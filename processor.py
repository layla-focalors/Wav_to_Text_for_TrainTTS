import os
import speech_recognition as sr
import soundfile
import dotenv

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

else:
    print("this data is already remaked")

# for j in remaked_store:
#     data, samplerate = soundfile.read(j)
#     remaked = j.split('.')[0] + 'neo' + '.wav'
#     soundfile.write(remaked, data, samplerate, subtype='PCM_16')
    
#     with sr.AudioFile(j) as source:
        
#         audio_data = r.record(source)
#         text = r.recognize_google(audio_data)
#         print("Audio File : " + j + '\noutput : ' + text)
