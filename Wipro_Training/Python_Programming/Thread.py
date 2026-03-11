import threading
import time

def task():
    print("Thread started")
    time.sleep(2)
    print("Thread finished")

# Create a thread
t = threading.Thread(target=task)
t.start()
t.join()  # Wait for the thread to finish
print("thread terminated")
