#coding:utf-8
import stomp
import time

class StompHelper:
    topic=""
    def __init__(self,_ip,_port,_topic):
        self.ip=_ip
        self.port=_port
        self.topic=_topic
        self.conn = stomp.Connection10([(self.ip,self.port)])
        self.conn.start()
        self.conn.connect()
        #self.conn.send(self.topic,"test")
        
    def post(self,mes):
        #conn = stomp.Connection10([("129.60.160.165",61613)])
        self.conn.send(self.topic,mes)
    def close(self):
        self.conn.disconnect()

if __name__=="__main__":
    ptr = StompHelper("127.0.0.1",61613,"/topic/recog")
    ptr.post("arimoto")
    ptr.close()

