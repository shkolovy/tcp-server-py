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

        print('--------')
        print(str(sock.recv(1024), "utf-8"))
        print('--------')

        input_mes = 'type email: '
        mes = input(input_mes)

        while mes != 'q':
            sock.send(mes.encode())

            # Receive data from the server and shut down
            print(str(sock.recv(1024), "utf-8"))
            mes = input(input_mes)

    except ConnectionRefusedError:
        print('can\'t connect to the server {}:{}'.format(host, port))
    finally:
        sock.close()


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        HOST, PORT = sys.argv[1], int(sys.argv[2])
        init(HOST, PORT)

    init()