from time import sleep, perf_counter
from threading import Thread, current_thread, enumerate

def show(name):
    print(f'{name} started.')
    print(current_thread().name, ' is running.')
    sleep(3)
    print(f'{name} finished.')

def print_alive_threads():
    print('Current threads alive:', enumerate())

start = perf_counter()

t1 = Thread(target=show, args=('One',), name='First')
t2 = Thread(target=show, args=('Two',), name='Second')

t1.start()
t2.start()

# Print the threads that are currently active
print_alive_threads()

# Wait for both threads to complete
t1.join()
t2.join()

end = perf_counter()

print('All threads have completed.')
print(f'Total time: {end - start:.2f} seconds')
