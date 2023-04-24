#Python3

import sys
import socket
import itertools

#this function receives the parameters from the command line
def get_parameters():
    ip_address = sys.argv[1]
    port = int(sys.argv[2])
    combined = (ip_address, port)
    return combined

def get_passwords():
    passwords = []
    with open("/passwords.txt", "r") as file:
        for line in file:
            yield line.strip()
            passwords.append(line.strip())
    return passwords

def brute_force():
    passwords = get_passwords()
    yield map(lambda x: ''.join(x), itertools.product(*([letter.lower(), letter.upper()] for letter in passwords)))


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
