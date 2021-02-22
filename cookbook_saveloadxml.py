"""
Title : cookbook_saveloadxml.py

Description: Cookbook of Python program that can save param to xml and load from xml

Author: Runnan Li

**Revision History:**

+---------+------------+------------+-----------------------------------------------------+
| Version |     Date   |   Author   |                  Change Description                 |
+---------+------------+------------+-----------------------------------------------------+
|   0.1   | 22/02/2021 | Runnan Li  |                   Initial Version                   |
+---------+------------+------------+-----------------------------------------------------+
"""
import xml.etree.ElementTree as ET


class SaveLoadXml:
    """
    Settings manager manages load and read settings from .xml file shared among Equipment2CAN project drivers.
    """
    @staticmethod
    def load_settings(file='settings.xml'):
        """
        Load settings from settings.xml file.

        :param file: optional for other .xml file. If uses please make sure schema is correct.
        :return: :meth:'dict' of loaded settings
        """
        settings_dict = {}
        tree = ET.parse(file)
        settings_dict['can_channel'] = tree.find('connections/LVPS_TENMA/can_channel').text
        settings_dict['can_app'] = tree.find('connections/LVPS_TENMA/can_application').text
        settings_dict['com_port'] = tree.find('connections/LVPS_TENMA/COM_port').text
        settings_dict['com_baud'] = tree.find('connections/LVPS_TENMA/COM_baud').text
        settings_dict['dbc_path'] = tree.find('connections/LVPS_TENMA/dbc_path').text
        return settings_dict

    @staticmethod
    def save_settings(save_dict, file='settings.xml'):
        """
        Save settings to settings.xml file.

        :param save_dict: save settings dictionary
        :param file: optional for other .xml file. If uses please make sure schema is correct.
        """
        tree = ET.parse(file)
        tree.find('connections/LVPS_TENMA/can_channel').text = str(save_dict['can_channel'])
        tree.find('connections/LVPS_TENMA/can_application').text = save_dict['can_app']
        tree.find('connections/LVPS_TENMA/COM_port').text = save_dict['com_port']
        tree.find('connections/LVPS_TENMA/COM_baud').text = str(save_dict['com_baud'])
        if save_dict['dbc_path'] is None:
            tree.find('connections/LVPS_TENMA/dbc_path').text = ''
        else:
            tree.find('connections/LVPS_TENMA/dbc_path').text = save_dict['dbc_path']
        tree.write(file)
