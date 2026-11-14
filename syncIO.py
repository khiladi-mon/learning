import time

start_time = time.perf_counter()

def task1():
    print("Task 1 started")
    time.sleep(3)
    print("Task 1 finished")

def task2():
    print("task 2 started")
    time.sleep(2)
    print("task 2 finished")



task1()
task2()

end_time = time.perf_counter()
elapsed_time = end_time - start_time

print(f"Program finished in {elapsed_time:.4f} seconds")
