import socketserver
import re
import sys

class EmailCheckerTCPHandler(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for EmailChecker server.
    """
    def get_request(self):
        self.request.sendall('dddd')

    
    def isEmailValid(self, email):
        checker = re.compile('^[a-b][\w-]+@[a-z0-9-]+\.[a-z]{1,3}$')
        return checker.match(email)

    def handle(self):
        # while True:
            # self.request is the TCP socket connected to the client
            data = self.request.recv(1024).strip().decode("utf-8")
            print('{} wrote:'.format(self.client_address[0]))
            print('checking {}'.format(data))
            
            resultMes = '{0} is {1}'.format(data, 'valid' if self.isEmailValid(data) else 'not valid\n')
            print(resultMes)

            # send result
            self.request.send(resultMes.encode())

def init(host = 'localhost', port=9000):
    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((host, port), EmailCheckerTCPHandler)
    print('server created {}:{}'.format(host, port))
    
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()

if __name__ == "__main__":
    HOST, PORT = sys.argv[1], int(sys.argv[2])
    init(HOST, PORT)


