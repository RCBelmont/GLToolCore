"""
FileName:   file_utils.py
Author:     RCB
Created on 2024.09.24 17:29
Description:

"""
import os
import sys

def is_frozen():
    return getattr(sys, 'frozen', False)

def file_utils_get_root_path():
    '''
    获取根目录路径
    :return:
    '''
    if is_frozen():
        return os.path.join(os.getcwd(), "Data")
    return os.getcwd()


def file_utils_get_core_shader_path():
    '''
    获取核心着色器路径
    :return:
    '''
    return os.path.join(file_utils_get_root_path(), "Core", "Shaders")


def file_util_get_entry_path():
    '''
    获取入口路径
    :return:
    '''
    return os.path.dirname(sys.argv[0])


def file_utils_get_default_shader_path(shader_name: str):
    '''
    获取着色器路径
    :param shader_name:
    :return:
    '''
    if is_frozen():
        shader_path = os.path.join(sys._MEIPASS, "Shaders", shader_name)
    else:
        shader_path = os.path.join(file_util_get_entry_path(), "Shaders", shader_name)
    if not os.path.exists(shader_path):
        raise FileNotFoundError(f"Shader file not found: {shader_path}")
    return shader_path



