#Server side

import socket, ssl, hashlib
from socketserver import ThreadingMixIn, TCPServer, StreamRequestHandler

class SslServer(ThreadingMixIn, TCPServer):
    def __init__(self, server_address, RequestHandlerClass, certfile, keyfile):
        TCPServer.__init__(self, server_address, RequestHandlerClass)
        self.certfile = certfile
        self.keyfile = keyfile

class SslRequestHandler(StreamRequestHandler):
    def handle(self):
        print('connection from', self.client_address)
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(self.server.certfile, self.server.keyfile)
        ssl_sock = context.wrap_socket(self.connection, server_side=True)

        data = ssl_sock.read()
        if not data:
            ssl_sock.close()
            return

        userid, password = data.decode().split(' ')
        hashed_password = None  


        with open('hashpasswd', 'r') as f:
            for line in f:
                parts = line.split(' ')
                if parts[0] == userid:
                    hashed_password = parts[1].strip()
                    print(hashed_password)
                    break

        if hashed_password is not None:
            if hashlib.sha256(password.encode()).hexdigest() == hashed_password:
                # print("Correct")
                ssl_sock.write(b'Correct ID and password')
            else:
                # print("Wrong")
                ssl_sock.write(b'The ID/password is incorrect')
        else:
            # print("ID does not exist")
            ssl_sock.write(b'ID does not exist, run genpasswd.py to create one')  # Send a response for non-existent ID

        ssl_sock.close()

if __name__ == '__main__':
    import sys
    server_address = ('', int(sys.argv[1]))
    server = SslServer(server_address, SslRequestHandler, 'cert.pem', 'key.pem')
    server.serve_forever()
