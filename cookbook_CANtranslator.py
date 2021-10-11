"""
Description: a simple Python CAN messaging method to control other device
Pre-requisite: Vector_CAN_API
"""
from Vector_CAN_API import Vector_CAN
import threading
import random


class CANtralslator():
    def __init__(self, channel, can_app, dbc):
        """
        Create translator instance

        :param channel: channel No of CAN starting from 0
        :param can_app: CAN application
        :param dbc: CAN .dbc file path
        """
        self.bus = Vector_CAN(channel, can_app)  # init CAN channel obj
        self.dbc = self.bus.LoadDbc(dbc)  # load .dbc
        self.translator_active = True  # thread control

    def do_on_msg1(self, signal_dict):
        """
        When Message1 received, what need to do

        :param signal_dict: Signals read dict in Message1
        :return:
        """
        print('Message1::Msg1_Sig1 ==', signal_dict['Msg1_Sig1'], '    ',
              'Message1::Msg1_Sig2 ==', signal_dict['Msg1_Sig2'])
        self.bus.SendCanMsgByName('ACK', {'ACK_Sig': 'on'})

    def do_on_msg2(self, signal_dict):
        """
        When Message2 received, what need to do

        :param signal_dict: Signals read dict in Message1
        :return:
        """
        print('Message1::Msg2_Sig1 ==', signal_dict['Msg2_Sig1'])
        self.bus.SendCanMsgByName('Response', {'Current': random.randrange(0, 10, 1),
                                               'Voltage': random.randrange(0, 100, 1),
                                               'Power': random.randrange(0, 10, 1),
                                               'Temperature': random.randrange(0, 10, 1)})

    def translator_thread(self):
        """
        Thread that translator emulates as a CAN node, listens message and call action functions.

        Link your Message - action function in message_map dictionary
        :return:
        """
        message_map = {
            'Message1': self.do_on_msg1,
            'Message2': self.do_on_msg2,
        }
        print('Start listening CAN message')
        while self.translator_active:
            try:
                msg_raw = self.bus.ReadMessageOnBus()  # get available message on bus in real time
                signal_dict = self.bus.DecodeCanMsg(msg_raw)  # decode the signals see if in .dbc
                msg_name = self.dbc.get_message_by_frame_id(msg_raw.arbitration_id).name  # decode the message name
                message_map[msg_name](signal_dict)  # do actions depend on message
            except KeyError:  # when msg not in dbc (continue or do something you want)
                continue  # customizable

    def start(self):
        """
        start translator for external switch on thread.
        :return:
        """
        translator_th = threading.Thread(target=self.translator_thread, args=())
        translator_th.start()

    def stop(self):
        """
        Toggle stop of thread.
        :return:
        """
        self.translator_active = False


if __name__ == "__main__":
    handle = CANtralslator(2, 'CANalyzer', 'cookbook_dbc.dbc')
    handle.start()
