Pythonic
========

Pythonic means code that doesn't just get the syntax right but that follows the conventions of the Python community and uses the language in the way it is intended to be used.

Threading
^^^^^^^^^

Thread works pseudo parallel in python. Example tackles unspecified workload that can stop thread nicely at any time. 

- class based thread that can turn off by event call
- function based thread that can turn off by lambda function

.. literalinclude:: ../cookbook_threading.py
    :language: python
    :linenos:

Multi-Process
^^^^^^^^^^^^^

Multi-process works true parallel in python. Example demonstrates how to share data between multiple threads.

- Multi-processing
- Exchanging pickleable data between processes using Queue
- Process ID, info etc.

.. literalinclude:: ../cookbook_multiprocess.py
    :language: python
    :linenos:

if-else Redundancy
^^^^^^^^^^^^^^^^^^

Reduce use of if-else and nested if-else statement is a pythonics way.

.. literalinclude:: ../cookbook_ifelse_redundancy.py
    :language: python
    :linenos:

args kwargs
^^^^^^^^^^^

*args and **kwargs allow you to pass multiple arguments or keyword arguments to a function.

.. literalinclude:: ../cookbook_args_kwargs.py
    :language: python
    :linenos: