import time 
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
#import animated

class ExampleHandler(FileSystemEventHandler):
    def __init__(self,q):
        self.q=q
    def on_created(self, event): # when file is created
        # do something, eg. call your function to process the image
        print (f'Got event for file {event.src_path}')

class watchimage:
    def run(self,q, _path):
        observer = Observer()
        event_handler = ExampleHandler(q) # create event handler
        # set observer to use created handler in directory
        observer.schedule(event_handler, path=_path)
        observer.start()

        # sleep until keyboard interrupt, then stop + rejoin the observer
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()

        observer.join()

if __name__ == "__main__":
    a=watchimage()
    a.run(None,None,"C:\\Users\\ajena\\Documents\\ShareX\\Screenshots\\2021-05")