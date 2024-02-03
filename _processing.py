from concurrent.futures import ProcessPoolExecutor

def processing(*funcs, max_workers=None):
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        for func in funcs:
            executor.submit(func)

import multiprocessing
def processing2(*funcs, arg : iter):
    if not arg:
        arg = [None for _ in range(len(funcs))]
    with multiprocessing.Pool(processes=len(funcs)) as pool:
        for func in funcs:
            pool.map(func, arg)
