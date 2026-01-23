# CPU bounded tasks are better handled with multiprocessing rather than multithreading due to Python's Global Interpreter Lock (GIL).
import time
import multiprocessing

def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(2)
def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(f"Letter: {letter}")
        time.sleep(2)

if __name__ == '__main__':
    t = time.time()
    print("With Multiprocessing:")
    # Create processes
    number_process = multiprocessing.Process(target=print_numbers)
    letter_process = multiprocessing.Process(target=print_letters)  
    # Start processes
    number_process.start()
    letter_process.start()
    # Wait for both processes to complete
    number_process.join()
    letter_process.join()
    print(f"Time taken with multiprocessing: {time.time() - t} seconds\n")
