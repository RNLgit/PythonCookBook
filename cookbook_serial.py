"""
Description: Python Serial communications (PySerial) messaging template
"""
import serial
import time


class SerialCookbook():
    def __init__(self):
        self.serial_handle = serial.Serial
        self.thread_active = True

    def connect(self, port_no, baud, read_timeout=0.1, write_timeout=0):
        """
        Connect a serial port and create instance

        :param port_no: e.g. COM10 in COMxx format of the port
        :param baud: baudrate of serial port
        :param timeout: set a read timeout value
        :param write_timeout: set a write timeout value
        :return:
        """
        try:
            self.serial_handle = serial.Serial(port_no, baud, timeout=read_timeout, write_timeout=write_timeout)
            return True
        except ValueError:
            print('Some parameter are out of range, e.g. baud rate, data bits.')
            return False
        except serial.SerialException:
            print('The device can not be found or can not be configured')
            return False

    def disconnect(self, timeout_s=1):
        """
        Close the already initialized serial port

        :param float timeout_s: timeout allowed to close port successfully
        :return: True of successfully. Otherwise raise TimeoutError
        """
        self.serial_handle.close()
        time_start = time.time()
        while time.time() - time_start < timeout_s:
            if not self.serial_handle.is_open:
                return True  # successfully close serial port
        raise TimeoutError  # not able to close serial port in time

    def query(self, cmd):
        """
        Query a command output with given input from serial comms port. Basic approach with no other protection
        mechanism implemented.

        :param str cmd:
        :return: :meth:`str`
        """
        self.serial_handle.write(cmd.encode('ascii'))
        value_read = self.serial_handle.readline().decode('ascii')
        return value_read

    def query_with_timeout(self, cmd, wait_timeout_s=1):
        """
        Query a command output with given input from serial comms port. A waiting for data timeout is implemented.

        :param str cmd:
        :param float wait_timeout_s: limit of time in second to wait data finished transmission
        :return:
        """
        self.serial_handle.write(cmd.encode('ascii'))
        start_time = time.time()
        while True:
            while self.serial_handle.in_waiting:
                value_read = self.serial_handle.readline()
                return value_read
            if time.time() - start_time > wait_timeout_s:
                print("Serial Read Timeout!")
                return None


    def query_fixed_output(self, cmd, response_len=5):
        """
        Query a command output (fixed lenth) with given input from serial comms port.
        Benefit of this is a faster read time with known response data length.

        :param str cmd:
        :param int response_len: a known fixed response length
        :return: :meth:`str~
        """
        self.serial_handle.write(cmd.encode('ascii'))
        time_start = time.time()
        value_read = ''
        while time.time() - time_start < 1:
            value_read += self.serial_handle.read().decode('ascii')
            if len(value_read) == response_len:
                return value_read
        return None

    def query_EoT_sign(self, cmd, EoT=b'\x03'):
        """
        Query a command output with an expected End of Transmission sign with given input from serial comms port.
        Benefit of this is a faster read time with known end of data sign.

        :param cmd:
        :param EoT: example ascii 3 End of Text sign
        :return: :meth:`byte`
        """
        self.serial_handle.write(cmd.encode('ascii'))
        line = bytearray()
        while True:
            char = self.serial_handle.read()  # if character is there in serial incoming
            if char:
                line += char
                if line[-1:] == EoT:
                    break
            else:
                break
        return bytes(line)

    def query_with_retry(self, cmd, retry_lim=5):
        """
        Query a command output with an expected number of retransmission when something unexpected happened. This is to
        deal with physical connection unstable, lost etc.

        :param str cmd:
        :param int retry_lim:
        :return:
        """
        retry_ct = 0
        while retry_ct < retry_lim:
            try:
                self.serial_handle.write(cmd.encode('ascii'))
                value_read = self.serial_handle.readline().decode('ascii')
                return value_read
            except (serial.SerialException, serial.SerialTimeoutException):
                # 1st close instance
                try:
                    self.disconnect()
                except TimeoutError:  # if timeout in self.disconnect happened
                    print('Do something handle close timeout here')  # do something you want to handle timeout
                except Exception as e:  # if some other exception scenarios we can ignore
                    pass
                # 2nd re connect
                if self.connect():
                    return True
                retry_ct += 1
        raise ConnectionError # if query retry times exhausted, give a connection error

