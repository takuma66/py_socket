import socket
import time

def disk_check():
    return True

def inode_check():
    return False

def send_warning(ip, port, type):
        sct = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sct.connect((ip, port))
        sct.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #sct.send(bytes("Message is sent.", 'utf-8'))
        sct.send(bytes(socket.gethostname) + " " + type, "utf-8")
        sct.close()
        exit()

ip = "127.0.0.1"
port = 12345

while True:
    if disk_check():
        send_warning(ip, port, "disk")
    
    if inode_check():
        send_warning(ip, port, "inode")

    time.sleep(30)