# IO bound tasks
'''
An I/O-bound task is a task where:
The program waits for data from external resources
CPU is mostly idle while waiting
Performance is limited by disk, network, or database speed
Examples of external resources:
Files
Network requests
Databases
APIs
User input
'''
import threading
import time


def task():
    print("Task started")
    time.sleep(3)
    print("tasks Completed")

task()
task() #total time taken is 6sec

#Using Threading concept
def task():
    print("Task started")
    time.sleep(3)
    print("Task Completed")

t1= threading.Thread(target= task())
t2 = threading.Thread(target=task())

t1.start()
t2.start()

t1.join()
t2.join()

# fetch the api details
def fetch_data(api_name):
    print(f"fetching from {api_name}")
    time.sleep(2)
    print(f"completed {api_name}")

apis = ["API1", "API2", "API3"]
threads = []

for api in apis:
    t = threading.Thread(target=fetch_data, args=(api,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All the API calls completed")


# file reading
def read_file(filename):
    with open(filename, "r") as f:
        data = f.read()
        print(f"{filename} read completed")

files = ["file1.txt", "file2.txt"]
file_threads = []

for file in files:
    t = threading.Thread(target=read_file, args=(file,))
    file_threads.append(t)
    t.start()

for t in file_threads:
    t.join()