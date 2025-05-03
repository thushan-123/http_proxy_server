import socket

class ConnectDestination():

    def __init__(self, clientSocket: socket.socket):
        self.clientSocket = clientSocket

    def sendRequestDestination(self,webServerIp: str, port: int, request):
        destinationServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        destinationServer.connect((webServerIp,port))
        destinationServer.sendall(request)

        # recive data from web server

        while True:
            data: bytes = destinationServer.recv(1024)
            if len(data) >0:
                return data
                # self.clientSocket.send(data)
            else:
                break

class HttpClientRequest():
    
    def __init__(self, httpRequest):
        self.httpRequest :bytes = httpRequest.decode("utf-8")

    def getHost(self):
        hostStartIndex :int = self.httpRequest.find("Host: ") + len("Host: ")
        portEndIndex :int = self.httpRequest.find("\n", hostStartIndex)

        # host ip not in request raise the runtime error
        if hostStartIndex == -1:
            hostStartIndex :int = self.httpRequest.find("host: ") + len("host: ")
            if hostStartIndex == -1:
                raise RuntimeError("can not find host ip")

        host :str = self.httpRequest[hostStartIndex: portEndIndex]

        portStartIndex :int = host.find(":")
        print(portStartIndex)

        # port is not define set default port 80
        if portStartIndex == -1:
            hostIp: str = host
            port :int = 80
        else:
            hostIp = host[:portStartIndex]
            port = int(host[portStartIndex + 1:])
        
        return hostIp, port
    
