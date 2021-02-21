from multiprocessing import Process, Queue
import os, time, random
import threading


def tx_th(q, p_name):
    q_ct = 0
    q_ct_lim = 5
    while q_ct < q_ct_lim:
        rdm = random.randrange(0, 100, 1)
        q.put(rdm)
        time.sleep(rdm/100)
        q_ct += 1
    print(p_name, ' queue read finished')


def pcs(p_name, q_tx, q_rx):
    info(p_name)
    print(p_name, ' Running')
    putting_th = threading.Thread(target=tx_th, args=(q_tx, p_name))
    putting_th.start()
    while putting_th.is_alive():
        print(p_name, ' get: ', q_rx.get(timeout=1), ' from another process')
    putting_th.join()



def info(p_name):
    print(p_name, ': module name:', __name__)
    print(p_name, ': parent process id:', os.getppid())
    print(p_name, ': this process id:', os.getpid())


if __name__ == '__main__':
    q_1_2 = Queue()
    q_2_1 = Queue()
    p1 = Process(target=pcs, args=('Process 1', q_1_2, q_2_1))
    p2 = Process(target=pcs, args=('Process 2', q_2_1, q_1_2))
    print('Main process ID:', os.getpid())

    # start process
    p1.start()
    p2.start()

    # wait for process to finish
    p1.join()
    print('P1 joined')
    p2.join()
    print('P2 joined')

    # Done
    print('ok')
