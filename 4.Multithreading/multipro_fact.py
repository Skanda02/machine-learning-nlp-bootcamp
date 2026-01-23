# "Calculating factorials using multiprocessing for improved performance. when dealing with large numbers."

import multiprocessing
import math
import time
import sys # sys module is imported to set recursion limit if needed

# Increse the maximum recursion limit if necessary
sys.set_int_max_str_digits(1000000)

# Function to calculate factorial
def calculate_factorial(n):
    print(f"Calculating factorial of {n}")
    result = math.factorial(n)
    print(f"Factorial of {n} is calculated.")
    return result

if __name__ == '__main__':
    numbers = [5000, 6000, 7000, 8000]
    # numbers = [5000000, 6000000, 7000000, 8000000]  # List of large numbers to calculate factorials for
    # 168.70723 sec 
    start_time = time.time()

    # Create a pool of processes
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        # Map the calculate_factorial function to the list of numbers
        results = pool.map(calculate_factorial, numbers)

    end_time = time.time()

    print(f"Factorials calculated for numbers: {numbers}")
    print(f"Time taken: {end_time - start_time} seconds")
