import cv2
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

idlegif = cv2.VideoCapture("resource/idle.gif")
rungif = cv2.VideoCapture("resource/run.gif")

curgif = rungif

def idle():
    global curgif
    curgif = idlegif
    curgif.set(cv2.CAP_PROP_POS_FRAMES, 0)

def proc():
    global curgif
    curgif = rungif
    curgif.set(cv2.CAP_PROP_POS_FRAMES, 0)

def run():
    while(True):
        ret,img=curgif.read()
        if ret:
            cv2.imshow('state',img)
        else:
            print('no video')
            curgif.set(cv2.CAP_PROP_POS_FRAMES, 0)
        
        key = cv2.waitKey(33) & 0xFF
       
        
        if(key == ord('i')):
            idle()
        if(key == ord('r')):
            proc()
       
        if(key == ord('q')):
            break;

if __name__ == "__main__":
    run()