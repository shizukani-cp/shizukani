import threading
from shizukani.randoms import randomstr

class Threading(threading.Thread):
    
    def __init__(self, thread_name:str, thread_num:int, func, lock=threading.Lock(), arg=True, daemon=True):
        self.thread_name = thread_name
        self.thread_num = thread_num
        self.runfunc = func
        self.lock = lock
        self.arg = arg
        super().__init__(target=self.runfunc, daemon=daemon)
    
    def __str__(self):
        return self.thread_name
    
    def __int__(self):
        return self.thread_num
    
    def __lock__(self):
        return self.lock
    
    def run(self):
        if self.arg:
            self.runfunc(self.thread_num, self.lock) 
        else:
            self.runfunc()

def threading_run(func, threads_num : int):
    threads = []
    for i in range(threads_num):
        thread = Threading(randomstr(10), i, func)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()