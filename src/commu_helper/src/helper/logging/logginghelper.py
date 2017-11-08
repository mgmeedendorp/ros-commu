#!/usr/bin/env python
# coding: utf-8
#あんまり意味ないかもしれないけど，ロガーを作るユーティリティ
# @author arimoto
# @date 2017.5.25

import logging

def get_basic_file_handle(_filename, _lvl):
    pf = logging.FileHandler(filename=_filename)
    pf.setLevel(_lvl)
    pf.setFormatter(get_basic_formatter())
    return pf

def get_basic_formatter():
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    return formatter

def get_filelogger(_loggername, _filename="logginghelper.log", _lvl=logging.DEBUG):
    if not hasattr(get_filelogger,'logfilelist'):
        get_filelogger.logfilelist = []

    ret_logger = logging.getLogger(_loggername)
    if _loggername not in get_filelogger.logfilelist:
        ret_logger.setLevel(_lvl)
        ret_logger.addHandler(get_basic_file_handle(_filename,_lvl))
        get_filelogger.logfilelist.append(_loggername)
    return ret_logger
