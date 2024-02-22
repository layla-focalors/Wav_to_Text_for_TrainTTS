## Infomation
- **Author**: [Layla-focalors]

## Description
이 레포지트리는 AI TTS 학습에 필요한 텍스트를 전처리하는 레포지트리입니다.  

## How to use
0. remove file in wav folder (nilou / wav) & output folder
1. `pip install -r requirements.txt`
2. chage `processor.py` file output path
3. `python processor.py`

## Warning
이 시스템은 구글의 recognition API를 통해 구축되었지만, 그로 인해 퀄리티가 낮은 STT가 발생하는 경우가 많습니다. 
이는 녹음된 환경 , 오디오의 미세한 잡음으로 인한 오류이기에 오디오의 퀄리티를 높게 구해주시길 바랍니다.  
현재 개발자인 저는 원신의 오디오셋을 구해 사용하였습니다. (들리는 것보다 낮을 수 있음)