# Microservices can be written in any language. They are interoperable whatever language they use
# The Microservices design pattern breaks a system into parts, each solving a particular problem
# Each service can interact with other services
# we often think of a microservice as application programming interface (API)
import socket # often called socket programming
import requests

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
        if bytebuffer in (b'quit', b'QUIT', b'q', b'Q'):
            client.send(b'you killed the server') # or .encode()
            break  # stop the run loop
        # optionally get the weather (this service acts as a proxy for another service)
        if bytebuffer in (b'Weather', b'weather'):
            try:
                report = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=athlone&units=metric&APPID=957d663a2296945e39a56609740a2548')
                msg = report.json() # Python will convert the JSON into a structure
                client.send( msg.encode() )
            except Exception as e:
                    print(e)
        else:
            response_str = bytebuffer.decode().upper()
            client.send( response_str.encode() )

if __name__ =='__main__':
    myServer()