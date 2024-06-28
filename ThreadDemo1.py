import threading
import time

done = False
def worker():
    c=0
    while not done:
        time.sleep(1)
        print(c)
        c=c+1


threading.Thread(target=worker).start()

input("press enter to exit")
done=True