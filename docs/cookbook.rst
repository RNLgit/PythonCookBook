Cookbook
========

Recepie of some best practice templates.

Serial
^^^^^^

Serial provides example of serial connection and couple of way to query response.

- Connection
- Disconnection
- Basic Query
- Query with timeout
- Query with fixed (expected length) output
- Query with ascii EoT (End of Transmission) sign
- Query with reconnection mechanism

.. literalinclude:: ../cookbook_serial.py
    :language: python
    :linenos:

TCP/IP
^^^^^^

TCP/IP creates both server and client side example of TCP/IP connection that can perform 1-to-1 communication

Server side features:

- open server (Win & Linux)
- listen request from client
- send back response to client
- back to listen connection after client drop

Client side features:

- server connection
- send command to server
- pickleable data

.. literalinclude:: ../cookbook_tcp_ip.py
    :language: python
    :linenos:

Ctypes
^^^^^^

C compatible data types, and allows calling functions in DLLs or shared libraries

- Init dll
- C type variable type
- C type char array
- Pass by ref

.. literalinclude:: ../cookbook_ctypes.py
    :language: python
    :linenos:

XML
^^^

Instance of read write .xml that can use for local parameter storage use.

.. literalinclude:: ../cookbook_saveloadxml.py
    :language: python
    :linenos:

Commandline Calling
^^^^^^^^^^^^^^^^^^^

Module that enables python accept commandline inupt variables.

.. literalinclude:: ../cookbook_commandline.py
    :language: python
    :linenos:

CAN Translator
^^^^^^^^^^^^^^

When a device control not available for CAN control, use this template as a CAN node emulator that accepts CAN message and controls the device correspondingly. 

- Utilising Vector_CAN_API (or python-can) module
- Simplified with minimum use of if-else or nested if-else

.. literalinclude:: ../cookbook_CANtranslator.py
    :language: python
    :linenos:
