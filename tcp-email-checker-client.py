import socket
import sys

def init(host = 'localhost', port=9000):
    """
    Init socket client
    """

    print('connecting to {}:{}...'.format(host, port))

    # Create a socket (SOCK_STREAM means a TCP socket)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to server and send data
        sock.connect((host, port))
        sock.send(input('type email: ').encode())

        # Receive data from the server and shut down
        print(str(sock.recv(1024), "utf-8"))
    except ConnectionRefusedError:
        print('can\'t connect to the server {}:{}'.format(host, port))
    finally:
        sock.close()


if __name__ == "__main__":
    HOST, PORT = '' or sys.argv[1], '' or int(sys.argv[2])
    init(HOST, PORT)
