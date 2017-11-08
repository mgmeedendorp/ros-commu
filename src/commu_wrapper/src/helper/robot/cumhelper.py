'''
Updated on 2017.5.25
Created on 2015/10/03
@author: arimoto
'''

from time import sleep
import sys,os
import argparse
sys.path.append(os.path.abspath("../../"))
from helper.connection.I2CProtocol import I2CProtocol
from helper.logging.logginghelper import get_filelogger

class CUMHelper(object):
    def __init__(self,host,port,volume=None,logfile="cumhelper.log"):
        self.__logger = get_filelogger("CUMHELPER-"+str(port),logfile)

        try:
            self.tcpip = I2CProtocol()
            self.tcpip.init_connection(host,port)
        except:
            self.__logger.error("Fail to initialize tcpip connection")
            exit()
        if volume != None:
            self.chvolume(volume)
        self.__logger.info("stanby")
        
    def chvolume(self,volume):
        command = "/aitalk-volume " + str(volume)
        self.tcpip.send_message(command)
        ret = self.tcpip.recv_message()
        ret_s1 = ret.split(":")
        if ret_s1[0] == "FAIL":
            self.__logger.error(command)
            return False
        else:
            self.__logger.info(command)
            return True

    def say(self,text,blocking=False):
        command = "/say { " + text + " }"
        self.tcpip.send_message(command)
        ret = self.tcpip.recv_message()
        ret_s1 = ret.split(":")
        if ret_s1[0] == "FAIL":
            self.__logger.error(command)
            return False
        else:
            self.__logger.info(command)

            if blocking:
                sleep(len(text) * (1.0/6.5)/3.0 + 1.5)

            return True

    def say_eng(self,text,blocking=False):
        command = "/say_eng { " + text + " }"

        self.tcpip.send_message(command)
        ret = self.tcpip.recv_message()
        ret_s1 = ret.split(":")
        if ret_s1[0] == "FAIL":
            self.__logger.error(command)
            return False
        else:
            self.__logger.info(command)

            if blocking:
                sleep(len(text) * (1.0/6.5)/3.0 + 1.5)

            return True

    def gesture(self,gesturefile):
        command = "/gesture " + gesturefile
        self.tcpip.send_message(command)
        ret = self.tcpip.recv_message()
        ret_s1 = ret.split(":")
        if ret_s1[0] == "FAIL":
            self.__logger.error(command)
            return False
        else:
            self.__logger.info(command)
            return True

    def look_label(self,label,cr,kinect=False):
        command = ""
        if kinect:
            command = "/look L " + "kinect-"+label+"-"+cr
        else:
            command = "/look L " + label+"-"+cr
        self.tcpip.send_message(command)
        ret = self.tcpip.recv_message()
        ret_s1 = ret.split(":")
        if ret_s1[0] == "FAIL":
            self.__logger.error(command)
            return False
        else:
            self.__logger.info(command)
            return True

class CUMHelperDummy(object):
    def __init__(self,host,port,volume=None,logfile="cumhelper.log"):
        self.__logger = get_filelogger("CUMHELPER_DUMMY-"+str(port),logfile)
        self.__logger.info("stanby")
        
    def chvolume(self,volume):
        command = "/aitalk-volume " + str(volume)
        self.__logger.info(command)
        return True

    def say(self,text,blocking=False):
        command = "/say { " + text + " }" if not blocking else "/say-b { " + text + " }"
        self.__logger.info(command)
        return True

    def gesture(self,gesturefile):
        command = "/gesture " + gesturefile
        self.__logger.info(command)
        return True

    def look_label(self,label,cr,kinect=False):
        command = "/look L " + label+"-"+cr
        self.__logger.info(command)
        return True

            
if __name__ =='__main__':
    parser = argparse.ArgumentParser(description="utility for CommUManager")
    parser.add_argument("-i","--ipaddress", default="127.0.0.1")
    parser.add_argument("-p","--port", required=True)
    parser.add_argument("-g","--gesture", default="nod1")
    parser.add_argument("-l","--look", default="center")
    args = parser.parse_args()

    manager=CUMHelper(args.ipaddress,int(args.port))
    manager.say_eng("Hello, I am CommU.")

    # manager=CUMHelper(args.ipaddress,int(args.port))
    # manager.look_label(args.look,"normal")
    # manager.gesture(args.gesture)

