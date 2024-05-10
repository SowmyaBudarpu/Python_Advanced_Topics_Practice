'''
    To create a timer using the threading module in Python, you can utilize the Timer class. 
    The Timer class allows you to execute a function after a specified delay. 
    Here's an example:
'''
import threading

def safe_repeating_timer_callback(counter):
    if counter > 0:
        print(f"Timer tick! Counter: {counter}")
        threading.Timer(5, safe_repeating_timer_callback, args=(counter - 1,)).start()
    else:
        print("Final tick!")

# Start the timer with an initial counter value
initial_counter = 3
timer = threading.Timer(5, safe_repeating_timer_callback, args=(initial_counter,))
timer.start()

print("Doing other tasks...")

# Assuming we want to wait for all ticks to complete
while timer.is_alive():
    timer.join(5)

print("Timer sequence finished.")
