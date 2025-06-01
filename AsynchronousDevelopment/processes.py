import time
from multiprocessing import Process


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

# Processes (from multiprocessing import Process)

process = Process(target=complex_calculation)
process2 = Process(target=complex_calculation)
start = time.time()

process.start()
process2.start()

process.join()
process2.join()

print(f'Two processes total time: {time.time() - start}')
