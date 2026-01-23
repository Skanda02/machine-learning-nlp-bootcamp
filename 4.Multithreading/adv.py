# Multithreading with thread pool executor
import time
from concurrent.futures import ThreadPoolExecutor   

def print_numbers(numbers):
    time.sleep(1)
    return f"numbers {numbers}"

numbers = [1,2,3,4,5,6,7,8,9,10,11,12]

with ThreadPoolExecutor(max_workers=2) as executor:
    results = executor.map(print_numbers, numbers)

for result in results:
    print(result)