#Python3

import sys
import itertools

#this function receives the parameters from the command line
def get_parameters():
    ip_address = sys.argv[1]
    port = int(sys.argv[2])
    combined = (ip_address, port)
    return combined

def get_passwords():
    passwords = []
    with open("passwords.txt", "r") as file:
        for line in file:
            passwords.append((lambda x: ''.join(x), itertools.product(*([letter.lower(), letter.upper()] for letter in line))))
    return passwords

#this function tests all possible case options for provided passwords

def socket_connection():
    for message in get_passwords():
        if "qWeRtY" in message:
            return message

def main():
    password = socket_connection()
    print(password)


main()
