import cv2
import os
from threading import Thread
os.chdir(os.path.dirname(os.path.abspath(__file__)))



class progess:
    def __init__(self,q):
        self.idlegif = cv2.VideoCapture("resource/idle.gif")
        self.rungif = cv2.VideoCapture("resource/run.gif")
        self.curgif = self.idlegif
        self.q=q

    def idle(self):
        self.curgif = self.idlegif
        self.curgif.set(cv2.CAP_PROP_POS_FRAMES, 0)

    def proc(self):
        self.curgif = self.rungif
        self.curgif.set(cv2.CAP_PROP_POS_FRAMES, 0)
    def work(self):
        while(True):
            state=self.q.get()
            print(state)
            if state == 0:
                self.idle()
            elif state == 1:
                self.proc()
            elif state == 2:
                break

        return
        
        
    def run(self):
        t1 = Thread(target=self.work)
        t1.start()
        while(True):
            ret,img=self.curgif.read()
            if ret:
                cv2.imshow('state',img)
            else:
                #print('no video')
                self.curgif.set(cv2.CAP_PROP_POS_FRAMES, 0)
            
            key = cv2.waitKey(33) & 0xFF
            if(key == ord('q')):
                self.q.put(2)
                break;
 
        t1.join()

if __name__ == "__main__":
    a=progess()
    a.run()