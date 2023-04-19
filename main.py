#Python3

import sys
import socket

#this function receives the parameters from the command line
def get_parameters():
    ip_address = sys.argv[1]
    port = sys.argv[2]
    message = sys.argv[3]
    combined = (ip_address, port)
    return combined, message

def socket_connection(url, message):
    with socket.socket() as client_socket:
        client_socket.connect(url)
        message = message.encode()
        client_socket.send(message)
        response = client_socket.recv(1024)
        response = response.decode()
        return response

def main():
    response = socket_connection(get_parameters()[0], get_parameters()[1])
    print(response)
    


if __file__ == "__main__":
    main()
