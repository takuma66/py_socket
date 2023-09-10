import socket
import mail

connect_to = "127.0.0.1"
port = 12345
mail_to = "kanza414@gmail.com"
mail_from = "mail_test@itec.hankyu-hanshin.co.jp"

sct = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sct.bind(("127.0.0.1", port))
sct.listen(1)

while True:
    clientsocket, address = sct.accept()
    #print("Connection is established by {}".format(address))
    msg = clientsocket.recv(1024).decode("utf-8")
    #print(msg)
    clientsocket.close()
    mail_message = mail.createMIMEText(mail_from, mail_from, msg, "Test Mail")
    mail.send_Mail(mail_message)