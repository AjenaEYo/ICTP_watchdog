import cv2
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

idlegif = cv2.VideoCapture("idle.gif")
rungif = cv2.VideoCapture("run.gif")

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
            
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if cv2.waitKey(1) & 0xFF == ord('i'):
            idle()

        if cv2.waitKey(1) & 0xFF == ord('r'):
            proc()

if __name__ == "__main__":
    run()