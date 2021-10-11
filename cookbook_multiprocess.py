"""
Description: Python multi processing cookbook template

+---------+------------+------------+-----------------------------------------------------+
| Version |     Date   |   Author   |                  Change Description                 |
+---------+------------+------------+-----------------------------------------------------+
|   0.1   | 22/02/2021 |    R Li    |                   Initial Version                   |
+---------+------------+------------+-----------------------------------------------------+
"""
from multiprocessing import Process, Queue
import threading
import os, time, random


def tx_th(q, p_name):
    """
    Data sharing (sending) thread to another processes

    :param q: :meth:`Queue` method that a thread populating data to a queue
    :param p_name: the Process name that tx data to another thread (Debugging message use)
    :return:
    """
    q_ct = 0
    q_ct_lim = 5
    while q_ct < q_ct_lim:  # Loop for couple of times. customizable on need.
        rdm = random.randrange(0, 100, 1)
        time.sleep(rdm / 100)
        q.put({'time': rdm, 'count': q_ct})  # populate to transmit queue
        q_ct += 1
    q.put('stop')  # stop flag to notice rx thread in another process that done
    print(p_name, 'tx thread finished')


def rx_th(q, p_name):
    """
    Data sharing (receiving) thread from another process

    :param q: :meth:`Queue` method that a thread grab data from a queue
    :param p_name: the Process name that rx data from another thread (Debugging message use)
    :return:
    """
    stop_flg = False
    while not stop_flg:
        data = q.get()
        print(p_name, 'get:', data)
        if 'stop' == data:
            stop_flg = True
    print(p_name, 'rx thread finished')


def pcs(p_name, q_tx, q_rx):
    """
    The new process working function. Put what work you want new process to do

    :param p_name: the Process name (Debugging message use)
    :param q_tx: the transmit queue obj this process is using
    :param q_rx: the receiving queue obj this process is using
    :return:
    """
    info(p_name)  # Print this process info
    print(p_name, 'Running')
    putting_th = threading.Thread(target=tx_th, args=(q_tx, p_name))  # spawn data sending thread
    putting_th.start()
    getting_th = threading.Thread(target=rx_th, args=(q_rx, p_name))  # spawn data receiving thread
    getting_th.start()

    # main works this new process need to do
    pass

    # Wait tx rx thread to finish and shuts properly
    putting_th.join()
    getting_th.join()


def info(p_name):
    """
    Show info of a process

    :param p_name: Process name for debugging print use
    :return:
    """
    print(p_name, ': module name:', __name__)
    print(p_name, ': parent process id:', os.getppid())
    print(p_name, ': this process id:', os.getpid())


if __name__ == '__main__':
    """
    Main thread is needed
    """
    q_1_2 = Queue()
    q_2_1 = Queue()
    p1 = Process(target=pcs, args=('Process 1', q_1_2, q_2_1))  # spawn Process 1
    p2 = Process(target=pcs, args=('Process 2', q_2_1, q_1_2))  # spawn Process 2
    print('Main process ID:', os.getpid())

    # start process
    p1.start()
    p2.start()

    # wait for process to finish
    p1.join()
    print('P1 joined')
    p2.join()
    print('P2 joined')
