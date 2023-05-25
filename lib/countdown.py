import time

def countdown(i):
    while i >= 1:
        print(f'{i} SECOND(S)!')
        i -= 1
    print('HAPPY NEW YEAR!')

# countdown(10)

def countdown_with_sleep(i):
    while i >= 1:
        print(f'{i} SECOND(S)!')
        i -= 1
        time.sleep(1)
    print('HAPPY NEW YEAR!')