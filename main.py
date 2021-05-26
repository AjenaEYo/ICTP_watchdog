import configparser
from multiprocessing import Process,freeze_support
import multiprocessing
from platform import version
import watchimage
import animated


if __name__ == '__main__':
    freeze_support()
    progess = animated.progess()
    vision = 0
    watchimg = watchimage.watchimage()
    config = configparser.ConfigParser()
    config.read('config.ini')

    capture_path = config['DEFAULT']['CAPTURE_PATH']

    print(capture_path)

    procs = []
    #watch = Process(target=watchimg.run, args=(progess,vision,capture_path,)) 
    q = multiprocessing.Queue()
    watch = Process(target=watchimg.run, args=(q,capture_path,)) 
    watch.daemon = True
    procs.append(watch) 
    watch.start()

    progess.run(q)
    # progess = Process(target=animated.run, args=(None,None,)) 
    # procs.append(progess) 
    # progess.start()
    
    for proc in procs: 
        proc.join()
