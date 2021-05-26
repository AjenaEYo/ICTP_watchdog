import cv2
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class progess:
    def __init__(self):
        self.idlegif = cv2.VideoCapture("resource/idle.gif")
        self.rungif = cv2.VideoCapture("resource/run.gif")
        self.curgif = self.idlegif
    def idle(self):
        self.curgif = self.idlegif
        self.curgif.set(cv2.CAP_PROP_POS_FRAMES, 0)

    def proc(self):
        self.curgif = self.rungif
        self.curgif.set(cv2.CAP_PROP_POS_FRAMES, 0)

    def run(self,q):
        while(True):
            ret,img=self.curgif.read()
            if ret:
                cv2.imshow('state',img)
            else:
                #print('no video')
                self.curgif.set(cv2.CAP_PROP_POS_FRAMES, 0)
            
            key = cv2.waitKey(33) & 0xFF
        
            #state = q.get()

            #print(state)
            
            if(key == ord('i')):
                self.idle()
            if(key == ord('r')):
                self.proc()
        
            if(key == ord('q')):
                break;

if __name__ == "__main__":
    a=progess()
    a.run()