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


t = time.time()
print("Without Multithreading:")
print_numbers()
print_letters()
print(f"Time taken without multithreading: {time.time() - t} seconds\n")