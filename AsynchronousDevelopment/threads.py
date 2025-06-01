import time
from threading import Thread


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

# Threads (from threading import Thread)

thread1 = Thread(target=complex_calculation)
thread2 = Thread(target=ask_user)

start = time.time()

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f'Two threads total time: {time.time() - start}')
