from __future__ import print_function
import socket
from contextlib import closing

class TCPServer:
  HOST = '127.0.0.1'
  PORT = 8080
  backlog = 10
  bufsize = 4096
  def Listen(self,host,port):
      self.HOST=host
      self.PORT=port
      self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      self.sock.bind((host, port))
      self.sock.listen(self.backlog)
      self.conn, address = self.sock.accept()
  def Recv(self,bufsize):
      return self.conn.recv(bufsize)
  def Send(self,data):
      self.conn.send(data)
  def Close(self):
      self.conn.close()
      self.sock.close()

class TCPClient:
  HOST = '127.0.0.1'
  PORT = 8080
  bufsize = 4096
  def Connect(self,host,port):
      self.HOST=host
      self.PORT=port
      self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.sock.connect((host, port))

  def Recv(self,bufsize):
      return self.sock.recv(bufsize)
  def Send(self,data):
      self.sock.send(data)
  def Close(self):
      self.sock.close()
