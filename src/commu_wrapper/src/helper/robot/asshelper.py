#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author arimoto
# @date 2017.5.29
#
# 機能
# ・ASSシナリオのロードと実行
# ・ロギング

import time
import sys,os
import datetime
from time import sleep

sys.path.append(os.path.abspath("../../"))
from helper.connection.I2CProtocol import I2CProtocol
from helper.logging.logginghelper import get_filelogger

class ASSHelper(object):
    def __init__(self,host,port,logfile="robot.log"):
        self.__logger = get_filelogger("ASSHELPER",logfile)
        try:
            self.tcpip = I2CProtocol()
            self.tcpip.init_connection(host,port)
        except:
            self.__logger.error("Fail to initialize tcpip connection")
            exit()
        self.__logger.info("stanby")

    def load_scenario(self,name):
        command_load = "/load t " + name
        self.tcpip.send_message(command_load)
        ret = self.tcpip.recv_message()
        ret_s1 = ret.split(":")
        if ret_s1[0] == "FAIL":
            self.__logger.error(command_load)
            return "-1"

        load_id = ret_s1[3].split("id=")[1]
        self.__logger.info(command_load+" => load_id="+load_id)

        while 1:
            command_check = "/check t "+load_id
            self.tcpip.send_message(command_check)
            ret_check = self.tcpip.recv_message()
            ret_check_s1 = ret_check.split(":")
            if "FAIL" in ret_check_s1 or "fail" in ret_check_s1 or "Fail" in ret_check_s1:
                self.__logger.error("FAIL to CHECK:(%s)" + ret_check)
                return "-1"
            elif ret_check_s1[4].find("STANDBY") > -1:
                break
            sleep(0.1)
        return load_id

    def exe_scenario(self,load_id):
        command = "/exe t "+load_id
        self.tcpip.send_message(command)
        ret_exe = self.tcpip.recv_message()
        self.__logger.info(command)

    def continue_scenario(self,load_id):
        command = "/continue t "+load_id
        self.tcpip.send_message(command)
        ret_exe = self.tcpip.recv_message()
        self.__logger.info(command)

    def check_scenario(self,load_id):
        command = "/check t "+load_id
        self.tcpip.send_message(command)
        ret_exe = self.tcpip.recv_message()
        self.__logger.info(command)
        return ret_exe


    def wait_for_standby(self, load_id):
        ret="-1"
        while 1:
            command_check = "/check t "+load_id
            self.tcpip.send_message(command_check)
            ret_check = self.tcpip.recv_message()
            if ret_check.find("EXECUTING") and not ret_check.find("FAIL"):
                sleep(1.0)
            elif ret_check.find("FAIL"):
                self.__logger.error("Fail to execute sid=" + load_id)
                break
            else:
                self.__logger.info("success to complete sid=" + load_id)
                ret = load_id
                break
        return ret

class ASSHelperDummy(object):
    def __init__(self,host,port,logfile="robot.log"):
        self.__logger = get_filelogger("ASSHELPER_DUMMY",logfile)
        self.__logger.info("stanby")
        self.load_id = 0

    def load_scenario(self,name):
        command_load = "/load t " + name
        load_id = self.load_id
        self.load_id += 1
        self.__logger.info(command_load+" => load_id="+str(load_id))
        return str(load_id)

    def exe_scenario(self,load_id):
        command = "/exe t "+load_id
        self.__logger.info(command)

    def wait_for_standby(self, load_id):
        self.__logger.info("success to complete sid=" + load_id)
        return load_id

            
if __name__ =='__main__':
    argvs = sys.argv
    argc = len(argvs)
    if argc != 3:
        print ("aruguments is invalid")
        print("python ./program [port of ASS2] [scenario file]")
        quit()
    portname = argvs[1]
    scnname = argvs[2]
    
    manager=ASSHelper("127.0.0.1",int(portname))
    id = manager.load_scenario(scnname)
    manager.exe_scenario(id)

