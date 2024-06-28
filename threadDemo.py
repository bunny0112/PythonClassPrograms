import _thread
import time

def print_time(thread_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(f"{thread_name}: {time.ctime(time.time())}")

# Create two threads
try:
    _thread.start_new_thread(print_time, ("Thread-1", 2))
    _thread.start_new_thread(print_time, ("Thread-2", 4))
except:
    print("Error: unable to start thread")

# Keep the main thread alive to see the output
while 1:
    pass

