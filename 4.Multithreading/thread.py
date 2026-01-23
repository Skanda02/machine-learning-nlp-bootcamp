import time
import threading

def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(2)


def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(f"Letter: {letter}")
        time.sleep(2)

# Create threads
number_thread = threading.Thread(target=print_numbers)
letter_thread = threading.Thread(target=print_letters)

t = time.time()
print("With Multithreading:")
number_thread.start()
letter_thread.start()

# Wait for both threads to complete
number_thread.join()
letter_thread.join()

print(f"Time taken with multithreading: {time.time() - t} seconds\n")