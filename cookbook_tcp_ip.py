"""
Title : cookbook_tcp_ip.py

Description: Cookbook of Python TCP/IP communications (socket)

Author: Runnan Li

**Revision History:**

+---------+------------+------------+-----------------------------------------------------+
| Version |     Date   |   Author   |                  Change Description                 |
+---------+------------+------------+-----------------------------------------------------+
|   0.1   | 22/02/2021 | Runnan Li  |                   Initial Version                   |
+---------+------------+------------+-----------------------------------------------------+
"""
import socket
import pickle
import time


class TCPIPServer:
    """
    This server always runs and wait for one client's connection. After successful connection made, will constantly
    listen to client's command request. When connection lost, will back to listen mode listening for next connection.

    Note: pickle of text in comms channel is used here for a good implementation of design for future.
    """
    def __init__(self):
        self.server_ip = ''
        self.server_port = 5005  # or any port number which is not used
        self.sock = socket.socket
        self.conn = socket.socket
        self.address = socket.socket
        self.Rx_Buffer_Size = 65535
        self.server_alive = True

    def get_server_ip(self):
        """
        1st get server's public ip address
        """
        self.server_ip = socket.gethostbyname(socket.gethostname())  # get windows machine local host IP
        # Linux_TCP_IP = subprocess.getoutput('hostname -I').strip()

    def wait_for_connection(self, ip, port):
        """
        Wait for client to connect server. Also use for re-connection when lost.

        :param ip:
        :param port:
        :return:
        """
        self.server_ip = ip
        self.server_port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # set the socket option to reuse the address to 1 (on/true)
        self.sock.bind((self.server_ip, self.server_port))
        print("Waiting for client machine connection")
        self.sock.listen(1)
        self.conn, self.address = self.sock.accept()
        print("Client machine connection accepted, connection accepted from:", self.address)

    def server_run(self):
        """
        normal server run loop after connection successfully established

        :return:
        """
        while self.server_alive:
            try:
                data = self.conn.recv(self.Rx_Buffer_Size)
            except Exception as e:
                print('TCP data receive error, connection broken')
                continue
            if not data:
                self.sock.close()
                print('connection lost, socket closed')
                self.wait_for_connection(self.server_ip, self.server_port)
                continue
            try:
                cmd = pickle.loads(data)  # unpickle TCP transmission data, into dictionary form
                print('command data: ' + str(cmd))
                if 'command1' in cmd:
                    pass  # do something when received command1
                    self.conn.send('ack:command1'.encode('ascii'))  # reply ack
                elif 'command2' in cmd:
                    pass  # do something when received command2
                    self.conn.send('ack:command2'.encode('ascii'))
            except pickle.UnpicklingError:
                print('Error, pickle data was truncated and incomplete')
                print(data)
                self.conn.send('nak'.encode('ascii'))  # send data from server to client
            except KeyError as e:
                print('Unrecognized dictionary key: ' + str(e))


class TCPClient:
    def __init__(self):
        self.ip = ''
        self.port = int()
        self.port = int()
        self.sock = socket.socket

    def connect_to_server(self, ip, port):
        """
        Connect server with known IP address and port number.
        """
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.sock.connect((self.ip, self.port))
            print('Successful connected server: ' + str(self.ip) + ' Port: ' + str(self.port))
            return True
        except TimeoutError:
            print('Time out connecting ' + str(self.ip) + ' Port: ' + str(self.port))
            return False

    def disconnect(self):
        """
        client disconnect from server

        :return:
        """
        self.sock.close()

    def send_command(self):
        """
        send command to server.

        :return:
        """
        pickle_cmd = pickle.dumps({'command1': True})
        try:  # when a command can be successful send
            self.sock.sendall(pickle_cmd)
            ack = self.sock.recv(128).decode('ascii')
            if 'ack:command1' == ack:
                print('Success send command and ack get')
        except (ConnectionResetError, ConnectionAbortedError):  # when encounter a connection error, auto resume connection
            print('ConnectionResetError: An existing connection was forcibly closed by the remote host')
            self.connect_to_server(self.ip, self.port)

