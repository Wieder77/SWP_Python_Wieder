import time
import functools
# this is a decorator example
def timer(func):
    @functools.wraps(func)
    def wrapper():
        start_time = time.time()
        print("start Timer")
        func()
        print("Timer laeuft gerade")
        print("end Timer")
        end_time = time.time()
        return (end_time - start_time)
    return wrapper
@timer
def sleep_time():
    time.sleep(10)
if __name__ == "__main__":
    print(f"Die Methode hat {sleep_time()} geschlafen")