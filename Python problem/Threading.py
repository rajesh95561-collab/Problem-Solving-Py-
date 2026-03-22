import threading

balance = 200

lock = threading.Lock()

def deposit(amount,times,lock):
    global balance
    for _ in range(times):
        lock.acquire()
        balance += amount
        lock.release()

def withdraw(amount,times,lock):
    global balance
    for _ in range(times):
        lock.acquire()
        balance -= amount
        lock.release()

deposit_thread = threading.Thread(target=deposit, args=[balance,100000,lock])
withdraw_thread = threading.Thread(target=withdraw,args=[balance,100000,lock])

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()

print(balance)