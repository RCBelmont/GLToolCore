"""
FileName:   file_utils.py
Author:     RCB
Created on 2024.09.24 17:29
Description:

"""
import os
import Core


def file_utils_get_root_path():
    '''
    获取根目录路径
    :return:
    '''
    if Core.is_frozen():
        return os.path.join(os.getcwd(), "Data")
    return os.getcwd()


def file_utils_get_core_shader_path():
    '''
    获取核心着色器路径
    :return:
    '''
    return os.path.join(file_utils_get_root_path(), "Core", "Shaders")
