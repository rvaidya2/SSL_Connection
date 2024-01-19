# Client side

import socket, ssl,sys

server_domain = sys.argv[1]
server_port = int(sys.argv[2])

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations('cert.pem')
context.check_hostname = False

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    with context.wrap_socket(sock, server_hostname=server_domain) as sslsock:
        sslsock.connect((server_domain, server_port))
        
        userid = input('Enter userid: ')
        password = input('Enter password: ')
        sslsock.send((userid + ' ' + password).encode())
        
        data = sslsock.recv(1024)
        print(data.decode())