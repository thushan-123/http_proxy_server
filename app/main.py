import socket
import signal
import threading


def main(): 
    IP : str = "127.0.0.1"
    PORT :int = 8000
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((IP,PORT))

    server.listen()

    print(f"Proxy Server Listen On PORT : {PORT}")

    #listen the port incomming client request

    while True :
        client_socket , address = server.accept()
        print (client_socket)
        print(address)



if __name__ == "__main__":
    main()