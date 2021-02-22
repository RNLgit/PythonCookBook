"""
Title : cookbook_commandline.py

Description: Cookbook of Python program that can be called from commandline with arguments

Author: Runnan Li

**Revision History:**

+---------+------------+------------+-----------------------------------------------------+
| Version |     Date   |   Author   |                  Change Description                 |
+---------+------------+------------+-----------------------------------------------------+
|   0.1   | 22/02/2021 | Runnan Li  |                   Initial Version                   |
+---------+------------+------------+-----------------------------------------------------+
"""
import getopt
import sys

__version__ = '0.1'


class Commandline:
    """
    Commandline calling conventions and main function.
    """
    def usage(self):
        """
        Command line call usage of the driver.

        -p       COM port of power supply in COMx format. i.e COM1, COM23 etc.

        -r       * Optional. Baudrate of COM port. Default 115200

        -h, --help    help
        """
        print('\n A typical usage example:')
        print('\n $ cookbook_commandline.py -p COM10 -d 115200\n')
        print('   Call COM port 10 with baud rate 115200')
        print('\nOptions:\n')
        print('-p       COM port of power supply in COMx format. i.e COM1, COM23 etc.\n')
        print('-r       Optional. Baudrate of COM port. Default 115200\n')
        print('-h, --help    help')
        print('\n' + 'cookbook_commandline version: ' + __version__)
        sys.exit(2)

    def main(self, argv):
        """
        Command line calling as main function

        :param argv: see :meth:`usage()`
        """
        com_port = ''  # default port no
        com_baud = 0  # default baud rate

        try:
            opts, args = getopt.getopt(argv[1:], "shp:r:",["help"])
        except getopt.GetoptError as err:
            print(str(err))
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-p':
                com_port = arg
            elif opt == '-r':
                com_baud = int(arg)
            elif opt in ('-h', '--help'):
                print('\nhelp usage')
                self.usage()
            else:
                assert False, "unhandled option"

        print('Commandline get argument: port number ' + str(com_port))
        print('Commandline get argument: baud rate: ' + str(com_baud))


if __name__ == "__main__":
    cmd_call = Commandline()
    cmd_call.main(sys.argv)
