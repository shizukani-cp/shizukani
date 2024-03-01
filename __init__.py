import random, time

uuidlatters = (
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'a', 'b', 'c', 'd', 'e','f'
)
varnamelatters = (
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
        'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd',
        'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
        'y', 'z'
    )
fnamelatters = varnamelatters + ('_', '-', '+', '=', '{', '}', '(', ')')
strings = [chr(int(hex(i), 16)) for i in range(33, 127)]

def randomnum(n:int) -> int:
    return random.randint(10 ** (n - 1), (10 ** n) - 1)

def randomstr(n:int) -> str:
    return "".join(random.choices(strings, k=n))

def randomfname(n:int) -> str:
    return "".join(random.choices(fnamelatters, k=n))

def randomvarname(n:int) -> str:
    return "".join(random.choices(varnamelatters, k=n))

def uuid():
    return "".join(random.choices(uuidlatters, k=32))

class Timer:

    def __init__(self):
        self.mode = -1
        self.stime = 0
        self.time = 0
    
    def getTime(self) -> float:
        return self.time if self.mode != 0 else time.time() - self.stime
    
    def __enter__(self):
        self.stime = time.time()
        self.mode = 0
    
    def __exit__(self, *args):
        self.time = time.time() - self.stime
        self.mode = 1