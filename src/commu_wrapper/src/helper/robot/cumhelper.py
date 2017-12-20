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

class CUMHelper():
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

    def look_manual(self, x, y, z, rate="normal"):
        command = "/look M {} {} {} {}".format(x, y, z, rate)
        self.tcpip.send_message(command)
        ret = self.tcpip.recv_message()
        ret_s1 = ret.split(":")

        if ret_s1[0] == "FAIL":
            self.__logger.error(command)
            return False
        else:
            self.__logger.info(command)
            return True

    def set_config(self, config):
        """
        This function allows for changing the CommUManager's config file while the CommUManager is running.
        Note: the new config file will replace the old configuration and all loaded gestures will be discarded, so
        make sure to include any gestures you want to use in the new config file as well.

        Note: This function might require a fix in the CommUManager C++ code. If gestures are not reloaded after calling
        this function, apply the following fix on the CommU.

        To fix this error, add
        `this->gesture_table->register_gesture_robot(this->robot);`
        at the bottom of the `config_loader` method, line 630, in the `commumanager.cpp` file, located at
        `$COMMU_LIB/usr/local/CommUManager/commumanager.cpp`, where `$COMMU_LIB` is the svn root directory of the
        currently running CommUManager (for me `/home/pi/CommU_v3_rev39`). Then call `make` in the folder containing the
        cpp file and restart the CommU to make the changes effective. After this, reloading the config should be
        possible while the CommUManager is running.
        :param config: The config file to be loaded. Note: not the _name_ of the config file on the CommU, the _entire_
            config file should be passed to this function as a string. For examples, see the file at
            `$COMMU_ROOT/etc/CommU.yml`
        :return: Whether the command was successfully parsed by the CommU.
        """
        command = "/config " + config
        self.tcpip.send_message(command)
        ret = self.tcpip.recv_message()
        ret_s1 = ret.split(':')
        if ret_s1[0] == "FAIL":
            self.__logger.error(command)
            return False
        else:
            self.__logger.info(command)
            return True

    def add_gesture_definition(self, gesture_name, gesture_definition):
        """
        This function adds a gesture while the CommUManager is running. Any previously registered gesture will be
        overwritten.

        :param gesture_name: The name by which the gesture can be activated.
        :param gesture_definition: The definition of the gesture. Note: this is not the _name_ of a gesture.s3r file.
            This parameter should contain the actual contents of a .s3r file.
        :return: Whether the command was successfully parsed by the CommU. This will return false if the gesture
            is incorrect.
        """
        command = "/gesturedef " + gesture_name + "\n" + gesture_definition
        self.tcpip.send_message(command)
        ret = self.tcpip.recv_message()
        ret_s1 = ret.split(':')
        print ret
        if ret_s1[0] == "FAIL":
            self.__logger.error(command)
            return False
        else:
            self.__logger.info(command)
            return True

    def close_connection(self):
        self.tcpip.close_connection()

class CUMHelperDummy(CUMHelper):
    # noinspection PyMissingConstructor
    def __init__(self, host, port, volume=None, logfile="cumhelper.log"):
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

    def look_manual(self,x,y,z,rate="normal"):
        command = "/look M {} {} {} {}".format(x, y, z, rate)
        self.__logger.info(command)
        return True


    def set_config(self, config):
        command = "/config " + config
        self.__logger.info(command)
        return True

    def add_gesture_definition(self, gesture_name, gesture_definition):
        command = "/gesturedef " + gesture_name + "\n" + gesture_definition
        self.__logger.info(command)
        return True

            
if __name__ =='__main__':
    parser = argparse.ArgumentParser(description="utility for CommUManager")
    parser.add_argument("-i","--ipaddress", default="127.0.0.1")
    parser.add_argument("-p","--port", required=True)
    parser.add_argument("-g","--gesture", default="nod1")
    parser.add_argument("-l","--look", default="center")
    args = parser.parse_args()

    #args.ipaddress = "127.0.0.1"

    manager=CUMHelper(args.ipaddress,int(args.port))

    gesture_nr = 1

    #manager.set_config("""\nLookTable:\n  pos_0:\n    name: end\n  ratio_0:\n    name: end\n  speed_0:\n    name: end\n
#\nGestureTable:\n  ges_0:\n    name: tmp_gesture""" + str(gesture_nr) + """\n    file: gesture/tmp_gesture""" + str(gesture_nr) + """.s3r\n  ges_1:\n    name: end\n""")

    # manager.say_eng("Hello, I am CommU.")

    # manager=CUMHelper(args.ipaddress,int(args.port))
    #manager.look_label(args.look,"normal")
    #manager.gesture('tmp_gesture' + str(gesture_nr))
    #manager.gesture('acchi_arm_left')
    #print manager.add_gesture_definition('test_gesture', """0.0 P 0.0 10
#10.0 t""")
    #print manager.gesture('test_gesture')


    try:
        for x in range(-500, 500):
            print x
            print manager.look_manual(x, 200, 200)
    except:
        manager.close_connection()

    #print manager.tcpip.recv_message()
