import socket
import ssl
import smtplib
import base64
import os
from EmailMessage import EmailMessage
from EmailMessageBuilder import EmailMessageBuilder

hostname = 'smtp.gmail.com'
username = os.environ.get('GMAIL_USERNAME')
password = os.environ.get('GMAIL_PASSWORD')

b64username = base64.b64encode(username.encode()).decode()
b64password = base64.b64encode(password.encode()).decode()

sslPort = '465'
context = ssl.create_default_context()
bufferSize = (1 << 12)


def sendMessage(socket, msg):
    socket.send(f'{msg}\r\n'.encode())
    return socket.recv(bufferSize).decode()

    
def sendEmail(clientSocket):
    #S: 220 <mail_server_domain>
    serverIntroduction = clientSocket.recv(bufferSize).decode()
    print(serverIntroduction)
    
    if '220' not in serverIntroduction:
        print('SMTP handshake failed')
        return
    
    resp = sendMessage(clientSocket,'HELO ucsd.edu')
    print(resp)
    if '250' not in resp:
        print('SMTP won\'t allow this client')
        
    resp = sendMessage(clientSocket,'AUTH LOGIN')
    print(resp)

    
    clientSocket.send(f'{b64username}\r\n'.encode())
    resp = clientSocket.recv(bufferSize).decode()
    print(resp)
    
    clientSocket.send(f'{b64password}\r\n'.encode())
    resp = clientSocket.recv(bufferSize).decode()
    print(resp)
    
    resp = sendMessage(clientSocket,f'MAIL FROM: <{username}>')
    print(resp)
    
    resp = sendMessage(clientSocket,f'RCPT TO: <{username}>')
    print(resp)
    
    resp = sendMessage(clientSocket,'DATA')
    print(resp)
    
    emailMessage = EmailMessageBuilder()\
    .addHeaderField(EmailMessage.TO, username)\
    .addHeaderField(EmailMessage.FROM, username)\
    .addHeaderField(EmailMessage.SUBJECT,"Python SMTP test")\
    .setBody("I just sent you an email using ssl socket library in python Check it out here.. https://github.com/EddieCarrillo/Python-Mail-Client\n\n\nDon't be mad that I am styling all over you brahs\n\nSincerely \n-Eddie ")\
    .create()\
    .message()
    clientSocket.send(f'{emailMessage}\r\n'.encode())
    clientSocket.send('.\r\n'.encode())
    resp = clientSocket.recv(bufferSize).decode()
    print(resp)
    
def main():
    with socket.create_connection((hostname, sslPort)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            sendEmail(ssock)


if __name__ == '__main__' : main()