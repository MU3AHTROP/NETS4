from socket import *
server = 'mail.cs.karelia.ru'
port = 25
frm = 'egor11514@gmail.com'
to = 'ilyukov@cs.karelia.ru'
msg = "\r\n I like nets"
endmsg = "\r\n.\r\n"

# Выбираем почтовый сервер
mailserver = "mail.cs.karelia.ru"

# Создаем сокет clientSocket и устанавливаем TCP-соединение
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((server, port))

recv = clientSocket.recv(1024)
print(recv)
if recv[:3] != b'220':
    print('Код 220 от сервера не получен.')

# Отправляем команду HELO и выводим ответ сервера.
heloCommand = 'HELO example.com\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024)
print(recv1)
if recv1[:3] != b'250':
    print('Код 250 от сервера не получен.')

# Отправляем команду MAIL FROM и выводим ответ сервера.
mailFromCommand = 'MAIL FROM: <egor11514@gmail.com>\r\n'
clientSocket.send(mailFromCommand.encode())
recv2 = clientSocket.recv(1024)
print(recv2)

# Отправляем команду RCPT TO и выводим ответ сервера.
rcptToCommand = 'RCPT TO: <ilyukov@cs.petrsu.ru>\r\n'
clientSocket.send(rcptToCommand.encode())
recv3 = clientSocket.recv(1024)
print(recv3)

# Отправляем команду DATA и выводим ответ сервера.
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())
recv4 = clientSocket.recv(1024)
print(recv4)

# Отправляем данные сообщения.
clientSocket.send(msg.encode())

# Сообщение завершается одинарной точкой.
clientSocket.send(endmsg.encode())

# Отправляем команду QUIT, получаем ответ сервера
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())
recv5 = clientSocket.recv(1024)
print(recv5)

# Закрываем соединение.
clientSocket.close()