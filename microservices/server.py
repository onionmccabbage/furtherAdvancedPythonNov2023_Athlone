# Microservices can be written in any language. They are interoperable whatever language they use
# The Microservices design pattern breaks a system into parts, each solving a particular problem
# Each service can interact with other services
# we often think of a microservice as application programming interface (API)
import socket # often called socket programming

def myServer(): # here we use functional programing - could use a class
    '''This simple server will receive client requests
    Response will be the request buffer returned as upper-case'''
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    config_t = ('127.0.0.1', 9876) # same as localhost
    server.bind(config_t) # tell the server which IP and port
    # we may choose to work with multiple clients
    server.listen(4) # begin listening for request
    print(f'Server is listening on {config_t[0]} port {config_t[1]}')
    while True: # this is a run loop
        (client, addr)= server.accept() # we know the client and their address
        print(f'Received from {addr}')
        bytebuffer = client.recv(1024) # the first 1024 bytes of the request object
        print(f'Server received {bytebuffer}')
        response_str = bytebuffer.decode().upper()
        client.send( response_str.encode() )
        # break

if __name__ =='__main__':
    myServer()