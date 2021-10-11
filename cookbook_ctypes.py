"""
Description: Python program that can calls dynamic lib (.dll) that written in C / C++
"""
import ctypes
import os


class CookbookCtypes():
    """
    C compatible data types, and allows calling functions in DLLs or shared libraries
    """
    def __init__(self):
        """
        Load dll to an instance
        """
        self.dll = ctypes.WinDLL(os.path.dirname(os.path.realpath(__file__)) + "\\tcio.dll")

    def read_version(self):
        """
        Example use of load Regatron tcio.dll print out version string
        :return:
        """
        ver = ctypes.c_uint32()  # unsigned int 32 type
        build = ctypes.c_uint32()  # unsigned int 32 type
        sb = ctypes.create_string_buffer(256)  # create array of c_char

        self.dll.DllReadVersion(ctypes.byref(ver), ctypes.byref(build), ctypes.byref(sb))  # dll provided function pass by ref

        print('DLL version:', ver.value >> 16, '.', ver.value & 0xFFFF)  # read ver with internal defined mask
        print('String:', sb.value.decode('utf-8'))  # read string

    def read_current(self):
        current = ctypes.c_double()  # create double type
        self.dll.TC4GetCurrentAct(ctypes.byref(current))  # pass by ref
        print('Current:', current.value)  # use .value attribute to access value read back


if __name__ == "__main__":
    cb = CookbookCtypes()
    cb.read_version()
    cb.read_current()
