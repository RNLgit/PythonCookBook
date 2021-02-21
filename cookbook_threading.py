"""
Title : cookbook_threading.py

Description: Cookbook of Python multi threads (threading)

Author: Runnan Li

**Revision History:**

+---------+------------+------------+-----------------------------------------------------+
| Version |     Date   |   Author   |                  Change Description                 |
+---------+------------+------------+-----------------------------------------------------+
|   0.1   | 26/02/2020 | Runnan Li  |                   Initial Version                   |
+---------+------------+------------+-----------------------------------------------------+
"""
import threading
import time, datetime


def threading_basic(arg1):
    """
    Basic threading
    """
    ticking = 0
    while ticking < 10:
        print(datetime.datetime.now().strftime("%H:%M:%S.%f") + ' basic threading running, tick ' + str(ticking))
        ticking += 1
        time.sleep(0.5)


class threading_with_EventObject(threading.Thread):
    """
    Threading that can control starat, stop, resume.
    """
    def __init__(self, event):
        threading.Thread.__init__(self)
        self.stop = event
        self.poolling_interval_s = 1

    def run(self):
        while not self.stop.wait(self.poolling_interval_s):
            print(datetime.datetime.now().strftime("%H:%M:%S.%f") + ' Thread ticking')

    def stop_set(self):
        self.stop.set()


def threading_lambda_control(thread_alive_bool):
    while thread_alive_bool():  # NOTE: use parenthesis here to use lambda as a 'function'
        print(datetime.datetime.now().strftime("%H:%M:%S.%f") + ' Thread ticking')
        time.sleep(0.5)


# Threading example 1, basic threading. Thread need to be finished, cannot kill by coder.
print('########## Threading example 1, basic threading: ##########')
thread_basic_handle = threading.Thread(target=threading_basic, args=(1,))
thread_basic_handle.start()
time.sleep(2)
thread_basic_handle.join()  # wait for a thread to finish it's task

# Threading example 2, using event object which can control thread start, stop easily
print('########## Threading example 2, event object threading: ##########')
thread_handle = threading_with_EventObject(threading.Event())
thread_handle.setDaemon(True)  # set daemon thread where the thread will stop if main program (thread) exits
thread_handle.start()
input('Thread running, press any key to see thread stop effect.\n')
thread_handle.stop_set()
print('Thread shall stopped now\n')
'''
alternatively use
stop_thread = threading.Event()
thread_handle = threading_with_EventObject()
stop_thread.set()
'''

# Threading example 3, using lambda to control thread infinite loop
print('########## Threading example 3, lambda threading: ##########')
thread_manager={'thread_labmda_alive': True}
thread_lambda_handle = threading.Thread(target=threading_lambda_control,
                                        args=(lambda: thread_manager['thread_labmda_alive'], ))
thread_lambda_handle.start()
time.sleep(2)
thread_manager['thread_labmda_alive'] = False


input('press any key to exit')

