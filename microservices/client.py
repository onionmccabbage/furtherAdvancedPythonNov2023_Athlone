# a client makes requests to a service

import socket

def myClient():
    '''This client will make requests to our service'''
    cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # match the server
    config_t = ('127.0.0.1', 9876)
    cli.connect(config_t) # match the server
    msg = 'quit'
    cli.send(msg.encode()) # always encode for http
    # handle any response
    res = cli.recv(1024)
    print(f'Client received {res}')
    cli.close()

if __name__ =='__main__':
    myClient() 