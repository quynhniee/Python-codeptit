from socket import *

server_name = '127.0.0.1'
server_port = 12000

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name, server_port))

sentence = input('Input lowercase sentence: ')
client_socket.sendall(bytes(sentence, encoding='utf-8'))

modified_sentence = client_socket.recv(1024)
print('From server: ', modified_sentence.decode('utf-8'))

client_socket.close()