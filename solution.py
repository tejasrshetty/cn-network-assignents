from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    # mailserver = ("smtp.aol.com", 25)

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    mailserver_and_port = (mailserver,1025)
    clientSocket.connect(mailserver_and_port)

    # Fill in end
    recv = clientSocket.recv(1024).decode()

    # Send HELLO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()

    # Send MAIL FROM command and print server response.
    # Fill in start
    fromCommand = 'MAIL FROM: <' + "Papercut@papercut.com" + '>\r\n'
    clientSocket.send(fromCommand.encode())
    recv2 = clientSocket.recv(1024)
   # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    toCommand = 'RCPT TO: <' + "Papercut@papercut.com" + '>\r\n'
    clientSocket.send(toCommand.encode())
    recv3 = clientSocket.recv(1024)
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode())
    recv4 = clientSocket.recv(1024)
    # Fill in end

    # Send message data.
    # Fill in start
    text = bytes("Message:",'utf-8')
    clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    clientSocket.send(endmsg.encode())
    recv_msg = clientSocket.recv(1024)
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    quit = "QUIT\r\n"
    clientSocket.send(quit.encode())
    # recv5 = clientSocket.recv(1024)
    clientSocket.close()
    # Fill in end

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
