"""
FILE_NAME: config_utils.py
AUTHOR: RCB
CREATED: 2024/4/28-18:11
DESC:管理一些默认配置
"""
import json
import sys
import os

config_base = os.path.expanduser('~\\AppData\\Local\\GLToolsConfig')


class CommonConfigMgr(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(CommonConfigMgr, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class ConfigMgr:
    data_dict = {}
    def __init__(self, key):
        self.main_key = key
        self.load_cfg_data()

    def make_cfg_file_name(self):
        file_path = os.path.join(config_base, self.main_key, "setting.json")
        return file_path

    # 加载配置
    def load_cfg_data(self):
        file_path = self.make_cfg_file_name()
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                self.data_dict = json.load(f)
        else:
            self.data_dict = {}

    # 保存配置
    def save_cfg_data(self):
        file_path = self.make_cfg_file_name()
        if not os.path.exists(os.path.dirname(file_path)):
            os.makedirs(os.path.dirname(file_path))
        with open(file_path, "w") as f:
            json.dump(self.data_dict, f, indent=4)

    def get_data(self, sub_key, default_value=None):
        if sub_key not in self.data_dict:
            return default_value
        return self.data_dict[sub_key]

    def set_data(self, sub_key, value):
        self.data_dict[sub_key] = value
        self.save_cfg_data()