import socket
import sys


# Making the Socket for the server
def make_socket():
    try:
        global ip 
        global port 
        global sock 
        ip = ""  # It will take our local Computer private IP address as the IP for the socket
        port = 5500
        sock = socket.socket()
    except socket.error as err:
        print("socket Creation Failed : "+str(err))


# Binding the Socket
def bind_socket():
    try:
        global ip 
        global port 
        global sock
        #Binding the port 
        print("Binding The Port : "+str(port))
        sock.bind((ip,port))
        sock.listen(10)
    except socket.error as err:
        print("Socket Binding Failed : "+str(err) +"\n"+"Retrying.....")
        bind_socket()


def accept_connections():
    conn,address = sock.accept()
    print("Connection has been established : "+address[0]+ " : "+str(address[1])+"\n")
    send_message(conn)
    conn.close()

def send_message(conn):
    while True:
        msg = input()
        if msg=="exit":
            conn.close()
            sock.close()
            sys.exit()
        if(len(str.encode(msg))>0):
            conn.send(str.encode(msg))
            client_msg = str(conn.recv(1024),'utf-8')
            print(client_msg ,end="")




def main():
    make_socket()
    bind_socket()
    accept_connections()

main()
