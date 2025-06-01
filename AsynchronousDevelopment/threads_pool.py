import time
from concurrent.futures import ThreadPoolExecutor


def ask_user():
    start_time = time.time()
    user_input = input('Enter your name: ')
    greet = f'Hello {user_input}'
    print(greet)
    print(f'ask_user, {time.time() - start_time}')


def complex_calculation():
    start_time = time.time()
    print('Starting complex calculation...')
    var = [x ** 2 for x in range(2 * 10 ** 7)]
    var += []
    print(f'complex_calculation, {time.time() - start_time}')


# start = time.time()
# ask_user()
# complex_calculation()
# print(f'Single thread total time: {time.time() - start}')

# Threads (from concurrent.futures import ThreadPoolExecutor)

start = time.time()

with ThreadPoolExecutor(max_workers=2) as pool:
    pool.submit(complex_calculation)
    pool.submit(ask_user)

print(f'Two threads total time: {time.time() - start}')
