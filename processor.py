import os

# 나중에 절대경로로 변경

fileList = os.listdir('./nilou/wav')
filePath = []
for i in fileList:
    filePath.append('./nilou/wav/' + i)
    
print(filePath)