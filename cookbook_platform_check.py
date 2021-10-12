"""
The script checks the OS platform that current py env running on
"""

import platform

if 'Darwin' == platform.system():
    print('macOS operating system')
elif 'Windows' == platform.system():
    print('Windows operating system')
elif 'Linux' == platform.system():
    print('Linux operating system')
