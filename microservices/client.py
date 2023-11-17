# a client makes requests to a service
import sys
import socket

def myClient():
    '''This client will make requests to our service'''
    cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # match the server
    config_t = ('127.0.0.1', 9876)
    cli.connect(config_t) # match the server
    # if system arguments were provided, concatenate theminto a request string
    if len(sys.argv)>1:
        msg = ', '.join(sys.argv[1:]) # ignore the file name
    else:
        msg = 'Default'
    cli.send(msg.encode()) # always encode for http
    # handle any response
    res = cli.recv(1024)
    print(f'Client received {res}')
    cli.close()

if __name__ =='__main__':
    myClient() 