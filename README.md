# ICTP_watchdog
왓치독을 활용하여 지정된 폴더에 이미지를 번역해서 띄워준다. 


``` bash
pip install easyocr
pip install kakaotrans
pip install watchdog


option
pip install torch==1.8.1+cu102 torchvision==0.9.1+cu102 torchaudio===0.8.1 -f https://download.pytorch.org/whl/torch_stable.html

pip install torch==1.8.1+cu111 torchvision==0.9.1+cu111 torchaudio===0.8.1 -f https://download.pytorch.org/whl/torch_stable.html
```
config.ini에 스크린샷 저장 폴더 설정

실행
``` bash
python main.py
```

![Screenshot](https://github.com/AjenaEYo/ICTP_watchdog/blob/develop/example/first_test.gif)



로직<br />
이미지캡쳐 프로그램[ShareX](https://getsharex.com/ "ShareX link")이나, 캡쳐한 이미지를 지정폴더에 넣는다.<br />
watchdog에서 생성된 파일 경로를 읽는다<br />
번역하고, text를 이미지에 넣어 출력해준다<br />

[설치가이드로 이동합니다.](./install_guild/README.md)