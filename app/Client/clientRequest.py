import socket

def handle_client_request():
    pass


request_text = b"""GET http://192.168.8.12:800/indc.kl HTTP/1.1
Host: 192.168.8.12:443
User-Agent: curl/8.12.1
Accept: */*
Proxy-Connection: Keep-Alive"""

print(request_text)


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
    
    def getHeaders(self):
        headersSplit :list = self.httpRequest.split("\n")
        

        for header in headersSplit:
            print(header.strip())
            print(header.split(":"))
            
        



http = HttpClientRequest(request_text)
ip, port = http.getHost()

http.getHeaders()

print(ip)
print(port)


# python .find()  value not in string return -1