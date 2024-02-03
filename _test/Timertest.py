from shizukani import Timer

def func():
    print("call")
    """for _ in range(10000):
        print("f**k you")"""
    
timer = Timer()

print(timer.getTime())

with timer:
    for _ in range(5):
        func()
        print(timer.getTime())

print(timer.getTime())