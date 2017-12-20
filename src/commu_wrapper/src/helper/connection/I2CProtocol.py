'''
Created on 2015/06/03

@author: arimoto-red
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import struct

class I2CProtocol(object):
    '''
    classdocs
    This is simple client for int(C/C++)-> char [byte]
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.SIZEOF_CINT = 4
        
    def init_connection(self,host,port):
        self.clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.clientsock.connect((host,port))
        except:
            print ("Fail to connect:" + host + "(" + str(port) +")")
        else:
            print ("Success to connect:" + host + "(" + str(port) +")")
        
    def close_connection(self):
        self.clientsock.close()
    
    def send_message(self,message):
        try:
            message = message + "\0"
            print "Sending message.."
            self.clientsock.send(struct.pack("i",len(message)))
            sent = self.clientsock.send(message)
            if sent == 0:
                print "broken"
                raise RuntimeError("socket connection broken")

            print "Sent length: " + repr(sent)
            print "Sent message: " + repr(message)
            print "Message length: " + str(len(message))
        except:
            print ("Fail to send().")
        
    def recv_message(self):
        print "trying to receive message"
        try:
            recv_message1=self.clientsock.recv(self.SIZEOF_CINT)
            length = struct.unpack("i",recv_message1)
        except:
            print ("Fail to recv().")
            return "Fail to recv"
        else:   
            response = self.clientsock.recv(int(length[0]))

            print "Received message: "+ repr(response)
            print "Received length: " + str(len(response))
            print "other "+ str(length)
            return response

'''    
if __name__ == '__main__':
    print "Test start!"
    prot = I2CProtocol()
    prot.init_connection("127.0.0.1", 9004)
    loop = 10
    while loop > 0:
        input_data = raw_input('>>> ')
        prot.send_message(input_data+"\0")
        reply = prot.recv_message()
        print reply
        loop = loop -1
        '''