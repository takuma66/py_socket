connect_to = "127.0.0.1"
port = 12345
sss = socket.gethostname()
while True:
    time.sleep(2)
    if disk_check():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((connect_to, 12345))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.send(bytes("There is no disk availability.", 'utf-8'))
        s.close()
        exit()