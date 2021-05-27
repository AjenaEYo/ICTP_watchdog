import time 
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from translate import trans
from translate_story import trans_story
import threading

def work(path,q):
    a=trans_story()
    a.run(path,q)

class ExampleHandler(FileSystemEventHandler):
    def __init__(self,q):
        self.q=q
    def on_created(self, event): # when file is created
        # do something, eg. call your function to process the image
        print (f'Got event for file {event.src_path}')
        self.q.put(1)
        t1 = threading.Thread(target=work,args=(event.src_path, self.q))
        t1.start()
        # a=trans_story()
        # a.run(event.src_path,self.q)
        #b=trans()
        #b.run(event.src_path,self.q)
        #self.q.put(0)

class watchimage:
    is_run=True
    lock = threading.Lock()
    def run(self,q, _path):
        self.observer = Observer()
        event_handler = ExampleHandler(q) # create event handler
        # set observer to use created handler in directory
        self.observer.schedule(event_handler, path=_path)
        self.observer.start()

        # sleep until keyboard interrupt, then stop + rejoin the observer
       
        while True:
            self.lock.acquire()
            if self.is_run: ### 스탑이 왜 동작을 안할까..?
                #print("run")
                time.sleep(1)
            else:
                print("stop")
                break
            self.lock.release()
        
            
        
        self.observer.stop()
        self.observer.join()
    
    def stop(self):
        self.lock.acquire()
        self.is_run=False
        print("False")
        self.lock.release()


if __name__ == "__main__":
    a=watchimage()
    a.run(None,None,"C:\\Users\\ajena\\Documents\\ShareX\\Screenshots\\2021-05")