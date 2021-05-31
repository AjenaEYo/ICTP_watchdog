by chucksal-tp(https://github.com/chucksal-tp)

[참고](https://github.com/AjenaEYo/ICTP_watchdog/blob/main/install_guild/ICTP_watchdog-%EC%85%8B%ED%8C%85%20%EB%B0%A9%EB%B2%95.txt)

ICTP_watchdog 셋팅 방법

1. Python 설치(python379-install.png 사진 참조)
Python 3.7.9 64bit에서 작성(https://www.python.org/downloads/release/python-379/)
(https://www.python.org/ftp/python/3.7.9/python-3.7.9-amd64.exe)
(설치 처음 실행 화면 맨 하단의 path 설정 체크 박스 체크 할 것!)

2. pip 설치(cmd 창에서 실행)
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py

3. 필수 패키지 설치(cmd 창에서 실행)
pip install easyocr
pip install kakaotrans
pip install watchdog

4. CUDA 10.2 버전 이상 설치(4, 5번 항목은 easyocr gpu에서 돌릴려면 진행)
CUDA 10.2 Download : https://developer.download.nvidia.com/compute/cuda/10.2/Prod/local_installers/cuda_10.2.89_441.22_win10.exe
버전별 검색 링크 : https://developer.nvidia.com/cuda-toolkit-archive
설치 진행시 "사용자 정의 설치"를 선택하여, 드라이버는 체크 해제한후 나머지만 설치 진행
(cuda install-01, 02.png 사진 참조)

5. cuda 버전 맞춰서 설치(https://pytorch.org/  참고)
cuda 10.2 설치시 아래 명령어 입력(cmd 창에서 실행)
pip install torch==1.8.1+cu102 torchvision==0.9.1+cu102 torchaudio===0.8.1 -f https://download.pytorch.org/whl/torch_stable.html

6. ICTP_watchdog 다운로드(cmd 창에서 실행 - ICTP_watchdog를 저장할 위치에서 실행)
git clone https://github.com/AjenaEYo/ICTP_watchdog

7. config.ini 수정(스크린샷이 저장되는 경로 지정)
스크린샷 저장되는 경로 지정(해당 경로에 이미지가 추가될 때 번역 실행)

8. ShareX 설치
공식 버전 : https://getsharex.com/
================================================================================<br />
사용 방법
1. ShareX.exe 실행
2. shareX_ocr-초기 셋팅-01, 02.png 를 참조하여 설정 변경
  2-1. "촬영 뒤 할 일"-> "이미지를 파일로 저장하기" 만 활성화[나머지 전부 비활성화]
  2-2. "프로그램 설정"->경로->"사용자 지정 스크린샷 폴더 사용" 체크 후 경로 지정
       "하위 폴더명 패턴" 내용 삭제
       (해당 경로는 위 "ICTP_watchdog 셋팅 방법" 7번 항목의 경로와 일치 해야함)

3. Ctrl + Print Screen 눌러 캡쳐 기능 활성화 후 
  마우스 드래그로 번역할 영역 지정하여 캡쳐

4. 로딩 화면 이후 번역 화면 출력
================================================================================<br />
참고 사항
스크린샷이 저장되는 경로의 파일은 계속 누적되어 쌓임.
용량이 계속 늘어나기 때문에 사용후 직접 삭제 해야 됨.

================================================================================<br />
사용자 설정(직접 코드 수정 하여 사용할 경우에만 참고)

>> translate_story.py (번역 글자 가로줄 사이즈 조절)
아래 내용중 width 부분에 숫자 변경

lines = textwrap.wrap(text, width=30)
