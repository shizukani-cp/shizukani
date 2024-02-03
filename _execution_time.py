import time

def _execution_time1(func, times=1):
    start = time.time()
    for _ in range(times):
        func()
    return time.time() - start

def _execution_time2(func, argument=(), times=1):
    start = time.time()

    if not argument:
        results = [func(*argument) for _ in range(times)]
        return time.time() - start, results
    else:
        for _ in range(times): func()
        return time.time() - start, []

