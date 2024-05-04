from socket import *
import ssl
import base64

server = 'smtp.gmail.com'
port = 465
frm = 'egor11514@gmail.com'
to = 'egor11514@gmail.com'
msg = "\r\n Я люблю компьютерные сети!"
endmsg = "\r\n.\r\n"
# Создаем сокет clientSocket и устанавливаем TCP-соединение
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((server, port))
clientSocketSSL = ssl.wrap_socket(clientSocket)
recv = clientSocketSSL.recv(1024)
print(recv)
if recv[:3] != b'220':
    print('Код 220 от сервера не получен.')

# Обернем сокет в SSL соединение

# Отправляем команду HELO и выводим ответ сервера.
heloCommand = 'HELO example.com\r\n'
clientSocketSSL.send(heloCommand.encode())
recv1 = clientSocketSSL.recv(1024)
print(recv1)
if recv1[:3] != b'250':
    print('Код 250 от сервера не получен.')

# Отправляем команду AUTH LOGIN для аутентификации
authCommand = 'AUTH LOGIN\r\n'
clientSocketSSL.send(authCommand.encode())
recv_auth = clientSocketSSL.recv(1024)
print(recv_auth)

# Отправляем закодированные данные для аутентификации
username = base64.b64encode("egor11514@gmail.com".encode())
password = base64.b64encode("Пароль приложения".encode())
clientSocketSSL.send(username + b'\r\n')
recv_user = clientSocketSSL.recv(1024)
print("first",recv_user)

clientSocketSSL.send(password + b'\r\n')
recv_pass = clientSocketSSL.recv(1024)
print("second",recv_pass)

# Отправляем команду MAIL FROM и выводим ответ сервера.
mailFromCommand = 'MAIL FROM: <egor11514@gmail.com>\r\n'
clientSocketSSL.send(mailFromCommand.encode())
recv2 = clientSocketSSL.recv(1024)
print(recv2)

# Отправляем команду RCPT TO и выводим ответ сервера.
rcptToCommand = 'RCPT TO: <egor11514@gmail.com>\r\n'
clientSocketSSL.send(rcptToCommand.encode())
recv3 = clientSocketSSL.recv(1024)
print(recv3)

# Отправляем команду DATA и выводим ответ сервера.
dataCommand = 'DATA\r\n'
clientSocketSSL.send(dataCommand.encode())
recv4 = clientSocketSSL.recv(1024)
print(recv4)

# Отправляем данные сообщения.
clientSocketSSL.send(msg.encode())

# Сообщение завершается одинарной точкой.
clientSocketSSL.send(endmsg.encode())

# Отправляем команду QUIT, получаем ответ сервера
quitCommand = 'QUIT\r\n'
clientSocketSSL.send(quitCommand.encode())
recv5 = clientSocketSSL.recv(1024)
print(recv5)

# Закрываем соединение.
clientSocketSSL.close()